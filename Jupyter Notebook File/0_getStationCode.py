import requests
import json

stationInfo_url = "https://apis.openapi.sk.com/puzzle/subway/stations"

headers = {'Content-Type': 'application/json; charset=utf-8'}
params = {
    'Accept': 'application/json',
    'appKey': 'pa9QvuuFu82jHWycxt21dan2IW3gmf55419lWWDt'
}
response = requests.get(stationInfo_url, headers=headers, params=params)

stationInfo = json.loads(response.text)

print(stationInfo)

file_path='./stationCode.json'
with open(file_path, 'w', encoding='UTF-8') as f:
    json.dump(stationInfo, f, ensure_ascii=False)

