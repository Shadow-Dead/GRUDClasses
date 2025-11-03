from Task9.Models.Games import GamesCollection

class GamesController:
    obj = GamesCollection()
    @classmethod
    def add(cls, title, genre, platform):
        for i in cls.obj.games:
            if i['title'] == title:
                return False
        cls.obj.games={
                "id": 0,
                "title": title,
                "genre": genre,
                "platform": platform,
                "completed": False
        }
        return True

    @classmethod
    def get(cls):
        return cls.obj.games

    @classmethod
    def completed(cls, id):
        for i in cls.get():
            if i['id'] == id:
                i["completed"] = True
                return True
        return False

    @classmethod
    def find_by_genre(cls, genre):
        lst = []
        for i in cls.get():
            if i["genre"] == genre:
                lst.append(i)
        return lst

    @classmethod
    def find_by_platform(cls, platform):
        lst = []
        for i in cls.get():
            if i["platform"] == platform:
                lst.append(i)
        return lst

if __name__ == "__main__":
    print(GamesController.add("Battlefield 6", "FPS", "PC"))
    print(GamesController.add("God of War", "RPG", "PS4"))
    print(GamesController.get())
    print(GamesController.completed(3))
    print(GamesController.find_by_genre("RPG"))
    print(GamesController.find_by_platform("PC"))