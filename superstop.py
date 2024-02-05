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

def stop_multiple_virtual_machines():
    response = listvirtualmachine()
    virtualmachines = response['listvirtualmachinesresponse']['virtualmachine']
    virtual_machine_names = [virtualmachine['name'] for virtualmachine in virtualmachines]

    print("가상 머신 목록:")
    for index, name in enumerate(virtual_machine_names):
        print(f"{index + 1}. {name}")

    input_names = input("중지할 가상 머신 이름을 입력하세요 (여러 개의 가상 머신 이름은 쉼표로 구분): ").split(',')
    for input_name in input_names:
        input_name = input_name.strip()
        virtual_machine_id = find_virtual_machine_id_by_name(input_name)
        if virtual_machine_id:
            stop_result = stopvirtuamachine(virtual_machine_id)
            if stop_result:
                print(f"{input_name} 가상 머신이 중지되었습니다.")
            else:
                print(f"{input_name} 가상 머신을 중지하는 데 문제가 발생했습니다.")
        else:
            print(f"{input_name} 이름의 가상 머신을 찾을 수 없습니다.")

def main():
    print("1. 개별 가상 머신 중지")
    print("2. 여러 가상 머신 한 번에 중지")
    choice = input("원하는 작업을 선택하세요 (숫자 입력): ")

    if choice == '1':
        virtual_machine_name = input("가상 머신 이름을 입력하세요: ")
        stop_single_virtual_machine(virtual_machine_name)
    elif choice == '2':
        stop_multiple_virtual_machines()
    else:
        print("올바른 선택이 아닙니다.")

if __name__ == "__main__":
    main()
