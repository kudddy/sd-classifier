import unittest

from plugins.inputer import inputter


class OldEngineTest(unittest.TestCase):
    use_new_search_engine = False

    def test_success_resp_with_brand(self):
        test = {'MESSAGE_NAME': 'GET_DUCKLING_RESULT',
                'data': {'new_search_engine': self.use_new_search_engine, 'text': [
                    {'text': 'BMW', 'raw_text': 'BMW', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'X'},
                     'lemma': 'bmw', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'root',
                     'head': 0},
                    {'raw_text': '.', 'text': '.', 'lemma': '.', 'token_type': 'SENTENCE_ENDPOINT_TOKEN',
                     'token_value': {'value': '.'},
                     'list_of_token_types_data': [
                         {'token_type': 'SENTENCE_ENDPOINT_TOKEN', 'token_value': {'value': '.'}}]}]}}

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

    def test_success_resp_brand_model(self):
        test = {'MESSAGE_NAME': 'GET_DUCKLING_RESULT', 'data': {'new_search_engine': self.use_new_search_engine, 'text': [
            {'text': 'bmw', 'raw_text': 'bmw', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'X'},
             'lemma': 'bmw', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'nsubj',
             'head': 2},
            {'text': '3', 'raw_text': '3', 'lemma': '3', 'original_text': '3', 'token_type': 'NUM_TOKEN',
             'token_value': {'value': 3, 'adjectival_number': False}, 'list_of_token_types_data': [
                {'token_type': 'NUM_TOKEN', 'token_value': {'value': 3, 'adjectival_number': False}}],
             'grammem_info': {'numform': 'digit', 'raw_gram_info': 'numform=digit', 'part_of_speech': 'NUM'},
             'is_stop_word': False, 'list_of_dependents': [1], 'dependency_type': 'root', 'head': 0},
            {'raw_text': '.', 'text': '.', 'lemma': '.', 'token_type': 'SENTENCE_ENDPOINT_TOKEN',
             'token_value': {'value': '.'},
             'list_of_token_types_data': [
                 {'token_type': 'SENTENCE_ENDPOINT_TOKEN', 'token_value': {'value': '.'}}]}]}}

        res = inputter(test, self.use_new_search_engine)
        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW 3ER")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 591)

    def test_success_resp_brand_model_city(self):
        test = {'MESSAGE_NAME': 'GET_DUCKLING_RESULT', 'data': {'new_search_engine': self.use_new_search_engine, 'text': [
            {'text': 'bmw', 'raw_text': 'bmw', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'X'},
             'lemma': 'bmw', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'nsubj',
             'head': 2},
            {'text': '3', 'raw_text': '3', 'lemma': '3', 'original_text': '3', 'token_type': 'NUM_TOKEN',
             'token_value': {'value': 3, 'adjectival_number': False}, 'list_of_token_types_data': [
                {'token_type': 'NUM_TOKEN', 'token_value': {'value': 3, 'adjectival_number': False}}],
             'grammem_info': {'numform': 'digit', 'raw_gram_info': 'numform=digit', 'part_of_speech': 'NUM'},
             'is_stop_word': False, 'list_of_dependents': [1, 4], 'dependency_type': 'root', 'head': 0},
            {'text': 'в', 'raw_text': 'в', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'ADP'},
             'lemma': 'в',
             'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'case', 'head': 4},
            {'text': 'Москве', 'raw_text': 'Москве',
             'grammem_info': {'animacy': 'inan', 'case': 'loc', 'gender': 'fem', 'number': 'sing',
                              'raw_gram_info': 'animacy=inan|case=loc|gender=fem|number=sing',
                              'part_of_speech': 'NOUN'}, 'lemma': 'москва', 'is_stop_word': False,
             'list_of_dependents': [3], 'dependency_type': 'obl', 'head': 2, 'composite_token_type': 'GEO_TOKEN',
             'composite_token_length': 1, 'is_beginning_of_composite': True,
             'composite_token_value': {'value': 'Москва', 'locality_type': 'CITY', 'latitude': 55.75222,
                                       'longitude': 37.61556, 'capital': None,
                                       'locative_value': {'CITY': 'в Москве'},
                                       'timezone': [[None, 3]], 'currency': ['RUB', 'российский рубль'],
                                       'country': 'Россия', 'country_hidden': False}},
            {'raw_text': '.', 'text': '.', 'lemma': '.', 'token_type': 'SENTENCE_ENDPOINT_TOKEN',
             'token_value': {'value': '.'},
             'list_of_token_types_data': [
                 {'token_type': 'SENTENCE_ENDPOINT_TOKEN', 'token_value': {'value': '.'}}]}]}}

        res = inputter(test, self.use_new_search_engine)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW 3ER Москва")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 591)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [1])

    def test_success_resp_brand_model_city_year_from(self):

        test = {'MESSAGE_NAME': 'GET_DUCKLING_RESULT', 'data': {'new_search_engine': self.use_new_search_engine, 'text': [
            {'text': 'bmw', 'raw_text': 'bmw', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'X'},
             'lemma': 'bmw', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'nsubj',
             'head': 2},
            {'text': '3', 'raw_text': '3', 'lemma': '3', 'original_text': '3', 'token_type': 'NUM_TOKEN',
             'token_value': {'value': 3, 'adjectival_number': False}, 'list_of_token_types_data': [
                {'token_type': 'NUM_TOKEN', 'token_value': {'value': 3, 'adjectival_number': False}}],
             'grammem_info': {'numform': 'digit', 'raw_gram_info': 'numform=digit', 'part_of_speech': 'NUM'},
             'is_stop_word': False, 'list_of_dependents': [1, 4, 7], 'dependency_type': 'root', 'head': 0},
            {'text': 'в', 'raw_text': 'в', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'ADP'},
             'lemma': 'в',
             'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'case', 'head': 4},
            {'text': 'Москве', 'raw_text': 'Москве',
             'grammem_info': {'animacy': 'inan', 'case': 'loc', 'gender': 'fem', 'number': 'sing',
                              'raw_gram_info': 'animacy=inan|case=loc|gender=fem|number=sing',
                              'part_of_speech': 'NOUN'}, 'lemma': 'москва', 'is_stop_word': False,
             'list_of_dependents': [3], 'dependency_type': 'nmod', 'head': 2, 'composite_token_type': 'GEO_TOKEN',
             'composite_token_length': 1, 'is_beginning_of_composite': True,
             'composite_token_value': {'value': 'Москва', 'locality_type': 'CITY', 'latitude': 55.75222,
                                       'longitude': 37.61556, 'capital': None,
                                       'locative_value': {'CITY': 'в Москве'},
                                       'timezone': [[None, 3]], 'currency': ['RUB', 'российский рубль'],
                                       'country': 'Россия', 'country_hidden': False}},
            {'text': 'от', 'raw_text': 'от', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'ADP'},
             'lemma': 'от', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'case', 'head': 7},
            {'text': '2015', 'raw_text': '2015', 'lemma': '2015', 'original_text': '2015',
             'token_type': 'NUM_TOKEN',
             'token_value': {'value': 2015, 'adjectival_number': False}, 'list_of_token_types_data': [
                {'token_type': 'NUM_TOKEN', 'token_value': {'value': 2015, 'adjectival_number': False}}],
             'grammem_info': {'numform': 'digit', 'raw_gram_info': 'numform=digit', 'part_of_speech': 'NUM'},
             'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'nummod', 'head': 7,
             'is_beginning_of_composite': True, 'composite_token_type': 'TIME_DATE_TOKEN',
             'composite_token_length': 2,
             'composite_token_value': {'year': 2015}}, {'text': 'года', 'raw_text': 'года',
                                                        'grammem_info': {'animacy': 'inan', 'case': 'gen',
                                                                         'gender': 'masc', 'number': 'sing',
                                                                         'raw_gram_info': 'animacy=inan|case=gen|gender=masc|number=sing',
                                                                         'part_of_speech': 'NOUN'}, 'lemma': 'год',
                                                        'is_stop_word': False, 'list_of_dependents': [5, 6],
                                                        'dependency_type': 'obl', 'head': 2,
                                                        'is_beginning_of_composite': False,
                                                        'composite_token_type': 'TIME_DATE_TOKEN',
                                                        'composite_token_length': 2,
                                                        'composite_token_value': {'year': 2015}},
            {'raw_text': '.', 'text': '.', 'lemma': '.', 'token_type': 'SENTENCE_ENDPOINT_TOKEN',
             'token_value': {'value': '.'},
             'list_of_token_types_data': [
                 {'token_type': 'SENTENCE_ENDPOINT_TOKEN', 'token_value': {'value': '.'}}]}]}}

        res = inputter(test, self.use_new_search_engine)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW 3ER Москва от 2015 года")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 591)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [1])

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2015)

    def test_success_resp_brand_model_city_year_to(self):
        test = {'MESSAGE_NAME': 'GET_DUCKLING_RESULT', 'data': {'new_search_engine': self.use_new_search_engine, 'text': [
            {'text': 'BMW', 'raw_text': 'BMW', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'X'},
             'lemma': 'bmw', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'nsubj',
             'head': 2},
            {'text': '3', 'raw_text': '3', 'lemma': '3', 'original_text': '3', 'token_type': 'NUM_TOKEN',
             'token_value': {'value': 3, 'adjectival_number': False}, 'list_of_token_types_data': [
                {'token_type': 'NUM_TOKEN', 'token_value': {'value': 3, 'adjectival_number': False}}],
             'grammem_info': {'numform': 'digit', 'raw_gram_info': 'numform=digit', 'part_of_speech': 'NUM'},
             'is_stop_word': False, 'list_of_dependents': [1, 4, 6], 'dependency_type': 'root', 'head': 0},
            {'text': 'в', 'raw_text': 'в', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'ADP'},
             'lemma': 'в',
             'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'case', 'head': 4},
            {'text': 'Москве', 'raw_text': 'Москве',
             'grammem_info': {'animacy': 'inan', 'case': 'loc', 'gender': 'fem', 'number': 'sing',
                              'raw_gram_info': 'animacy=inan|case=loc|gender=fem|number=sing',
                              'part_of_speech': 'NOUN'}, 'lemma': 'москва', 'is_stop_word': False,
             'list_of_dependents': [3], 'dependency_type': 'nmod', 'head': 2, 'composite_token_type': 'GEO_TOKEN',
             'composite_token_length': 1, 'is_beginning_of_composite': True,
             'composite_token_value': {'value': 'Москва', 'locality_type': 'CITY', 'latitude': 55.75222,
                                       'longitude': 37.61556, 'capital': None,
                                       'locative_value': {'CITY': 'в Москве'},
                                       'timezone': [[None, 3]], 'currency': ['RUB', 'российский рубль'],
                                       'country': 'Россия', 'country_hidden': False}},
            {'text': 'до', 'raw_text': 'до', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'ADP'},
             'lemma': 'до', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'case', 'head': 6},
            {'text': '2015', 'raw_text': '2015', 'lemma': '2015', 'original_text': '2015',
             'token_type': 'NUM_TOKEN',
             'token_value': {'value': 2015, 'adjectival_number': False}, 'list_of_token_types_data': [
                {'token_type': 'NUM_TOKEN', 'token_value': {'value': 2015, 'adjectival_number': False}}],
             'grammem_info': {'numform': 'digit', 'raw_gram_info': 'numform=digit', 'part_of_speech': 'NUM'},
             'is_stop_word': False, 'list_of_dependents': [5], 'dependency_type': 'nummod:gov', 'head': 2},
            {'raw_text': '.', 'text': '.', 'lemma': '.', 'token_type': 'SENTENCE_ENDPOINT_TOKEN',
             'token_value': {'value': '.'},
             'list_of_token_types_data': [
                 {'token_type': 'SENTENCE_ENDPOINT_TOKEN', 'token_value': {'value': '.'}}]}]}}

        res = inputter(test, self.use_new_search_engine)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW 3ER Москва до 2015 года")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 591)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [1])

        year_to = res['PAYLOAD']['result']['search_keys']['year_to']

        self.assertEqual(year_to, 2015)

    def test_success_resp_brand_model_city_year_from_to(self):

        test = {'MESSAGE_NAME': 'GET_DUCKLING_RESULT', 'data': {'new_search_engine': self.use_new_search_engine, 'text': [
            {'text': 'bmw', 'raw_text': 'bmw', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'X'},
             'lemma': 'bmw', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'nsubj',
             'head': 2},
            {'text': '3', 'raw_text': '3', 'lemma': '3', 'original_text': '3', 'token_type': 'NUM_TOKEN',
             'token_value': {'value': 3, 'adjectival_number': False}, 'list_of_token_types_data': [
                {'token_type': 'NUM_TOKEN', 'token_value': {'value': 3, 'adjectival_number': False}}],
             'grammem_info': {'numform': 'digit', 'raw_gram_info': 'numform=digit', 'part_of_speech': 'NUM'},
             'is_stop_word': False, 'list_of_dependents': [1, 4, 9], 'dependency_type': 'root', 'head': 0},
            {'text': 'в', 'raw_text': 'в', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'ADP'},
             'lemma': 'в',
             'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'case', 'head': 4},
            {'text': 'Москве', 'raw_text': 'Москве',
             'grammem_info': {'animacy': 'inan', 'case': 'loc', 'gender': 'fem', 'number': 'sing',
                              'raw_gram_info': 'animacy=inan|case=loc|gender=fem|number=sing',
                              'part_of_speech': 'NOUN'}, 'lemma': 'москва', 'is_stop_word': False,
             'list_of_dependents': [3], 'dependency_type': 'nmod', 'head': 2, 'composite_token_type': 'GEO_TOKEN',
             'composite_token_length': 1, 'is_beginning_of_composite': True,
             'composite_token_value': {'value': 'Москва', 'locality_type': 'CITY', 'latitude': 55.75222,
                                       'longitude': 37.61556, 'capital': None,
                                       'locative_value': {'CITY': 'в Москве'},
                                       'timezone': [[None, 3]], 'currency': ['RUB', 'российский рубль'],
                                       'country': 'Россия', 'country_hidden': False}},
            {'text': 'от', 'raw_text': 'от', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'ADP'},
             'lemma': 'от', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'case', 'head': 7},
            {'text': '2015', 'raw_text': '2015', 'lemma': '2015', 'original_text': '2015',
             'token_type': 'NUM_TOKEN',
             'token_value': {'value': 2015, 'adjectival_number': False}, 'list_of_token_types_data': [
                {'token_type': 'NUM_TOKEN', 'token_value': {'value': 2015, 'adjectival_number': False}}],
             'grammem_info': {'numform': 'digit', 'raw_gram_info': 'numform=digit', 'part_of_speech': 'NUM'},
             'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'nummod', 'head': 7,
             'is_beginning_of_composite': True, 'composite_token_type': 'TIME_DATE_TOKEN',
             'composite_token_length': 2,
             'composite_token_value': {'year': 2015}}, {'text': 'года', 'raw_text': 'года',
                                                        'grammem_info': {'animacy': 'inan', 'case': 'gen',
                                                                         'gender': 'masc', 'number': 'sing',
                                                                         'raw_gram_info': 'animacy=inan|case=gen|gender=masc|number=sing',
                                                                         'part_of_speech': 'NOUN'}, 'lemma': 'год',
                                                        'is_stop_word': False, 'list_of_dependents': [5, 6],
                                                        'dependency_type': 'obl', 'head': 9,
                                                        'is_beginning_of_composite': False,
                                                        'composite_token_type': 'TIME_DATE_TOKEN',
                                                        'composite_token_length': 2,
                                                        'composite_token_value': {'year': 2015}},
            {'text': 'до', 'raw_text': 'до', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'ADP'},
             'lemma': 'до', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'case', 'head': 9},
            {'text': '2020', 'raw_text': '2020', 'lemma': '2020', 'original_text': '2020',
             'token_type': 'NUM_TOKEN',
             'token_value': {'value': 2020, 'adjectival_number': False}, 'list_of_token_types_data': [
                {'token_type': 'NUM_TOKEN', 'token_value': {'value': 2020, 'adjectival_number': False}}],
             'grammem_info': {'numform': 'digit', 'raw_gram_info': 'numform=digit', 'part_of_speech': 'NUM'},
             'is_stop_word': False, 'list_of_dependents': [7, 8], 'dependency_type': 'nummod:gov', 'head': 2},
            {'raw_text': '.', 'text': '.', 'lemma': '.', 'token_type': 'SENTENCE_ENDPOINT_TOKEN',
             'token_value': {'value': '.'},
             'list_of_token_types_data': [
                 {'token_type': 'SENTENCE_ENDPOINT_TOKEN', 'token_value': {'value': '.'}}]}]}}

        res = inputter(test, self.use_new_search_engine)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "BMW 3ER Москва от 2015 до 2020 года")

        brand_id = res['PAYLOAD']['result']['search_keys']['brand_id']

        self.assertEqual(brand_id, 48)

        model_id = res['PAYLOAD']['result']['search_keys']['model_id']

        self.assertEqual(model_id, 591)

        city_id = res['PAYLOAD']['result']['search_keys']['city_id']

        self.assertEqual(city_id, [1])

        year_to = res['PAYLOAD']['result']['search_keys']['year_to']

        self.assertEqual(year_to, 2020)

        year_from = res['PAYLOAD']['result']['search_keys']['year_from']

        self.assertEqual(year_from, 2015)

    def test_success_resp_city(self):
        test = {'MESSAGE_NAME': 'GET_DUCKLING_RESULT',
                'data': {'new_search_engine': self.use_new_search_engine, 'text': [{'text': 'хочу', 'raw_text': 'хочу',
                                                                           'grammem_info': {'aspect': 'impf',
                                                                                            'mood': 'ind',
                                                                                            'number': 'sing',
                                                                                            'person': '1',
                                                                                            'tense': 'notpast',
                                                                                            'transitivity': 'tran',
                                                                                            'verbform': 'fin',
                                                                                            'voice': 'act',
                                                                                            'raw_gram_info': 'aspect=impf|mood=ind|number=sing|person=1|tense=notpast|transitivity=tran|verbform=fin|voice=act',
                                                                                            'part_of_speech': 'VERB'},
                                                                           'lemma': 'хотеть', 'is_stop_word': False,
                                                                           'list_of_dependents': [2],
                                                                           'dependency_type': 'root', 'head': 0},
                                                                          {'text': 'тачку', 'raw_text': 'тачку',
                                                                           'grammem_info': {'animacy': 'inan',
                                                                                            'case': 'acc',
                                                                                            'gender': 'fem',
                                                                                            'number': 'sing',
                                                                                            'raw_gram_info': 'animacy=inan|case=acc|gender=fem|number=sing',
                                                                                            'part_of_speech': 'NOUN'},
                                                                           'lemma': 'тачка', 'is_stop_word': False,
                                                                           'list_of_dependents': [4],
                                                                           'dependency_type': 'obl', 'head': 1},
                                                                          {'text': 'в', 'raw_text': 'в',
                                                                           'grammem_info': {'raw_gram_info': '',
                                                                                            'part_of_speech': 'ADP'},
                                                                           'lemma': 'в', 'is_stop_word': False,
                                                                           'list_of_dependents': [],
                                                                           'dependency_type': 'case', 'head': 4},
                                                                          {'text': 'Москве', 'raw_text': 'Москве',
                                                                           'grammem_info': {'animacy': 'inan',
                                                                                            'case': 'loc',
                                                                                            'gender': 'fem',
                                                                                            'number': 'sing',
                                                                                            'raw_gram_info': 'animacy=inan|case=loc|gender=fem|number=sing',
                                                                                            'part_of_speech': 'NOUN'},
                                                                           'lemma': 'москва', 'is_stop_word': False,
                                                                           'list_of_dependents': [3],
                                                                           'dependency_type': 'nmod', 'head': 2,
                                                                           'composite_token_type': 'GEO_TOKEN',
                                                                           'composite_token_length': 1,
                                                                           'is_beginning_of_composite': True,
                                                                           'composite_token_value': {
                                                                               'value': 'Москва',
                                                                               'locality_type': 'CITY',
                                                                               'latitude': 55.75222,
                                                                               'longitude': 37.61556,
                                                                               'capital': None,
                                                                               'locative_value': {
                                                                                   'CITY': 'в Москве'},
                                                                               'timezone': [
                                                                                   [None, 3]],
                                                                               'currency': ['RUB',
                                                                                            'российский рубль'],
                                                                               'country': 'Россия',
                                                                               'country_hidden': False}},
                                                                          {'raw_text': '.', 'text': '.',
                                                                           'lemma': '.',
                                                                           'token_type': 'SENTENCE_ENDPOINT_TOKEN',
                                                                           'token_value': {'value': '.'},
                                                                           'list_of_token_types_data': [
                                                                               {
                                                                                   'token_type': 'SENTENCE_ENDPOINT_TOKEN',
                                                                                   'token_value': {
                                                                                       'value': '.'}}]}]}}

        res = inputter(test, self.use_new_search_engine)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "Москва")

    def test_success_resp_year_from(self):
        test = {'MESSAGE_NAME': 'GET_DUCKLING_RESULT',
                'data': {'new_search_engine': self.use_new_search_engine, 'text': [{'text': 'хочу', 'raw_text': 'хочу',
                                                                           'grammem_info': {'aspect': 'impf',
                                                                                            'mood': 'ind',
                                                                                            'number': 'sing',
                                                                                            'person': '1',
                                                                                            'tense': 'notpast',
                                                                                            'transitivity': 'tran',
                                                                                            'verbform': 'fin',
                                                                                            'voice': 'act',
                                                                                            'raw_gram_info': 'aspect=impf|mood=ind|number=sing|person=1|tense=notpast|transitivity=tran|verbform=fin|voice=act',
                                                                                            'part_of_speech': 'VERB'},
                                                                           'lemma': 'хотеть', 'is_stop_word': False,
                                                                           'list_of_dependents': [2],
                                                                           'dependency_type': 'root', 'head': 0},
                                                                          {'text': 'тачку', 'raw_text': 'тачку',
                                                                           'grammem_info': {'animacy': 'inan',
                                                                                            'case': 'acc',
                                                                                            'gender': 'fem',
                                                                                            'number': 'sing',
                                                                                            'raw_gram_info': 'animacy=inan|case=acc|gender=fem|number=sing',
                                                                                            'part_of_speech': 'NOUN'},
                                                                           'lemma': 'тачка', 'is_stop_word': False,
                                                                           'list_of_dependents': [5],
                                                                           'dependency_type': 'nsubj', 'head': 1},
                                                                          {'text': 'от', 'raw_text': 'от',
                                                                           'grammem_info': {'raw_gram_info': '',
                                                                                            'part_of_speech': 'ADP'},
                                                                           'lemma': 'от', 'is_stop_word': False,
                                                                           'list_of_dependents': [],
                                                                           'dependency_type': 'case', 'head': 5},
                                                                          {'text': '2015', 'raw_text': '2015',
                                                                           'lemma': '2015', 'original_text': '2015',
                                                                           'token_type': 'NUM_TOKEN',
                                                                           'token_value': {'value': 2015,
                                                                                           'adjectival_number': False},
                                                                           'list_of_token_types_data': [
                                                                               {'token_type': 'NUM_TOKEN',
                                                                                'token_value': {'value': 2015,
                                                                                                'adjectival_number': False}}],
                                                                           'grammem_info': {'numform': 'digit',
                                                                                            'raw_gram_info': 'numform=digit',
                                                                                            'part_of_speech': 'NUM'},
                                                                           'is_stop_word': False,
                                                                           'list_of_dependents': [],
                                                                           'dependency_type': 'nummod', 'head': 5,
                                                                           'is_beginning_of_composite': True,
                                                                           'composite_token_type': 'TIME_DATE_TOKEN',
                                                                           'composite_token_length': 2,
                                                                           'composite_token_value': {'year': 2015}},
                                                                          {'text': 'года', 'raw_text': 'года',
                                                                           'grammem_info': {'animacy': 'inan',
                                                                                            'case': 'gen',
                                                                                            'gender': 'masc',
                                                                                            'number': 'sing',
                                                                                            'raw_gram_info': 'animacy=inan|case=gen|gender=masc|number=sing',
                                                                                            'part_of_speech': 'NOUN'},
                                                                           'lemma': 'год', 'is_stop_word': False,
                                                                           'list_of_dependents': [3, 4],
                                                                           'dependency_type': 'nmod', 'head': 2,
                                                                           'is_beginning_of_composite': False,
                                                                           'composite_token_type': 'TIME_DATE_TOKEN',
                                                                           'composite_token_length': 2,
                                                                           'composite_token_value': {'year': 2015}},
                                                                          {'raw_text': '.', 'text': '.',
                                                                           'lemma': '.',
                                                                           'token_type': 'SENTENCE_ENDPOINT_TOKEN',
                                                                           'token_value': {'value': '.'},
                                                                           'list_of_token_types_data': [
                                                                               {
                                                                                   'token_type': 'SENTENCE_ENDPOINT_TOKEN',
                                                                                   'token_value': {
                                                                                       'value': '.'}}]}]}}

        res = inputter(test, self.use_new_search_engine)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "от 2015 года")

    def test_success_resp_year_to(self):
        test = {'MESSAGE_NAME': 'GET_DUCKLING_RESULT',
                'data': {'new_search_engine': self.use_new_search_engine, 'text': [{'text': 'Хочу', 'raw_text': 'Хочу',
                                                                           'grammem_info': {'aspect': 'impf',
                                                                                            'mood': 'ind',
                                                                                            'number': 'sing',
                                                                                            'person': '1',
                                                                                            'tense': 'notpast',
                                                                                            'transitivity': 'tran',
                                                                                            'verbform': 'fin',
                                                                                            'voice': 'act',
                                                                                            'raw_gram_info': 'aspect=impf|mood=ind|number=sing|person=1|tense=notpast|transitivity=tran|verbform=fin|voice=act',
                                                                                            'part_of_speech': 'VERB'},
                                                                           'lemma': 'хотеть', 'is_stop_word': False,
                                                                           'list_of_dependents': [2],
                                                                           'dependency_type': 'root', 'head': 0},
                                                                          {'text': 'тачку', 'raw_text': 'тачку',
                                                                           'grammem_info': {'animacy': 'inan',
                                                                                            'case': 'acc',
                                                                                            'gender': 'fem',
                                                                                            'number': 'sing',
                                                                                            'raw_gram_info': 'animacy=inan|case=acc|gender=fem|number=sing',
                                                                                            'part_of_speech': 'NOUN'},
                                                                           'lemma': 'тачка', 'is_stop_word': False,
                                                                           'list_of_dependents': [5],
                                                                           'dependency_type': 'nsubj', 'head': 1},
                                                                          {'text': 'до', 'raw_text': 'до',
                                                                           'grammem_info': {'raw_gram_info': '',
                                                                                            'part_of_speech': 'ADP'},
                                                                           'lemma': 'до', 'is_stop_word': False,
                                                                           'list_of_dependents': [],
                                                                           'dependency_type': 'case', 'head': 5},
                                                                          {'text': '2015', 'raw_text': '2015',
                                                                           'lemma': '2015', 'original_text': '2015',
                                                                           'token_type': 'NUM_TOKEN',
                                                                           'token_value': {'value': 2015,
                                                                                           'adjectival_number': False},
                                                                           'list_of_token_types_data': [
                                                                               {'token_type': 'NUM_TOKEN',
                                                                                'token_value': {'value': 2015,
                                                                                                'adjectival_number': False}}],
                                                                           'grammem_info': {'numform': 'digit',
                                                                                            'raw_gram_info': 'numform=digit',
                                                                                            'part_of_speech': 'NUM'},
                                                                           'is_stop_word': False,
                                                                           'list_of_dependents': [],
                                                                           'dependency_type': 'nummod', 'head': 5,
                                                                           'is_beginning_of_composite': True,
                                                                           'composite_token_type': 'TIME_DATE_TOKEN',
                                                                           'composite_token_length': 2,
                                                                           'composite_token_value': {'year': 2015}},
                                                                          {'text': 'года', 'raw_text': 'года',
                                                                           'grammem_info': {'animacy': 'inan',
                                                                                            'case': 'gen',
                                                                                            'gender': 'masc',
                                                                                            'number': 'sing',
                                                                                            'raw_gram_info': 'animacy=inan|case=gen|gender=masc|number=sing',
                                                                                            'part_of_speech': 'NOUN'},
                                                                           'lemma': 'год', 'is_stop_word': False,
                                                                           'list_of_dependents': [3, 4],
                                                                           'dependency_type': 'nmod', 'head': 2,
                                                                           'is_beginning_of_composite': False,
                                                                           'composite_token_type': 'TIME_DATE_TOKEN',
                                                                           'composite_token_length': 2,
                                                                           'composite_token_value': {'year': 2015}},
                                                                          {'raw_text': '.', 'text': '.',
                                                                           'lemma': '.',
                                                                           'token_type': 'SENTENCE_ENDPOINT_TOKEN',
                                                                           'token_value': {'value': '.'},
                                                                           'list_of_token_types_data': [
                                                                               {
                                                                                   'token_type': 'SENTENCE_ENDPOINT_TOKEN',
                                                                                   'token_value': {
                                                                                       'value': '.'}}]}]}}

        res = inputter(test, self.use_new_search_engine)

        self.assertEqual(res['STATUS'], True)

        search_text_form = res['PAYLOAD']['result']['search_text_form']

        self.assertEqual(search_text_form, "до 2015 года")
