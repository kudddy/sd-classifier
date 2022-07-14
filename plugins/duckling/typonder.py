def replace_typos(text: str) -> str:

    text = text.replace("бэхо", "бэха")
    text = text.replace("митсубись", "митсубиси")
    text = text.replace("аккорд", "accord")
    text = text.replace("аудио", "audi")
    text = text.replace("икс 3", "x 3")
    text = text.replace("секс", "CX")
    return text


def prepare_data_tokenize_str(tokenized_elements_list: list) -> str:
    return " ".join([x["text"] for x in tokenized_elements_list])
