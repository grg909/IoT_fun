# -*- coding: UTF-8 -*-

# @Date    : 2019/6/16
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    get air polution api
"""

import random
import requests
import os
from dotenv import load_dotenv

# World Air Quality    http://aqicn.org/
# API doc              http://aqicn.org/json-api/doc/

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


def get_aqi(lat_lng):

    token = os.environ.get('AQI_TOKEN')
    ip = ''.join([random.randint(1, 254).__str__(), '.', random.randint(1, 254).__str__(
    ), '.', random.randint(1, 254).__str__(), '.', random.randint(1, 254).__str__()])
    url = 'https://api.waqi.info/feed/geo:' + lat_lng + '/?token=' + token
    headers = {
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
        'X-Forwarded-For': ip}
    r = requests.get(url, headers=headers)
    data = r.json()

    return data


def process_aqi(data):
    s = data
    #     print(json.dumps(s, indent=4))
    res = {}
    if s['status'] == "ok":
        res['cityName'] = s['data']['city']['name']
        res['time'] = s['data']['time']['s']
        res['aqi'] = s['data']['aqi']
        try:
            res['pm25'] = s['data']['iaqi']['pm25']['v']
        except BaseException:
            res['pm25'] = "N/A"
        try:
            res['pm10'] = s['data']['iaqi']['pm10']['v']
        except BaseException:
            res['pm10'] = "N/A"
        try:
            res['temp'] = s['data']['iaqi']['t']['v']
        except BaseException:
            res['temp'] = "N/A"
        try:
            res['humidity'] = s['data']['iaqi']['h']['v']
        except BaseException:
            res['humidity'] = "N/A"
        try:
            res['wind'] = s['data']['iaqi']['w']['v']
        except BaseException:
            res['wind'] = "N/A"
    else:
        res = s
    return res
