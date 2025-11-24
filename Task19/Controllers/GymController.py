import datetime
from datetime import timedelta

from Task19.Models.GymModel import *

class GymController:
    @classmethod
    def add(cls,date,type,duration,calories,notes):
        GymModel.create(date=date,type=type,duration=duration,calories=calories,notes=notes)
    @classmethod
    def get(cls):
        return GymModel.select()
    @classmethod
    def week_statistic(cls):
        cal=0
        today = datetime.datetime.now().date()
        week = today - timedelta(days=7)
        for i in GymModel.select().where((week <= GymModel.date) & (GymModel.date <= today)):
            cal+=i.calories
        return cal
    @classmethod
    def find_by_type(cls,type):
        return GymModel.select().where(GymModel.type==type)
    @classmethod
    def total_duration(cls):
        duration = 0
        for i in GymModel.select():
            duration +=i.duration
        return duration

if __name__ == "__main__":
    # GymController.add("2025-11-14","отжимания",10,700,"отжимания лучника")

    for i in GymController.get():
        print(i.id,i.date,i.type,i.duration,i.calories,i.notes)
    print("========================")
    print(GymController.week_statistic())
    # for i in GymController.week_statistic():
        # print(i.id,i.date,i.type,i.duration,i.calories,i.notes)
    print("========================")
    for i in GymController.find_by_type('отжимания'):
        print(i.id,i.date,i.type,i.duration,i.calories,i.notes)
    print(GymController.total_duration())
