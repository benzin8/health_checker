import mysql.connector


def check_db_connection(
        host="localhost",
        user='',
        password=''
) -> str:
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        conn.close()
        return f"Успешное подключение к серверу БД"
    except Exception as e:
        return f"Ошибка проверки подключения: {str(e)}"

def check_db_operations(
        host="localhost",
        user="benzin",
        password="",
        database_name="test"
) -> str:
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )
        cursor = conn.cursor()
        cursor.execute("CREATE TEMPORARY TABLE test (id INT, data VARCHAR(255))")
        cursor.execute("INSERT INTO test VALUES(1, 'test')")
        cursor.execute("DROP TABLE test")
        conn.close()
        return "Операции с БД прошли успешно"
    except Exception as e:
        return f"Ошибка при проведении операций: {str(e)}"

def db_check() -> str:
    result = [check_db_connection(), check_db_operations()]
    return "\n".join(result)
