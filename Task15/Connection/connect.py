from peewee import *

mysql_db = MySQLDatabase(
    'RohtA84_order',
    user='RohtA84_order',
    password='24680',
    host='10.11.13.118',
    port=3306,
)

if __name__ == "__main__":
    print(mysql_db.connect())