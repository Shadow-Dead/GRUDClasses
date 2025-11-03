class GamesCollection:
    def __init__(self):
        self.__games = [
        {"id": 1, "title": "The Witcher 3", "genre": "RPG", "platform": "PC","completed": True}
        ]
        self.__id = 2

    @property
    def games(self):
        return self.__games

    def add(self, title, genre, platform):
        for i in self.__games:
            if i['title'] == title:
                return False
        self.__games.append(
            {
                "id": self.__id,
                "title": title,
                "genre": genre,
                "platform": platform,
                "completed": False
            }
        )
        self.__id += 1
        return True

    def completed(self, id):
        for i in self.__games:
            if i['id'] == id:
                i["completed"] = True
                return True
        return False

    def find_by_genre(self, genre):
        lst = []
        for i in self.__games:
            if i["genre"] == genre:
                lst.append(i)
        return lst

    def find_by_platform(self, platform):
        lst = []
        for i in self.__games:
            if i["platform"] == platform:
                lst.append(i)
        return lst

if __name__ == "__main__":
    games = GamesCollection()
    print(games.add("Battlefield 6", "FPS", "PC"))
    print(games.add("God of War", "RPG", "PS4"))
    print(games.games)
    print(games.completed(3))
    print(games.find_by_genre("RPG"))
    print(games.find_by_platform("PC"))