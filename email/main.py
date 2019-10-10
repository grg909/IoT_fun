# -*- coding: UTF-8 -*-

# @Date    : 2019/6/16
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    check air polution and control xiaomi airpurifier automatically
"""

import os
import time
from dotenv import load_dotenv
from miio.airpurifier import AirPurifier
import get_aqi
from pprint import pprint
import logging

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)
logging.basicConfig(
    filename='log/log.log',
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=10)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.info('获取aqi数据中。。。')

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

ip = os.environ.get('MIROBO_IP')
token = os.environ.get('MIROBO_TOKEN')
air = AirPurifier(ip, token)

aqi_raw = get_aqi.get_aqi(lat_lng = '39.856;116.368')
aqi_dict = get_aqi.process_aqi(aqi_raw)

pprint(aqi_dict)
pprint('-' * 30)

if aqi_dict['pm25'] > 100 or aqi_dict['pm10'] > 200:
    logging.info('空气有点糟糕，准备启动净化器。。。')
    time.sleep(5)
    air.on()
else:
    logging.info('外面空气还不错，准备关闭净化器。。。')
    time.sleep(5)
    air.off()
