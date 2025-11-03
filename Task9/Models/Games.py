class GamesCollection:
    def __init__(self):
        self.__games = [
        {"id": 1, "title": "The Witcher 3", "genre": "RPG", "platform": "PC","completed": True}
        ]
        self.__id = 2

    @property
    def games(self):
        return self.__games

    @games.setter
    def games(self,dict):
        dict['id'] = self.__id
        self.__games.append(dict)
        self.__id += 1

if __name__ == "__main__":
    games = GamesCollection()
    print(games.games)
    games.games = {"id": 1, "title": "Battlefield 6", "genre": "FPS", "platform": "PC","completed": True}
    print(games.games)
