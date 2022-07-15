import logging


from .responder.tlg import send_log
from .duckling.typonder import prepare_data_tokenize_str
from .config import cfg
from .duckling.classifier import Classifier

use_tlg_logger: bool = cfg.app.main.use_tlg_logger
logger_url: str = cfg.app.logger.url
bot_name: str = cfg.app.logger.name


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
                logger_string = f"☢️ the text - {txt} not processed because model not load yet!"
                # send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
                send_log(
                    log_str=logger_string,
                    bot_name=bot_name,
                    func_host=logger_url
                )
            return {"MESSAGE_NAME": "GET_CLASSIFIER_RESULT",
                    "CODE": 404,
                    "STATUS": False,
                    "PAYLOAD": {
                        "description": "model not loaded yet",
                        "target": predict_class
                    }}
        elif predict_class == "model_not_use":
            log.debug(f'feature toggle is off')
            if use_tlg_logger:
                logger_string = f"☢️ the text - {txt} not processed because feature toggle is off!"
                # send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
                send_log(
                    log_str=logger_string,
                    bot_name=bot_name,
                    func_host=logger_url
                )
            return {"MESSAGE_NAME": "GET_CLASSIFIER_RESULT",
                    "CODE": 404,
                    "STATUS": False,
                    "PAYLOAD": {
                        "description": "feature toggle is off",
                        "target": predict_class
                    }}
        else:
            log.debug("ok, send good response")
            if use_tlg_logger:
                logger_string = f"✅️ the text - {txt} have class - {predict_class}. It is all be good!"
                # send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
                send_log(
                    log_str=logger_string,
                    bot_name=bot_name,
                    func_host=logger_url
                )
            return {"MESSAGE_NAME": "GET_CLASSIFIER_RESULT",
                    "CODE": 200,
                    "STATUS": True,
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
            logger_string = f"🛑 some problems with text - {txt} error - {str(e)[0:4095]}"
            send_log(
                log_str=logger_string,
                bot_name=bot_name,
                func_host=logger_url
            )
        logging.info(f'function done work incorrect with error - {e}')
        return {"MESSAGE_NAME": "GET_CLASSIFIER_RESULT",
                "CODE": 504,
                "STATUS": status,
                "PAYLOAD": {
                    "description": "error",
                    "target": predict_class
                }}
