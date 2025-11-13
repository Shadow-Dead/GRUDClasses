from Task13.Connection.connect import *

class BaseModel(Model):
    class Meta:
        database = mysql_db