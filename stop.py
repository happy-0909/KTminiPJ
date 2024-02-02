import sys
sys.path.append("./KT-Cloud-Toolkit/")
import json
import time
import server

def listvirtualmachine():
    response = server.listVirtualMachines(zone='KR-M2',)
    return response

def stopvirtuamachine(stopvirtuamachine):
    stop = server.stopVirtualMachine(zone='KR-M2', vmid=stopvirtuamachine)
    return stop

def find_virtual_machine_id_by_name(name):
    response = listvirtualmachine()
    virtualmachines = response['listvirtualmachinesresponse']['virtualmachine']
    for virtualmachine in virtualmachines:
        if virtualmachine['name'] == name:
            return virtualmachine['id']
    return None

def main():
    response = listvirtualmachine()
    virtualmachine_name = [virtualmachine['name'] for virtualmachine in response['listvirtualmachinesresponse']['virtualmachine']]
    print(json.dumps(response, indent=4))
    print(virtualmachine_name)
    virtual_machine_name = input("가상 머신 이름을 입력하세요: ")
    virtual_machine_id = find_virtual_machine_id_by_name(virtual_machine_name)
    if virtual_machine_id:
        print("가상 머신 ID:", virtual_machine_id)
        stop_result = stopvirtuamachine(virtual_machine_id)
        if stop_result:
            print("가상 머신 중지 결과:", stop_result)
        else:
            print(virtual_machine_id, "없는 가상 머신입니다.")
    else:
        print(virtual_machine_name, "이름의 가상 머신을 찾을 수 없습니다.")


if __name__ == "__main__":
    main()