from subprocess import getoutput

def serv_test(service:str) -> str:
    try:
        status = getoutput(f"systemctl is-active {service}")
        if status == "active":
            return f"Сервис {service} активен"
        else:
            return f"Сервис {service} не активен"
    except Exception as e:
        return f"Не удалось проверить {service}: {str(e)}"

def log_test() -> str:
    try:
        errors = getoutput("journalctl -p err..alert -n 5")
        if "No entries" in errors:
            return "Критическких ошибок нет"
        else:
            return f"Критические ошибки: {errors}"
    except Exception as e:
        return f"Не удалось проверить логи: {str(e)}"

def serv_check() -> str:
    services = ["ssh", "httpd", "mysql"]
    result = []
    for service in services:
        result.append(serv_test(service))
    result.append(log_test())
    return "\n".join(result) + "\n"
