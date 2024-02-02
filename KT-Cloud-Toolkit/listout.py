import sys
sys.path.append("./KT-Cloud-Toolkit/")
import json
import server

def listNetworks():
    response = server.listNetworks(zone='KR-M2')
    return response

# JSON 데이터를 문자열로 변환


print(json.dumps(listNetworks(), indent=4))
