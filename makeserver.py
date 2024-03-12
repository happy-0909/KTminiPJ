import sys
sys.path.append("./KT-Cloud-Toolkit/")
import json
import server
import time

def listNetworks():
    response = server.listNetworks(zone='KR-M2')
    # 여기서는 첫 번째 네트워크의 ID를 반환하도록 설정
    network_id = response.get('listnetworksresponse', {}).get('network', [{}])[0].get('id', '')
    return network_id


servername = input("생성할 서버의 이름을 입력해주세요:")
servernum = int(input("몇 대의 서버를 생성할까요?:"))

network_id = listNetworks()

def deployVirtualMachine():
    responses = []
    for i in range(1, servernum + 1):
        name_with_number = f"{servername}{i}"
        response = server.deployVirtualMachine(
            zone="KR-M2",
            serviceofferingid="753c80b0-b03f-4a91-98a7-6b11233f85a8", #id 값은 ./KT-Cloud-Toolkit/EXlist 안에있는 txt 파일 참고
            templateid="23bc4025-8a16-4ebf-aa49-3160ee2ac24b",        #id 값은 ./KT-Cloud-Toolkit/EXlist 안에있는 txt 파일 참고
            networkids=network_id,
            ipaddress=f"172.27.1.{0 + i}", # 사설아이피 주소 변경은 이곳을 수정 ex) 172.27.19.{50 + i} 
            name=name_with_number
        )
        responses.append(response)
        time.sleep(2)  
    return responses

result = deployVirtualMachine()
for response in result:
    print(json.dumps(response, indent=4))
