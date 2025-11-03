from Task7.Models.Library import Library

class LibraryController:
    obj = Library()
    @classmethod
    def add(cls,title,author,year,read = False):
        for i in cls.obj.library:
            if i['title'] == title:
                return False
        cls.obj.library ={
                "id": 0,
                "title": title,
                "author": author,
                "year": year,
                "read": read
        }
        return True

    @classmethod
    def get(cls):
        return cls.obj.library

    @classmethod
    def read(cls, id):
        for i in cls.get():
            if i['id'] == id:
                i["read"] = True
                return True
        return False

    @classmethod
    def find_by_author(cls, author):
        lst = []
        for i in cls.get():
            if i["author"] == author:
                lst.append(i)
        return lst

    @classmethod
    def find_by_year(cls, year):
        lst = []
        for i in cls.get():
            if i["year"] == year:
                lst.append(i)
        return lst


if __name__ == "__main__":
    print(LibraryController.add("Преступление и наказание", "Достоевский", 1866))
    print(LibraryController.add("Война и мир", "Достоевский", 1866))
    print(LibraryController.get())
    print(LibraryController.read(3))
    print(LibraryController.find_by_author("Достоевский"))
    print(LibraryController.find_by_year(1866))