import yaml


def load_config(filename: str):
    with open(filename, 'r') as stream:
        config = yaml.safe_load(stream)
    return config


try:
    config = load_config('function/config/prod.yaml')
except:
    config = load_config('config/prod.yaml')


class ConfigObj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [ConfigObj(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, ConfigObj(b) if isinstance(b, dict) else b)


cfg = ConfigObj(config)
