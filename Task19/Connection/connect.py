from peewee import *

mysql_db = MySQLDatabase(
    "RohtA84_training",
    user="RohtA84_training",
    password="asd",
    host="10.11.13.118",
    port=3306,
)

if __name__ == "__main__":
    print(mysql_db.connect())