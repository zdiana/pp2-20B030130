import json

jsondata = open('C:\CPP\PP2\TSIS4\sample-data.json').read()

json_object = json.loads(jsondata)
print(
    "Interface Status")
print(
    "=======================================================================================")
print(
    "DN                                                 Description           Speed    MTU")
print( 
    "-------------------------------------------------- --------------------  ------  ------")
imdata = json_object["imdata"]
for i in imdata:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print("{0:50} {1:20} {2:7} {3:6}".format(dn,descr,speed,mtu))