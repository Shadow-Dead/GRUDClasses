from Task7.Models.LibraryModel import *

class LibraryController:
    @classmethod
    def add(cls,title,author,year,read=False):
        Library.create(title=title,author=author,year=year,read=read)
    @classmethod
    def get(cls):
        return Library.select()
    @classmethod
    def update(cls,id,**kwargs):
        Library.update(**kwargs).where(Library.id == id).execute()

    @classmethod
    def read(cls,id):
        cls.update(id, read=True)

    @classmethod
    def find_by_author(cls,author):
        return Library.select().where(Library.author == author)
    @classmethod
    def find_by_year(cls,year):
        return Library.select().where(Library.year == year)

if __name__ == "__main__":
    # LibraryController.add("Преступление и наказание","Достоевский","1866")
    for i in LibraryController.get():
        print(i.id,i.title,i.author,i.year,i.read)
    LibraryController.read(2)
    for i in LibraryController.find_by_author("Достоевский"):
        print(i.id,i.title,i.author,i.year,i.read)
    for i in LibraryController.find_by_year(1866):
        print(i.id,i.title,i.author,i.year,i.read)