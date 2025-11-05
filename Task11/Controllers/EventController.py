from Task11.Models.Event import Event

class EventController:
    obj = Event()
    @classmethod
    def get(cls):
        return cls.obj.events
    @classmethod
    def add(cls,title,date,time,description):
        for i in cls.get():
            if i['title'] == title and i["description"] == description:
                return False
        cls.obj.events ={
            "id": 0,
            "title": title,
            "date": date,
            "time": time,
            "description": description
        }
        return True
    @classmethod
    def event_by_date(cls,date):
        lst = []
        for i in cls.get():
            if i['date'] == date:
                lst.append(i)
        return lst
    @classmethod
    def future_event(cls,date):
        lst = []
        for i in cls.get():
            if i['date'] >= date:
                lst.append(i)
        return lst

if __name__ == "__main__":
    print(EventController.get())
    print(EventController.add('Встреча','2024-02-18','18:00','С друзьями'))
    print(EventController.get())
    print(EventController.event_by_date("2024-02-15"))
    print(EventController.future_event("2024-02-14"))
