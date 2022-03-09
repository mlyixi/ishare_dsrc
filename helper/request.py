# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Dec  8 2021, 21:08:43) 
# [GCC 8.4.0]
# Embedded file name: helper/request.py
import requests, json

def get(url, param={}):
    try:
        r = requests.get(url, params=param)
        r.raise_for_status()
        return json.loads(r.text)
    except requests.exceptions.HTTPError as err:
        print err.response.text
        return False


def post(url, datas={}):
    try:
        r = requests.post(url, data=datas)
        r.raise_for_status()
        return json.loads(r.text)
    except requests.exceptions.HTTPError as err:
        print err.response.text
        return False
# okay decompiling request.pyc
