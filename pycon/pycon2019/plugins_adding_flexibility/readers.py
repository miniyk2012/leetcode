import json as jsonlib

import pandas as pd

__READERS = dict()


def register(func):
    __READERS[func.__name__] = func
    return func


def read(plugin, *args, **kwargs):
    if plugin in __READERS:
        return __READERS[plugin](*args, **kwargs)
    else:
        raise  TypeError(f"{plugin} not supported")


@register
def csv(file_path, delimiter, *args, **kwargs):
    """read csv file return Pandas DataFrame"""
    return pd.read_csv(file_path, delimiter=delimiter)


@register
def json(file_path, *args, **kwargs):
    """read json file return Pandas DataFrame"""
    json_dict = jsonlib.loads(file_path.read_text())
    return pd.DataFrame(json_dict)
