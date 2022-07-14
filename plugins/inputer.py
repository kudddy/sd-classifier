import logging

try:
    from ..plugins.responder.tlg import send_message, send_log
    from ..plugins.duckling.typonder import replace_typos, prepare_data_tokenize_str
    from ..plugins.config import cfg
    from ..plugins.duckling.classifier import Classifier
    from ..plugins.db.query import insert_value_to_audit
except Exception as e:
    from plugins.responder.tlg import send_message, send_log
    from plugins.duckling.typonder import replace_typos, prepare_data_tokenize_str
    from plugins.config import cfg
    from plugins.duckling.classifier import Classifier
    from plugins.db.query import insert_value_to_audit

use_tlg_logger: bool = cfg.app.main.use_tlg_logger

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)

classifier = Classifier(use_database=True)


def inputter(res: dict):
    log.debug(f'start process message with payload - {res}')

    text: list = res["data"]["text"]

    # if cfg.app.main.use_graph_ql:
    #     try:
    #         insert_value_to_audit(text=query,
    #                               session_id=session_id,
    #                               user_id=user_id)
    #     except Exception as e:
    #         log.debug(str(e))
    #         log.debug("troubles with gql query")

    txt = prepare_data_tokenize_str(text)

    if cfg.app.main.use_model:
        predict_class = classifier.predict(txt)
    else:
        predict_class = "model_not_use"
    try:
        log.debug("message_name - %r info - %r", "GET_CLASSIFIER_RESULT", "token - {}".format(txt))
        # если запрос не касается поиска авто б то сразу кидаем 404

        if predict_class == "model not loaded yet":
            if use_tlg_logger:
                logger_string = f"☢️ the text - {txt} has a class - {predict_class}. Go to another app!"
                # send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
                send_log(
                    log_str=logger_string,
                    bot_name="sberauto",
                    func_host="https://smapi.pv-api.sbc.space/fn_df4f75ea_c184_4999_92ae_5f0f20ec9f2b"
                )
            status: bool = False
            return {"MESSAGE_NAME": "GET_CLASSIFIER_RESULT",
                    "CODE": 404,
                    "STATUS": status,
                    "PAYLOAD": {
                        "description": "model not loaded yet",
                        "target": predict_class
                    }}
        elif predict_class == "model_not_use":
            log.debug(f'feature toggle is off')
            status: bool = False
            return {"MESSAGE_NAME": "GET_CLASSIFIER_RESULT",
                    "CODE": 404,
                    "STATUS": status,
                    "PAYLOAD": {
                        "description": "feature toggle is off",
                        "target": predict_class
                    }}
        else:
            log.debug("ok, send good response")
            status: bool = True
            return {"MESSAGE_NAME": "GET_CLASSIFIER_RESULT",
                    "CODE": 200,
                    "STATUS": status,
                    "PAYLOAD": {
                        "description": "OK",
                        "target": predict_class
                    }}
    except Exception as e:
        log.debug("message_name - %r info - %r error - %r",
                  "GET_CLASSIFIER_RESULT",
                  "token - {}".format(txt),
                  e)
        status = False
        if use_tlg_logger:
            logger_string = f"🛑 some problems with text - {txt} ошибка - {str(e)[0:4095]}"
            # send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
            send_log(
                log_str=logger_string,
                bot_name="sberauto",
                func_host="https://smapi.pv-api.sbc.space/fn_df4f75ea_c184_4999_92ae_5f0f20ec9f2b"
            )
        logging.info(f'function done work incorrect with error - {e}')
        return {"MESSAGE_NAME": "GET_CLASSIFIER_RESULT",
                "CODE": 504,
                "STATUS": status,
                "PAYLOAD": {
                    "description": "error",
                    "target": predict_class
                }}
