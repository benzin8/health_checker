from psutil import virtual_memory, cpu_percent


def cpu_test() -> str:
    cpu = cpu_percent(interval=1)
    return f"CPU: {cpu} %"

def ram_test() -> str:
    ram = virtual_memory()
    return (f"Всего RAM: {ram.total / (2**30):.2f} GB\n"
            f"Нагрузка RAM: {ram.used / (2**30):.2f} GB\n"
            f"Свободно RAM: {ram.available / (2**30):.2f} GB\n")

def cpu_check() -> str:
    return f"{cpu_test()}\n{ram_test()}\n"