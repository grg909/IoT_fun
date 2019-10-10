# -*- coding: UTF-8 -*-

# @Date    : 2019/6/16
# @Author  : WANG JINGE
# @Email   : wang.j.au@m.titech.ac.jp
# @Language: python 3.7
"""
    air polution checker and send warning email
"""

import os
import get_aqi
from pprint import pprint
import yagmail
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

yag = yagmail.SMTP(
    'example@example.com',
    os.environ.get('example'),
    host='example.com',
    port=123)

aqi_raw = get_aqi.get_aqi(lat_lng='12.456;45.678')
aqi_dict = get_aqi.process_aqi(aqi_raw)

pprint(aqi_dict)

contents = """
<table width="400" border="1" style="position:absolute; top: 120px">
     <tr>
      <th align="left">空气质量指标</th>
      <th align="right">数值</th>
     </tr>
     <tr>
      <td align="left">PM2.5</td>
      <td align="right">{pm25}</td>
     </tr>
     <tr>
      <td align="left">PM10</td>
      <td align="right">{pm10}</td>
     </tr>
     <tr>
      <td align="left">风力</td>
      <td align="right">{wind}</td>
     </tr>
     <tr>
      <td align="left">时间</td>
      <td align="right">{time}</td>
     </tr>
     <tr>
      <th align="left">测量站</th>
      <th align="right">{city}</th>
     </tr>
</table>
""".format(pm25=aqi_dict['pm25'],
           pm10=aqi_dict['pm10'],
           wind=aqi_dict['wind'],
           time=aqi_dict['time'],
           city=aqi_dict['cityName'][26:-1])

if aqi_dict['pm25'] > 100 or aqi_dict['pm10'] > 200:
    yag.send(to='example@example.com', subject='Warning email for air polution',
             contents=contents)