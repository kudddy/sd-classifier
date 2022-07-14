import re
import threading
from glob import glob
from typing import List
import codecs
from queue import Queue

import dill

try:
    from ..config import cfg
    from ...plugins.duckling.morph_analyzer import text_list
    from ...plugins.db.upload_model import download_model
except Exception as e:
    from plugins.config import cfg
    from plugins.duckling.morph_analyzer import text_list
    from plugins.db.upload_model import download_model


class Preprocessing:
    def __init__(self):
        self.brand_token = 'brand_token'

    @staticmethod
    def mask_mark_token(word: str):
        return word

    def mask_mark(self, word_list: List[str]):
        mask_word_list = [self.mask_mark_token(word) for word in word_list]
        return mask_word_list

    @staticmethod
    def preprocess_string(string):
        string = re.sub(r'([!.,?] )+', r' ', string)
        string = string.strip('?.!, ')
        string = string.lower()
        return string

    @staticmethod
    def mask_digits(string):
        string = re.sub(r'[0-9]', '1', string)
        return string

    @staticmethod
    def split_tokens(string):
        tokens = text_list(string)
        tokens = [token.strip('?.!, ') for token in tokens if token.strip('?.!, ')]
        tokens = [token for token in tokens if token]
        return tokens

    def get_tokens(self, string):
        string = self.preprocess_string(string)
        string = self.mask_digits(string)
        tokens = self.split_tokens(string)
        mask_tokens = self.mask_mark(tokens)

        return mask_tokens


class Classifier:
    def __init__(self, use_database=False, test=False):
        self._preprocessing = Preprocessing()
        self.my_queue = Queue()
        self._test = test
        if not test:
            if use_database:
                # загружаем c базы
                self._load_from_database()
            else:
                # загрузить с диска
                self._load_from_hdd()

        self._model_load = False
        self._model = None
        self.labels = None

    def _load_from_hdd(self):
        classifier_files = sorted(glob(cfg.app.directory.classifier_path_glob))
        if not classifier_files:
            raise FileNotFoundError(
                f'Отсутствует файлы с основной моделью (формата {cfg.app.directory.classifier_path_glob})')

        data = ''
        for file in classifier_files:
            with open(file) as f:
                data += f.read()
        self._model = dill.loads(codecs.decode(data.encode(), "base64"))

    def _load_from_database(self):
        t = threading.Thread(target=download_model,
                             args=("it.modelRevision == '{}'".format(cfg.app.main.model_name),
                                   self.my_queue,))
        t.start()

    def predict(self, line: str):
        if self._test:
            return "test"
        else:
            if self._model_load:
                return self._model.predict(dill.dumps([{'text': word} for word in self._preprocessing.get_tokens(line)]))[
                        0]
            else:
                try:
                    # получаем из очереди
                    # model = self.my_queue.get_nowait()
                    self._model = self.my_queue.get_nowait()
                    self.labels = self._model.labels
                    self._model_load = True
                    return self._model.predict(
                            dill.dumps([{'text': word} for word in self._preprocessing.get_tokens(line)]))[
                            0]
                except Exception as e:
                    print(e)
                    return "model not loaded yet"


if __name__ == '__main__':
    classifier = Classifier()

    for text in ['найди bmw', 'страховка авто', 'солярис', 'хочу купить авто в кредит', 'ипотека',
                 'хочу тачку подешевле', 'осаго', 'Skoda Octavia 2019 года в Москве']:
        print(text, classifier.predict(text))
