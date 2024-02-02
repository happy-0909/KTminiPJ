import sys
sys.path.append("./KT-Cloud-Toolkit/")
import json
import time
import server

def listZones():
    response = server.listZones()
    return response

def listvirtualmachine():
    response = server.listVirtualMachines(zone='KR-M2',)
    return response

def stopvirtuamachine(stopvirtuamachine):
    stop = server.stopVirtualMachine(zone='KR-M2', vmid=stopvirtuamachine)
    return stop

def destroyvirtualmachine(delvirtuamachine):
    destroy = server.destroyVirtualMachine(zone='KR-M2', vmid=delvirtuamachine)
    return destroy

def main():
    response = listvirtualmachine()
    virtualmachine_ids = [virtualmachine['id'] for virtualmachine in response['listvirtualmachinesresponse']['virtualmachine']]
    print(response)
    print(virtualmachine_ids)
    virtual_machine_id = input("가상 머신 ID를 입력하세요: ")
    stop_result = stopvirtuamachine(virtual_machine_id)
    time.sleep(10)
    if stop_result:
        print("가상 머신 중지 결과:", stop_result)
        destroy_result = destroyvirtualmachine(virtual_machine_id)
    
        if destroy_result:
            print("가상 머신 삭제 결과:", destroy_result)
        else:
            print(virtual_machine_id,"없는 가상 머신입니다.")
    else:
        print(virtual_machine_id,"없는 가상 머신입니다.")



if __name__ == "__main__":
    main()

#print(json.dumps(listZones(), indent=4))
