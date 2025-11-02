from Task4.Models.Films import FilmsInfo

class FilmsController:
    obj = FilmsInfo()
    @classmethod
    def add(cls, title, year, rating, watched = False):
        cls.obj.movies ={
                "id":0,
                "title":title,
                "year":year,
                "rating":rating,
                "watched":watched
            }
        return True
    
    @classmethod
    def get(cls):
        return cls.obj.movies
    
    @classmethod
    def give_rating(cls,id,rating):
        for i in cls.get():
            if i["id"] == id:
                i["rating"] = rating
                return True
        return None

    @classmethod
    def find(cls,title):
        for i in cls.get():
            if i["title"] == title:
                return i
        return False

    @classmethod
    def not_watched(cls):
        not_watched = []
        for i in cls.get():
            if i["watched"] == False:
                not_watched.append(i)
        return not_watched
    
if __name__ == "__main__":
    print(FilmsController)
    print(FilmsController.add("Спасти рядового Райана", 1999, 9.3))
    print(FilmsController.get())
    print(FilmsController.find("Кресттный Отец"))
    print(FilmsController.give_rating(1,9.9))
    print(FilmsController.not_watched())