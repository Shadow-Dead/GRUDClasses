from peewee import *

mysql_db = MySQLDatabase(
    "RohtA84_pets",
    user="RohtA84_pets",
    password="1010",
    host="10.11.13.118",
    port=3306,
)

if __name__ == "__main__":
    print(mysql_db.connect())