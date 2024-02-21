# гавнокод лаунчера, зато никаких вирусов)

import os
import json
from art import text2art
from colorama import Fore, init
import requests

init()

version = 1.0
clear = lambda: os.system("cls")


def os_check():
    if os.name == "nt":
        pass
    else:
        print("Системы UNIX временно не поддерживаются.")
        exit(0)


def settings():
    # проверка папки и вопрос про настройку
    if not os.path.isdir("C:\\cmt-launcher"):
        os.mkdir("C:\\cmt-launcher")
        set_settings = True
    else:
        i = input("Желаете настроить запуск заново? (yes/no) > ")
        if i == "yes":
            set_settings = True
        elif i == "no":
            set_settings = False
        else:
            print("Перезапустите программу. Укажите верный ответ (y/n)")
            exit(0)

    # настройка
    if set_settings:
        clear()
        print(Fore.LIGHTYELLOW_EX + text2art("CMT") + Fore.RESET)
        print("Настройка запуска")
        username = input("Введите никнейм > ")
        ram = input(
            "Введите максимальзую используемую оперативную память (в мб, рекомендуемо от 4096) > "
        )

        # запись в файл
        json_settings = {"username": username, "ram": ram}

        with open(
            "C:\\cmt-launcher\\launcher-configuration.json", "w", encoding="UTF-8"
        ) as f:
            json.dump(json_settings, f, sort_keys=True, indent=4)


def update():
    clear()
    print(Fore.LIGHTYELLOW_EX + text2art("CMT") + Fore.RESET)

    print('Проверка обновлений')

    # чекаем версию на гх
    r = requests.get('https://github.com/art3m4ik3/CMT-Launcher/raw/main/version.txt')
    if float(r.text) != version:
        print('Вышла новая версия. Обновление.')
        os.system('curl -Lo cmt-launcher.exe https://github.com/art3m4ik3/CMT-Launcher/releases/latest/download/cmt-launcher.exe')
        print('Перезапустите лаунчер на новой версии!')
        exit(0)
    else:
        print('Текущая версия. Запуск.')



if __name__ == "__main__":
    try:
        os_check()
        clear()
        print(Fore.LIGHTYELLOW_EX + text2art("CMT") + Fore.RESET)
        settings()
        update()
    except KeyboardInterrupt:
        exit(0)
