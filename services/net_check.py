from requests import get
from subprocess import getoutput
from socket import gethostbyname

def internet_test(site:str = "http://www.google.com") -> str:
    try:
        get(site)
        return "Интернет подключен"
    except Exception as e:
        return f"Ошибка подключения: {str(e)}"

def ping_test(host:str = "8.8.8.8") -> str:
    try:
        getoutput(f"ping -c 1 {str(host)}")
        return f"Ping {host} -> Удачно"
    except Exception as e:
        return f"Ошибка при попытке ping {host}: {str(e)}"

def dns_check(domen:str = "google.com") -> str:
    try:
        ip = gethostbyname(domen)
        return f"Успешное DNS разрешение для {domen} -> {ip}"
    except Exception as e:
        return f"Не удалось полчуить DNS разрешение для {domen}.Ошибка: {str(e)}"

def net_check() -> str:
    return f"{internet_test()}\n{ping_test()}\n{dns_check()}\n"