class Library:
    def __init__(self):
        self.__library = [
            {"id": 1, "title": "1984", "author": "Оруэлл", "year": 1949, "read": False}
        ]
        self.__id=2
    @property
    def library(self):
        return self.__library

    def add(self,title,author,year):
        for i in self.__library:
            if i['title'] == title:
                return False
        self.__library.append(
            {
                "id": self.__id,
                "title": title,
                "author": author,
                "year": year,
                "read": False
            }
        )
        self.__id += 1
        return True

    def read(self,id):
        for i in self.__library:
            if i['id'] == id:
                i["read"]=True
                return True
        return False

    def find_by_author(self,author):
        lst = []
        for i in self.__library:
            if i["author"] == author:
                lst.append(i)
        return lst

    def find_by_year(self,year):
        lst = []
        for i in self.__library:
            if i["year"] == year:
                lst.append(i)
        return lst

if __name__ == "__main__":
    lib = Library()
    print(lib.add("Преступление и наказание", "Достоевский", 1866))
    print(lib.add("Война и мир", "Достоевский", 1866))
    print(lib.library)
    print(lib.read(3))
    print(lib.find_by_author("Достоевский"))
    print(lib.find_by_year(1866))