import pip._vendor.requests 
from datetime import datetime
import json

with open('stationCode.json', 'r',encoding='utf-8') as f:
    stationCodeList=json.load(f)
stationCodeList=stationCodeList['contents']

##stationCode: 125
stationName='제기동역'
subwayLine='1호선'

# 반복자 없으면 None 반환, 위에서 입력한 역과 호선이 일치하는 것을 code라는 리스트에 넣고 마지막 결과를 stationCode에 넣는다.
stationCode=next((code for code in stationCodeList if (code['stationName']==stationName and code['subwayLine']==subwayLine)),None)['stationCode']

now = datetime.now()
day = [ "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"] # weekday():날짜의 요일 정보를 숫자값으로 리턴. 0은 월요일이고, 6일 일요일.
url = f"https://apis.openapi.sk.com/puzzle/congestion-train/stat/stations/{stationCode}?dow={day[now.weekday()]}&hh={now.hour}"
headers = {'Content-Type': 'application/json; charset=utf-8'}
params={
    'Accept': 'application/json',
    'appKey': 'pa9QvuuFu82jHWycxt21dan2IW3gmf55419lWWDt'
    }
response = pip._vendor.requests.get(url, headers=headers, params=params)

conjestionInfo=json.loads(response.text)

file_path=f'[{stationCode}][{now.year}{now.month}{now.day}][{now.hour}]_conjestionInfo.json'
with open(file_path, 'w', encoding='UTF-8') as f:
    json.dump(conjestionInfo, f, ensure_ascii=False)