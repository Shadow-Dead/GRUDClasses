from Task4.Models.BaseModel import *

class FilmsInfo(BaseModel):
    id = PrimaryKeyField()
    title = CharField()
    year = IntegerField()
    rating = FloatField(default=0.0)
    watched = BooleanField(default=False)

if __name__ == "__main__":
    mysql_db.create_tables([FilmsInfo])