from peewee import *

mysql_db = MySQLDatabase(
    "RohtA84_client",
    user="RohtA84_client",
    password="255288",
    host="10.11.13.118",
    port=3306,
)

if __name__ == "__main__":
    print(mysql_db.connect())