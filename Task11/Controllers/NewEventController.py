from Task11.Models.EventModel import *

class EventController:
    @classmethod
    def add(cls,title,date,time,description):
        Event.create(title=title,date=date,time=time,description=description)
    @classmethod
    def get(cls):
        return Event.select()
    @classmethod
    def event_by_date(cls,date):
        return Event.select().where(Event.date==date)
    @classmethod
    def future_event(cls,date):
        return Event.select().where(Event.date>=date)

if __name__ == "__main__":
    # EventController.add('Встреча','2024-02-15','14:00','С коллегами')
    # EventController.add('Встреча','2024-02-18','18:00','С друзьями')
    for i in EventController.get():
        print(i.id,i.title,i.date,i.time,i.description)
    print("==========")
    for i in EventController.event_by_date('2024-02-15'):
        print(i.id,i.title,i.date,i.time,i.description)
    print("==========")
    for i in EventController.future_event('2024-02-17'):
        print(i.id,i.title,i.date,i.time,i.description)