import json
import logging

from requests import request

try:
    from ..helper import timing
    from ..config import cfg
    from ...plugins.db.apig_sdk import signer
except Exception as e:
    from plugins.helper import timing
    from plugins.db.apig_sdk import signer
    from plugins.config import cfg

dataspace_url = cfg.app.auth.url
app_key = cfg.app.auth.key
app_secret = cfg.app.auth.secret

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)

sig = signer.Signer()
sig.Key = app_key
sig.Secret = app_secret


@timing
def send_message(url: str,
                 chat_id: int,
                 text: str,
                 parse_mode: str = None,
                 buttons: list or None = None,
                 inline_keyboard: list or None = None,
                 one_time_keyboard: bool = True,
                 resize_keyboard: bool = True,
                 remove_keyboard: bool = False):
    payload = {
        "chat_id": chat_id,
        "text": text[:4095],
        "reply_markup": {
            "remove_keyboard": remove_keyboard
        }
    }

    if parse_mode:
        payload.update({"parse_mode": parse_mode})

    if buttons:
        # TODO hardcode
        keyboards = [[{"text": text}] for text in buttons]
        payload["reply_markup"].update({
            "keyboard": keyboards,
            "resize_keyboard": resize_keyboard,
            "one_time_keyboard": one_time_keyboard
        })

    if inline_keyboard:
        payload["reply_markup"].update({"inline_keyboard": inline_keyboard})

    headers = {
        "Content-Type": "application/json"
    }
    # не дожидаемся ответа чтобы не терять время
    # requests.get(url, headers=headers, data=json.dumps(payload), ssl=False)
    request("GET", url, headers=headers, data=json.dumps(payload))
    # маскирование текста
    payload["text"] = "*******"

    log.debug("request with payload: %s success delivered to tlg", payload)


def send_log(log_str: str, bot_name: str, func_host: str):
    body = {
        "MESSAGE_NAME": "LOGGER_INFO",
        "DATA": {
            "log_info": log_str,
            "bot_type": bot_name
        }
    }

    r = signer.HttpRequest("POST",
                           func_host,
                           {"Content-Type": "application/json", "x-stage": "RELEASE"},
                           body=json.dumps(body))
    sig.Sign(r)

    data = request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body, verify=False)
