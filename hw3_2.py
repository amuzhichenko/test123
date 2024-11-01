#Написать скрипт, который будет делать ping google.com. Если сервер отвечает, то выводить - success, если нет - doesn't work.

import os

def ping_srv(host):
    command = f"ping -n 5 {host}"
    response = os.system(command)

    if response == 0:
        print("success")
    else:
        print("doesn't work")

ping_srv("google.com")

