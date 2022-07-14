import logging

from .responder.tlg import send_log
from .duckling.typonder import replace_typos, prepare_data_tokenize_str
from .config import cfg
from .duckling.classifier import Classifier
from .db.query import insert_value_to_audit

tlg_logger: str = cfg.app.url.tlg

use_tlg_logger: bool = cfg.app.main.use_tlg_logger

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)

classifier = Classifier(use_database=True)


def inputter(res: dict):
    log.debug(f'start process message with payload - {res}')
    result: dict = {}
    search_res_text_from = None
    status = False

    text: list = res["data"]["text"]

    query = res["data"].get("query", "empty")
    session_id = res["data"].get("sessionid", "empty")
    user_id = res["data"].get("userid", "empty")
    if cfg.app.main.use_graph_ql:
        try:
            insert_value_to_audit(text=query,
                                  session_id=session_id,
                                  user_id=user_id)
        except Exception as e:
            log.debug(str(e))
            log.debug("troubles with gql query")

    txt = prepare_data_tokenize_str(text)

    if cfg.app.main.use_model:
        predict_class = classifier.predict(txt)
    else:
        predict_class = "toggle_is_off"
    try:
        log.debug("message_name - %r info - %r", "GET_CLASSIFICATION_RESULT", "token - {}".format(txt))
        # если запрос не касается поиска авто б то сразу кидаем 404
        if predict_class not in ("search", "model not load eat"):
            if use_tlg_logger:
                logger_string = f"☢️ the text - {txt} has a class - {predict_class}. Go to another app!"
                # send_message(url=tlg_logger, text=logger_string, chat_id=81432612)
                send_log(
                    log_str=logger_string,
                    bot_name="sberauto",
                    func_host="https://smapi.pv-api.sbc.space/fn_df4f75ea_c184_4999_92ae_5f0f20ec9f2b"
                )
            log.debug(f'intent isnt class search')
            return {"MESSAGE_NAME": "GET_DUCKLING_RESULT",
                    "CODE": 504,
                    "STATUS": status,
                    "PAYLOAD": {
                        "result": {
                            "search_text_form": search_res_text_from if search_res_text_from else False
                        },
                        "description": "nothing found",
                        "target": predict_class
                    }}
        else:
            # TODO Кажется, что в это условие никогда не заходит
            # status = False
            if use_tlg_logger:
                logger_string = f"☢️ by the text - {txt} nothing found."
                send_log(
                    log_str=logger_string,
                    bot_name="sberauto",
                    func_host="https://smapi.pv-api.sbc.space/fn_df4f75ea_c184_4999_92ae_5f0f20ec9f2b"
                )
            log.debug(f'function done work fine but nothing found')
            return {"MESSAGE_NAME": "GET_CLASSIFICATION_RESULT",
                    "CODE": 504,
                    "STATUS": status,
                    "PAYLOAD": {
                        "result": {
                            "search_text_form": search_res_text_from if search_res_text_from else False
                        },
                        "description": "nothing found",
                        "target": predict_class
                    }}

    except Exception as e:
        log.debug("message_name - %r info - %r error - %r",
                  "GET_CLASSIFICATION_RESULT",
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
        return {"MESSAGE_NAME": "GET_CLASSIFICATION_RESULT",
                "CODE": 504,
                "STATUS": status,
                "PAYLOAD": {
                    "result": result,
                    "description": "error",
                    "target": predict_class
                }}