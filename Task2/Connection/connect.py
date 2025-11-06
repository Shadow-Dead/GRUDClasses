from peewee import *

from Task1.Connection.connect import mysql_db

mysql_db = MySQLDatabase(
    "RohtA84_PhoneBook",
    user="RohtA84_task2",
    password="222",
    host="10.11.13.118",
    port=3306,
)

if __name__ == "__main__":
    # проверить подключение
    print(mysql_db.connect())