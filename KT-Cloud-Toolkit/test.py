import json
import sys
import server
sys.path.append("./KT-Cloud-Toolkit/")

def find_zone_by_name(json_data, target_name):
    zones = json_data.get('listzonesresponse', {}).get('zone', [])
    for zone in zones:
        if zone.get('name') == target_name:
            return zone
    return None

def listZones():
    response = server.listZones()
    return response

# JSON 데이터 가져오기
json_data = listZones()

# 'KOR-Seoul M2'인 zone 찾기
target_name = 'KOR-Seoul M2'
found_zone = find_zone_by_name(json_data, target_name)

# 결과 출력
if found_zone:
    print(json.dumps(found_zone, indent=4))
else:
    print(f"No zone found with name '{target_name}'")