import time
import logging
import base64

import dill
import codecs
import pickle
import math
from glob import glob
from tqdm.auto import tqdm
import random

try:
    from ..plugins.config import cfg
except Exception as e:
    from plugins.config import cfg

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)


def timing(f):
    def wrap(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        end = time.time()
        log.debug('{:s} function took {:.3f} ms'.format(f.__name__, (end - start) * 1000.0))
        return ret

    return wrap


def is_true(val):
    if val:
        return val


def split(data, size):
    return [data[i * size: (i + 1) * size] for i in range(math.ceil(len(data) / size))]


def split_base64(data, count_line=45_000):
    return list(map(lambda x: '\n'.join(x), split(data.split('\n'), count_line)))


def save_splits(data_splits):
    for i, data_split in enumerate(data_splits):
        with open(f'../persistants/classifier/base_model_base64_part{i}.txt', 'w') as f:
            f.write(data_split)
