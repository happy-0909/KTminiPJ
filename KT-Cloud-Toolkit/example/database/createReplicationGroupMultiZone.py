import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
# Zone parameter
    # 1) KR-CA : KOR-Central A Zone
    # 2) KR-CB : KOR-Central B Zone
    # 3) KR-M  : KOR-Seoul M Zone
    # 4) KR-M2 : KOR-Seoul M2 Zone

# simple example
print(db.createReplicationGroupMultiZone(
    instancename='sdktestmca',
    storagesize='80',
    perfclass='1x1',
    maintenanceweekday='sun',
    parametergroupid='11',
    dbmastername='AAtest123',
    dbmasterpassword='abcd1234',
    dbname='AATest123',
    dbengineversion='5.5.27',
    mainzone='KR-M',
    remotezone='KR-CA',
    usageplantype='monthly'))
