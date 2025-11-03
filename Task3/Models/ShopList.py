class ShopList:
    def __init__(self):
        self.__shopping_list = [
            {"id":1,"product":"Хлеб","quantity":1,"bought":False,},
            {"id":2,"product":"Молоко","quantity":2,"bought":True,},
        ]
        self.__id=3
    @property
    def shopping_list(self):
        return self.__shopping_list
    @shopping_list.setter
    def shopping_list(self,dict):
        dict["id"] = self.__id
        self.shopping_list.append(dict)
        self.__id += 1

if __name__ == "__main__":
    lst = ShopList()
    print(lst.shopping_list)
    lst.shopping_list = {"id":1,"product":"Мёд","quantity":5,"bought":False,}
    print(lst.shopping_list)