class FilmsInfo:
    def __init__(self):
        self.__movies = [
            {"id":1,"title":"Кресный Отец","year":1972,"rating":9.2,"watched":True},
        ]
        self.__id = 2
    @property
    def movies(self):
        return self.__movies
    @movies.setter
    def movies(self,dict):
        dict['id'] = self.__id
        self.movies.append(dict)
        self.__id += 1

if __name__ == "__main__":
    films = FilmsInfo()
    print(films.movies)
    films.movies = {"id":1,"title":"Спасти рядового Райана","year":1999,"rating":9.3,"watched":True}
    print(films.movies)