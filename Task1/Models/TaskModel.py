from Task1.Models.BaseModel import *


class Task(BaseModel):
    """
    Этот класс описывает таблицу task в базе данных
    """
    id = PrimaryKeyField() # первичный ключ в таблице
    task = CharField() # символьный тип данных (строка) в макс кол сим в 255
    completed = BooleanField(default=0) # поле Логическое, по умолчанию False

if __name__ == "__main__":
    mysql_db.create_tables([Task])

    # number = IntegerField()
    # date = DateField()
    # datetime = DateTimeField()
    # time = TimeField()