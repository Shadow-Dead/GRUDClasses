from Task4.Models.FilmsModel import *

class FilmsController:
    @classmethod
    def add(cls,title,year,rating=0.0,watched=False):
        FilmsInfo.create(title=title,year=year,rating=rating,watched=watched)
    @classmethod
    def get(cls):
        return FilmsInfo.select()
    @classmethod
    def give_rating(cls, id, rating):
        FilmsInfo.update({FilmsInfo.rating:rating}).where(FilmsInfo.id == id).execute()
    @classmethod
    def find(cls, title):
        return FilmsInfo.select().where(FilmsInfo.title == title)
    @classmethod
    def not_watched(cls):
        return FilmsInfo.select().where(FilmsInfo.watched == False)

if __name__ == "__main__":
    # print(FilmsController.add("Крестный Отец",1992,9.2,True))
    # print(FilmsController.add("Белое солнце пустыни",1969))
    # print(FilmsController.add("Крестный Отец",1972))

    # for i in FilmsController.get():
    #     print(i.id,i.title,i.year,i.rating,i.watched)
    #
    # for i in FilmsController.find("Крестный Отец"):
    #     print(i.id,i.title,i.year,i.rating,i.watched)

    for i in FilmsController.not_watched():
        print(i.id,i.title,i.year,i.rating,i.watched)