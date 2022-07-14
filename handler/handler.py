import logging
from prometheus_client import Summary

from function.plugins.inputer import inputter
from function.plugins.helper import timing

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Метод handlers. Этот метод будет вызываться при вызове функции
@REQUEST_TIME.time()
@timing
def handler(request):
    payload = request.form if request.form else request.json
    resp = inputter(payload)
    return (
        resp
        ,
        200,
        {"Content-Type": "application/json"})
