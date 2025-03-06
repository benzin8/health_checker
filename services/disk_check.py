from shutil import disk_usage

def disk_test() -> str:
    disk = disk_usage('/')
    return (f"Всего места: {disk.total / (2**30):.2f} GB\n"
            f"Использованно места: {disk.used / (2**30):.2f} GB\n"
            f"Свободного места: {disk.free / (2**30):.2f} GB\n")

def disk_check() -> str:
    return f"{disk_test()}\n"
