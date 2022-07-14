import re

import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def text_list(user_text: str) -> list:
    """
    Разбивает фразу клиента на слова в виде списка

    :param user_text: Фраза клиента
    :return: ['найти', 'мерс', 'в', 'екатеринбург', 'от', '2012', 'до', '2022', 'год']
    """

    result = []
    map_replace = {ord(','): '', ord('.'): ''}  # Убираем точки
    for word in user_text.translate(map_replace).split():
        result.append(morph.parse(word)[0].normal_form)  # Записываем в нормализованном виде
    return result
