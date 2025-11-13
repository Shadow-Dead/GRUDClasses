from Task10.Models.RationModel import *

class RationController:
    @classmethod
    def add(cls,meal,food,calories,time):
        Ration.create(meal=meal,food=food,calories=calories,time=time)
    @classmethod
    def get(cls):
        return Ration.select()
    @classmethod
    def cal_by_day(cls):
        calories = 0
        for i in Ration.select():
            calories += i.calories
        return calories
    @classmethod
    def find_by_time(cls,time):
        return Ration.select().where(Ration.time == time)

if __name__ == "__main__":
    # RationController.add("Завтрак","Овсянка",300,"08:00")
    # RationController.add("Обед","Гречка с мясом",100,"12:00")
    for i in RationController.get():
        print(i.id,i.meal,i.food,i.calories,i.time)
    print(RationController.cal_by_day())
    for i in RationController.find_by_time("08:00"):
        print(i.id,i.meal,i.food,i.calories,i.time)