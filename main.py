from plugins.db.upload_model import upload_model

import codecs




# with open('../persistants/classifier/base_model.pkl', 'rb') as f:
#     data = codecs.encode(f.read(), "base64").decode()

# with open('persistants/classifier/lil.pkl', 'rb') as f:
#     data = codecs.encode(f.read(), "base64").decode()
# with open('persistants/classifier/base_model_base64.txt', 'w') as f:
#     f.write(data)

upload_model("model_for_sd_ver_2")

# classifier = Classifier()
#
# for text in ['найди bmw', 'страховка авто', 'солярис', 'хочу купить авто в кредит', 'ипотека',
#              'хочу тачку подешевле', 'осаго', 'Skoda Octavia 2019 года в Москве']:
#     print(text, classifier.predict(text))