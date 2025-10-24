class FilmsInfo:
    def __init__(self):
        self.__movies = [
            {"id":1,"title":"Кресный Отец","year":1972,"rating":9.2,"watched":True},
        ]
        self.__id = 2
    @property
    def movies(self):
        return self.__movies

    def add(self, title, year, rating, watched):
        for i in self.__movies:
            if i["title"] == title:
                return None
        self.__movies.append(
            {
                "id":self.__id,
                 "title":title,
                 "year":year,
                "rating":rating,
                "watched":watched
            }
        )
        self.__id += 1
        return True

    def give_rating(self,id,rating):
        for i in self.__movies:
            if i["id"] == id:
                i["rating"] = rating
                return True
        return None

    def find(self,title):
        for i in self.__movies:
            if i["title"] == title:
                return i
        return False

    def not_watched(self):
        not_watched = []
        for i in self.__movies:
            if i["watched"] == False:
                not_watched.append(i)
        return not_watched

if __name__ == "__main__":
    films = FilmsInfo()
    print(films.add("Спасти рядового Райана",1999,9.3,True))
    print(films.add("Парк Юрского периода",1999,9.3,False))
    print(films.movies)
    print(films.find("Крестный Отец"))
    print(films.give_rating(1,9.9))
    print(films.not_watched())
    print(films.movies)