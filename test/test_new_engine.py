import unittest

from plugins.config import cfg
from plugins.inputer import inputter


class NewEngineTest(unittest.TestCase):
    use_new_search_engine = True

    def test_tesla_year(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "tesla",
                        "raw_text": "tesla",
                        "lemma": "tesla",
                        "original_text": "tesla",
                        "is_stop_word": False,
                        "grammem_info": {},
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "2021",
                        "raw_text": "2021",
                        "lemma": "2021",
                        "original_text": "две тысячи двадцать первого",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2021,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2021,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2021
                        },
                        "head": 2
                    },
                    {
                        "text": "года",
                        "raw_text": "года",
                        "lemma": "год",
                        "original_text": "года",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "is_beginning_of_composite": False,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2021
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 82)

        year_to = res['PAYLOAD']['result']['search_keys']['year_to']

        self.assertEqual(year_to, 2021)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2021)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Tesla 2021 года")

    def test_pizhik_2008_year_from(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "найди",
                        "raw_text": "найди",
                        "lemma": "найти",
                        "original_text": "Найди",
                        "is_stop_word": False,
                        "grammem_info": {
                            "number": "sing",
                            "raw_gram_info": "number=sing",
                            "part_of_speech": "VERB"
                        },
                        "head": 0
                    },
                    {
                        "text": "пыжик",
                        "raw_text": "пыжик",
                        "lemma": "пыжик",
                        "original_text": "Пыжик",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "anim",
                            "case": "nomn",
                            "gender": "femn",
                            "number": "sing",
                            "raw_gram_info": "animacy=anim|case=nomn|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "2008",
                        "raw_text": "2008",
                        "lemma": "2008",
                        "original_text": "две тысячи восьмого",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2008,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2021,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2008
                        },
                        "head": 2
                    },
                    {
                        "text": "с",
                        "raw_text": "с",
                        "lemma": "с",
                        "original_text": "с",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "2008",
                        "raw_text": "2008",
                        "lemma": "2008",
                        "original_text": "две тысячи восемь",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2008,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2008,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "NUM_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2008
                        },
                        "head": 2
                    },
                    {
                        "text": "года",
                        "raw_text": "года",
                        "lemma": "год",
                        "original_text": "года",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "is_beginning_of_composite": False,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2021
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 199)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 2343)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2008)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Peugeot 2008 от 2008 года")

    def test_pizhik_2008_year_from_price_from(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "найди",
                        "raw_text": "найди",
                        "lemma": "найти",
                        "original_text": "Найди",
                        "is_stop_word": False,
                        "grammem_info": {
                            "number": "sing",
                            "raw_gram_info": "number=sing",
                            "part_of_speech": "VERB"
                        },
                        "head": 0
                    },
                    {
                        "text": "пыжик",
                        "raw_text": "пыжик",
                        "lemma": "пыжик",
                        "original_text": "Пыжик",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "anim",
                            "case": "nomn",
                            "gender": "femn",
                            "number": "sing",
                            "raw_gram_info": "animacy=anim|case=nomn|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "2008",
                        "raw_text": "2008",
                        "lemma": "2008",
                        "original_text": "две тысячи восьмого",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2008,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2021,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2008
                        },
                        "head": 2
                    },
                    {
                        "text": "с",
                        "raw_text": "с",
                        "lemma": "с",
                        "original_text": "с",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "2008",
                        "raw_text": "2008",
                        "lemma": "2008",
                        "original_text": "две тысячи восемь",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2008,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2008,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "NUM_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2008
                        },
                        "head": 2
                    },
                    {
                        "text": "года",
                        "raw_text": "года",
                        "lemma": "год",
                        "original_text": "года",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "is_beginning_of_composite": False,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2021
                        },
                        "head": 0
                    },
                    {
                        "text": "от",
                        "raw_text": "от",
                        "lemma": "от",
                        "original_text": "от",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "300000",
                        "raw_text": "300000",
                        "lemma": "300000",
                        "original_text": "триста тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 300000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2021,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "text": "₽",
                        "raw_text": "₽",
                        "lemma": "₽",
                        "original_text": "₽",
                        "is_stop_word": False,
                        "grammem_info": {},
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 199)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 2343)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2008)

        price_from = res['PAYLOAD']['result']['search_keys']['price_from']

        self.assertEqual(price_from, 300000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Peugeot 2008 от 2008 года от 300000 ₽")

    def test_lada_kalina_year_from_year_to(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "найди",
                        "raw_text": "найди",
                        "lemma": "найти",
                        "original_text": "Найди",
                        "is_stop_word": False,
                        "grammem_info": {
                            "number": "sing",
                            "raw_gram_info": "number=sing",
                            "part_of_speech": "VERB"
                        },
                        "head": 0
                    },
                    {
                        "text": "лада",
                        "raw_text": "лада",
                        "lemma": "лада",
                        "original_text": "лада",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "anim",
                            "case": "nomn",
                            "gender": "femn",
                            "number": "sing",
                            "raw_gram_info": "animacy=anim|case=nomn|gender=femn|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "калина",
                        "raw_text": "калина",
                        "lemma": "калин",
                        "original_text": "калина",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gent",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=gent|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "2008",
                        "raw_text": "2008",
                        "lemma": "2008",
                        "original_text": "две тысячи восьмого",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2008,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2021,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2008
                        },
                        "head": 2
                    },
                    {
                        "text": "года",
                        "raw_text": "года",
                        "lemma": "год",
                        "original_text": "года",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "is_beginning_of_composite": False,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2021
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 232)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 2818)

        year_to = res['PAYLOAD']['result']['search_keys']['year_to']

        self.assertEqual(year_to, 2008)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2008)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "ВАЗ Kalina 2008 года")

    def test_lada_kalina_more_year_to_less_year_from(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "лада",
                        "raw_text": "лада",
                        "lemma": "лада",
                        "original_text": "лада",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "anim",
                            "case": "nomn",
                            "gender": "femn",
                            "number": "sing",
                            "raw_gram_info": "animacy=anim|case=nomn|gender=femn|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "калина",
                        "raw_text": "калина",
                        "lemma": "калин",
                        "original_text": "калина",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gent",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=gent|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "от",
                        "raw_text": "от",
                        "lemma": "от",
                        "original_text": "от",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "2008",
                        "raw_text": "2008",
                        "lemma": "2008",
                        "original_text": "две тысячи восьмого",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2008,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2021,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2008
                        },
                        "head": 2
                    },
                    {
                        "text": "до",
                        "raw_text": "до",
                        "lemma": "до",
                        "original_text": "до",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "2013",
                        "raw_text": "2013",
                        "lemma": "2013",
                        "original_text": "две тысячи восьмого",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2013,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2013,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2013
                        },
                        "head": 2
                    },
                    {
                        "text": "года",
                        "raw_text": "года",
                        "lemma": "год",
                        "original_text": "года",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "is_beginning_of_composite": False,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2021
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 232)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 2818)

        year_to = res['PAYLOAD']['result']['search_keys']['year_to']

        self.assertEqual(year_to, 2013)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2008)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "ВАЗ Kalina от 2008 до 2013 года")

    def test_mers_za_200k_rub(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "мерс",
                        "raw_text": "мерс",
                        "lemma": "мерс",
                        "original_text": "мерс",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "от",
                        "raw_text": "от",
                        "lemma": "от",
                        "original_text": "от",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "200000",
                        "raw_text": "200000",
                        "lemma": "200000",
                        "original_text": "двести тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 200000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 200000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "text": "₽",
                        "raw_text": "₽",
                        "lemma": "₽",
                        "original_text": "₽",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']
        self.assertEqual(brand_id, 192)

        year_to = res['PAYLOAD']['result']['search_keys']['price_from']
        self.assertEqual(year_to, 200000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']
        self.assertEqual(search_text_form, "Mercedes Benz от 200000 ₽")

    def test_mers_do_900k_s2005_po_2021(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "мерс",
                        "raw_text": "мерс",
                        "lemma": "мерс",
                        "original_text": "мерс",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "до",
                        "raw_text": "до",
                        "lemma": "до",
                        "original_text": "до",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "head": 0
                    },
                    {
                        "text": "900000",
                        "raw_text": "900000",
                        "lemma": "900000",
                        "original_text": "девятьсот тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 900000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 900000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "text": "с",
                        "raw_text": "с",
                        "lemma": "с",
                        "original_text": "с",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "head": 0
                    },
                    {
                        "text": "2005",
                        "raw_text": "2005",
                        "lemma": "2005",
                        "original_text": "две тысячи пятого",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2005,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2005,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2005
                        },
                        "head": 2
                    },
                    {
                        "text": "по",
                        "raw_text": "по",
                        "lemma": "по",
                        "original_text": "по",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "head": 0
                    },
                    {
                        "text": "2021",
                        "raw_text": "2021",
                        "lemma": "2021",
                        "original_text": "две тысячи двадцать один",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2021,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2021,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2021
                        },
                        "head": 2
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 192)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2005)

        year_to = res['PAYLOAD']['result']['search_keys']['year_to']

        self.assertEqual(year_to, 2021)

        price_from = res['PAYLOAD']['result']['search_keys']['price_to']

        self.assertEqual(price_from, 900000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Mercedes Benz от 2005 до 2021 года до 900000 ₽")

    def test_mers_ot_200k(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "найди",
                        "raw_text": "найди",
                        "lemma": "найти",
                        "original_text": "Найди",
                        "is_stop_word": False,
                        "grammem_info": {
                            "number": "sing",
                            "raw_gram_info": "number=sing",
                            "part_of_speech": "VERB"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 0
                    },
                    {
                        "text": "мерс",
                        "raw_text": "мерс",
                        "lemma": "мерс",
                        "original_text": "мерс",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "от",
                        "raw_text": "от",
                        "lemma": "от",
                        "original_text": "от",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "200000",
                        "raw_text": "200000",
                        "lemma": "200000",
                        "original_text": "двести тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 200000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 200000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 192)

        price_from = res['PAYLOAD']['result']['search_keys']['price_from']

        self.assertEqual(price_from, 200000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Mercedes Benz от 200000 ₽")

    def test_mers_ot_year_from_do_200k(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "мерс",
                        "raw_text": "мерс",
                        "lemma": "мерс",
                        "original_text": "мерс",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "от",
                        "raw_text": "от",
                        "lemma": "от",
                        "original_text": "от",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "200000",
                        "raw_text": "200000",
                        "lemma": "200000",
                        "original_text": "двести тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 200000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 200000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "text": "от",
                        "raw_text": "от",
                        "lemma": "от",
                        "original_text": "от",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "2008",
                        "raw_text": "2008",
                        "lemma": "2008",
                        "original_text": "две тысячи двадцать",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2008,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2008,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2008
                        },
                        "head": 2
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 192)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2008)

        price_from = res['PAYLOAD']['result']['search_keys']['price_from']

        self.assertEqual(price_from, 200000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Mercedes Benz от 2008 года от 200000 ₽")

    def test_mers_v_kalchenske_ot_200k_false(self):
        # ТУТ ОШИБКА С ЦЕНОЙ
        # Находит вместо цены год
        # Не находит Калачинск и валится на этом
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "мерс",
                        "raw_text": "мерс",
                        "lemma": "мерс",
                        "original_text": "мерс",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "в",
                        "raw_text": "в",
                        "lemma": "в",
                        "original_text": "в",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "калачинске",
                        "raw_text": "калачинске",
                        "lemma": "калачинск",
                        "original_text": "Калачинске",
                        "is_stop_word": False,
                        "grammem_info": {
                            "number": "sing",
                            "raw_gram_info": "number=sing",
                            "part_of_speech": "VERB"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 0
                    },
                    {
                        "text": "от",
                        "raw_text": "от",
                        "lemma": "от",
                        "original_text": "от",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "200000",
                        "raw_text": "200000",
                        "lemma": "200000",
                        "original_text": "двести тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 200000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 200000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], False)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Mercedes Benz Калачинск")

    def test_mers_2000_year_from_year_ot_200k(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "мерс",
                        "raw_text": "мерс",
                        "lemma": "мерс",
                        "original_text": "мерс",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "2008",
                        "raw_text": "2008",
                        "lemma": "2008",
                        "original_text": "две тысячи восьмого",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2008,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2021,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2008
                        },
                        "head": 2
                    },
                    {
                        "text": "года",
                        "raw_text": "года",
                        "lemma": "год",
                        "original_text": "года",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "is_beginning_of_composite": False,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2021
                        },
                        "head": 0
                    },
                    {
                        "text": "от",
                        "raw_text": "от",
                        "lemma": "от",
                        "original_text": "от",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "200000",
                        "raw_text": "200000",
                        "lemma": "200000",
                        "original_text": "двести тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 200000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 200000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 192)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2008)

        price_from = res['PAYLOAD']['result']['search_keys']['price_from']

        self.assertEqual(price_from, 200000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Mercedes Benz от 2008 года от 200000 ₽")

    def test_mers_2000_year_from_year_do_600k(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "мерс",
                        "raw_text": "мерс",
                        "lemma": "мерс",
                        "original_text": "мерс",
                        "is_stop_word": True,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "2008",
                        "raw_text": "2008",
                        "lemma": "2008",
                        "original_text": "две тысячи восьмого",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 2008,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 2008,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "composite_token_type": "TIME_DATE_TOKEN",
                        "composite_token_length": 2,
                        "composite_token_value": {
                            "year": 2008
                        },
                        "head": 2
                    },
                    {
                        "text": "года",
                        "raw_text": "года",
                        "lemma": "год",
                        "original_text": "года",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "is_beginning_of_composite": False,
                        "head": 0
                    },
                    {
                        "text": "до",
                        "raw_text": "до",
                        "lemma": "до",
                        "original_text": "до",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "600000",
                        "raw_text": "600000",
                        "lemma": "600000",
                        "original_text": "шестьсот тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 600000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 600000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 192)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2008)

        price_from = res['PAYLOAD']['result']['search_keys']['price_to']

        self.assertEqual(price_from, 600000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Mercedes Benz от 2008 года до 600000 ₽")

    def test_toyota_rostov_na_donu(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "Toyota",
                        "raw_text": "Toyota",
                        "lemma": "Toyota",
                        "original_text": "Toyota",
                        "is_stop_word": False,
                        "grammem_info": {},
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "Ростов на Дону",
                        "raw_text": "Ростов на Дону",
                        "lemma": "Ростов на Дону",
                        "original_text": "Ростов на Дону",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=nomn|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 196)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [2])

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Toyota Ростов-на-Дону")

    def test_toyota_omsk(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "Toyota",
                        "raw_text": "Toyota",
                        "lemma": "Toyota",
                        "original_text": "Toyota",
                        "is_stop_word": False,
                        "grammem_info": {},
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "Омск",
                        "raw_text": "Омск",
                        "lemma": "Омск",
                        "original_text": "Омск",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=nomn|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 196)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [10])

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Toyota Омск")

    def test_toyota_spb_nino(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "Toyota",
                        "raw_text": "Toyota",
                        "lemma": "Toyota",
                        "original_text": "Toyota",
                        "is_stop_word": False,
                        "grammem_info": {},
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "СПБ",
                        "raw_text": "СПБ",
                        "lemma": "СПБ",
                        "original_text": "СПБ",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=nomn|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "head": 0
                    },
                    {
                        "text": "НиНо",
                        "raw_text": "НиНо",
                        "lemma": "НиНо",
                        "original_text": "НиНо",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=nomn|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 196)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [18, 23])

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Toyota  Санкт-Петербург, Нижний Новгород")

    def test_citroen_cobalt(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "Ситроен",
                        "raw_text": "Ситроен",
                        "lemma": "Ситроен",
                        "original_text": "Ситроен",
                        "is_stop_word": False,
                        "grammem_info": {},
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "Кобальт",
                        "raw_text": "Кобальт",
                        "lemma": "Кобальт",
                        "original_text": "Кобальт",
                        "is_stop_word": False,
                        "grammem_info": {},
                        "list_of_dependents": [],
                        "dependency_type": "case",
                        "head": 1
                    },
                    {
                        "text": "СПБ",
                        "raw_text": "СПБ",
                        "lemma": "СПБ",
                        "original_text": "СПБ",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "sing",
                            "raw_gram_info": "animacy=inan|case=nomn|gender=masc|number=sing",
                            "part_of_speech": "NOUN"
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test)
        self.assertEqual(res['STATUS'], True)

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 212)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [18])

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Citroen Санкт-Петербург")

    def test_auto_more_500k_rub(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "авто",
                        "raw_text": "авто",
                        "lemma": "авто",
                        "original_text": "авто",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "больше",
                        "raw_text": "больше",
                        "lemma": "больше",
                        "original_text": "больше",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "500 000",
                        "raw_text": "500 000",
                        "lemma": "500 000",
                        "original_text": "пятьсот тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 500000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 500000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "text": "рублей",
                        "raw_text": "рублей",
                        "lemma": "рублей",
                        "original_text": "рублей",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        price_from = res['PAYLOAD']['result']['search_keys']['price_from']
        self.assertEqual(price_from, 500000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']
        self.assertEqual(search_text_form, "от 500000 ₽")

    def test_auto_less_750k_rub(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "автомобили",
                        "raw_text": "автомобили",
                        "lemma": "автомобили",
                        "original_text": "автомобили",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "меньше",
                        "raw_text": "меньше",
                        "lemma": "меньше",
                        "original_text": "меньше",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "750000",
                        "raw_text": "750000",
                        "lemma": "750000",
                        "original_text": "Семьсот пятьдесят тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 750000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 750000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "text": "рублей",
                        "raw_text": "рублей",
                        "lemma": "рублей",
                        "original_text": "рублей",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        price_to = res['PAYLOAD']['result']['search_keys']['price_to']
        self.assertEqual(price_to, 750000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']
        self.assertEqual(search_text_form, "до 750000 ₽")

    def test_auto_more_345k_less_785k_rub(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "авто",
                        "raw_text": "авто",
                        "lemma": "авто",
                        "original_text": "авто",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "больше",
                        "raw_text": "больше",
                        "lemma": "больше",
                        "original_text": "больше",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "345000",
                        "raw_text": "345000",
                        "lemma": "345000",
                        "original_text": "Трехсот сорока пяти тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 345000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 345000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "text": "и",
                        "raw_text": "и",
                        "lemma": "и",
                        "original_text": "и",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "меньше",
                        "raw_text": "меньше",
                        "lemma": "меньше",
                        "original_text": "меньше",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "785000",
                        "raw_text": "785000",
                        "lemma": "785000",
                        "original_text": "Семьсот восемьдесят пять тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 785000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 785000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "text": "рублей",
                        "raw_text": "рублей",
                        "lemma": "рублей",
                        "original_text": "рублей",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        price_from = res['PAYLOAD']['result']['search_keys']['price_from']
        self.assertEqual(price_from, 345000)

        price_to = res['PAYLOAD']['result']['search_keys']['price_to']
        self.assertEqual(price_to, 785000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']
        self.assertEqual(search_text_form, "от 345000 до 785000 ₽")

    def test_auto_s_more_345k_no_less_785k_rub(self):
        test = {
            "data": {
                "new_search_engine": True,
                "text": [
                    {
                        "text": "автомобиль",
                        "raw_text": "автомобиль",
                        "lemma": "автомобиль",
                        "original_text": "автомобиль",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "стоимостью",
                        "raw_text": "стоимостью",
                        "lemma": "стоимостью",
                        "original_text": "стоимостью",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "больше",
                        "raw_text": "больше",
                        "lemma": "больше",
                        "original_text": "больше",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "345000",
                        "raw_text": "345000",
                        "lemma": "345000",
                        "original_text": "Трехсот сорока пяти тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 345000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 345000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "text": "но",
                        "raw_text": "но",
                        "lemma": "но",
                        "original_text": "но",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "меньше",
                        "raw_text": "меньше",
                        "lemma": "меньше",
                        "original_text": "меньше",
                        "is_stop_word": False,
                        "grammem_info": {
                            "part_of_speech": "PREP"
                        },
                        "list_of_dependents": [
                            1,
                            2
                        ],
                        "dependency_type": "root",
                        "head": 0
                    },
                    {
                        "text": "785000",
                        "raw_text": "785000",
                        "lemma": "785000",
                        "original_text": "Семьсот восемьдесят пять тысяч",
                        "token_type": "NUM_TOKEN",
                        "is_stop_word": False,
                        "token_value": {
                            "value": 785000,
                            "adjectival_number": False
                        },
                        "grammem_info": {
                            "numform": "digit",
                            "raw_gram_info": "numform=digit",
                            "part_of_speech": "NUM"
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "NUM_TOKEN",
                                "token_value": {
                                    "value": 785000,
                                    "adjectival_number": True
                                }
                            }
                        ],
                        "list_of_dependents": [],
                        "dependency_type": "nummod",
                        "is_beginning_of_composite": True,
                        "head": 2
                    },
                    {
                        "text": "рублей",
                        "raw_text": "рублей",
                        "lemma": "рублей",
                        "original_text": "рублей",
                        "is_stop_word": False,
                        "grammem_info": {
                            "animacy": "inan",
                            "case": "gen",
                            "gender": "masc",
                            "number": "plur",
                            "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=plur",
                            "part_of_speech": "NOUN"
                        },
                        "head": 0
                    },
                    {
                        "raw_text": ".",
                        "text": ".",
                        "lemma": ".",
                        "token_type": "SENTENCE_ENDPOINT_TOKEN",
                        "token_value": {
                            "value": "."
                        },
                        "list_of_token_types_data": [
                            {
                                "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                "token_value": {
                                    "value": "."
                                }
                            }
                        ]
                    }
                ]
            }
        }

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        price_from = res['PAYLOAD']['result']['search_keys']['price_from']
        self.assertEqual(price_from, 345000)

        price_to = res['PAYLOAD']['result']['search_keys']['price_to']
        self.assertEqual(price_to, 785000)

        search_text_form = res['PAYLOAD']['result']['search_text_form']
        self.assertEqual(search_text_form, "от 345000 до 785000 ₽")
