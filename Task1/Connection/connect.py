from peewee import *

mysql_db = MySQLDatabase(
    "RohtA84_task1",
    user="RohtA84_task1",
    password="111111",
    host="10.11.13.118",
    port=3306,
)

if __name__ == "__main__":
    # проверить подключение
    print(mysql_db.connect())