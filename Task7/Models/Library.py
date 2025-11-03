class Library:
    def __init__(self):
        self.__library = [
            {"id": 1, "title": "1984", "author": "Оруэлл", "year": 1949, "read": False}
        ]
        self.__id=2
    @property
    def library(self):
        return self.__library
    @library.setter
    def library(self, dict):
        dict['id'] = self.__id
        self.__library.append(dict)
        self.__id += 1

if __name__ == "__main__":
    lib = Library()
    print(lib.library)
    lib.library = {"id": 1, "title": "Преступление и наказание", "author": "Достоевский", "year": 1866, "read": False}
    print(lib.library)