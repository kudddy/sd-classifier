import codecs
from glob import glob
from queue import Queue

import dill


try:
    from ..config import cfg
    from ...plugins.db.query import insert_value_to_model
    from ...plugins.db.query import get_base64_model_from_base
    from ..helper import timing
except Exception as e:
    from plugins.config import cfg
    from plugins.db.query import insert_value_to_model
    from plugins.db.query import get_base64_model_from_base
    from plugins.helper import timing


def split_string(text: str, chunk_size: int) -> list:
    chunks = len(text)
    return [text[i:i + chunk_size] for i in range(0, chunks, chunk_size)]


def upload_model(model_uid: str):
    classifier_files = sorted(glob(cfg.app.directory.classifier_path_glob))
    if not classifier_files:
        raise FileNotFoundError(
            f'Отсутствует файлы с основной моделью (формата {cfg.app.directory.classifier_path_glob})')

    data = ''
    for file in classifier_files:
        with open(file) as f:
            data += f.read()
            for chunk_text in split_string(text=data, chunk_size=3998):
                insert_value_to_model(bin_text=chunk_text,
                                      model_revision=model_uid)


@timing
def download_model(model_revision: str, queue: Queue):
    end = True
    limit = 250
    offset = 0
    bin_file = ""
    counter = 0
    while end:
        data = get_base64_model_from_base(limit=limit, offset=offset, model_revision=model_revision)

        lst = data['searchModelData']['elems']
        if len(lst) > 0:
            for dct in lst:
                bin_file += dct['binText']
            offset += limit
            counter += 1
        else:
            end = False
    model = dill.loads(codecs.decode(bin_file.encode(), "base64"))
    queue.put(model)


# ### тест
# import threading
#
#
# def download_model_fast(model_revision: str) -> str:
#     counter = 0
#     limit = 250
#     offset = 0
#     bin_file = ""
#     for off in range(5):
#         t = threading.Thread(target=get_base64_model_from_base, args=(limit, offset, model_revision,))
#         t.start()
#
#         offset += limit
#
#     res = [my_queue.get() for x in range(5)]
#
#     for data in res:
#         lst = data['searchModelData']['elems']
#         if len(lst) > 0:
#             for dct in lst:
#                 bin_file += dct['binText']
#             offset += limit
#             counter += 1
#     print(bin_file)
#     return bin_file


# def job(start_position: int, limit: int):
#     n_iter = number_of_string / limit


