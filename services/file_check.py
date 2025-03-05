import os

def file_check(file_path:str, perm:str) -> str:
    result =[]

    try:
        with open(file_path, "rb") as f:
            while f.read(1024*1024): pass
        result.append(f"Файл {file_path} в порядке")
    except Exception as e:
        result.append(f"Битые байты в файле {file_path}: {str(e)}")

    try:
        current_perm = oct(os.stat(file_path).st_mode)[-3:]
        if current_perm == perm:
            result.append(f"Права доступа файла {file_path} = {perm}")
        else:
            result.append(f"Права доступа файла {file_path} {current_perm} != {perm}")
    except Exception as e:
        result.append(f"Не удалось проверить файл {file_path}: {str(e)}")

    return "\n".join(result)