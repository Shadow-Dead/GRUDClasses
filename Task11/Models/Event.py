class Event:
    def __init__(self):
        self.__events = [
            {
                "id": 1,
                "title": "Встреча",
                "date": "2024-02-15",
                "time": "14:00",
                "description": "С коллегами"
            }
        ]
        self.__id = 2
    @property
    def events(self):
        return self.__events
    @events.setter
    def events(self,dict):
        dict["id"] = self.__id
        self.__events.append(dict)
        self.__id += 1

if __name__ == "__main__":
    ev = Event()
    print(ev.events)
    ev.events = {
        "id": 1,
        "title": "Встреча",
        "date": "2024-02-18",
        "time": "18:00",
        "description": "С друзьями"
    }
    print(ev.events)
