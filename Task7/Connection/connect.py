from peewee import *

mysql_db = MySQLDatabase(
    "RohtA84_library",
    user="RohtA84_library",
    password="321",
    host="10.11.13.118",
    port=3306,
)

if __name__ == "__main__":
    print(mysql_db.connect())