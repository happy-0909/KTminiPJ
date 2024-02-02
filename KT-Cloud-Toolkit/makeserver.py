import sys
sys.path.append("./KT-Cloud-Toolkit/")
import json
import server
import time

def deployVirtualMachine ():
    response = server.deployVirtualMachine (
        zone="KR-M2",
        serviceofferingid="753c80b0-b03f-4a91-98a7-6b11233f85a8",
        templateid="23bc4025-8a16-4ebf-aa49-3160ee2ac24b",
            )
    return response

for _ in range(1):
    result = deployVirtualMachine()
    print(json.dumps(result, indent=4))
    time.sleep(2)

