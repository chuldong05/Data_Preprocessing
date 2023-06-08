import pip._vendor.requests
from datetime import datetime
import json

with open('stationCode.json', 'r', encoding='utf-8') as f:
    stationCodeList=json.load(f)['contents']
# print(type(stationCodeList)) -> list 나옴.
# stationCodeList=stationCodeList['contents']
# print(stationCodeList) key가 status랑 contents가 있는데, 그 중 contents인 요소 {}들이 쭉쭉 나온다.


stationName='제기동역'
subwayLine='1호선'

stationCode=next((code for code in stationCodeList if (code['stationName']==stationName and code['subwayLine']==subwayLine)),None)
print(stationCode)


