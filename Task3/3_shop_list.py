from time import sleep


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

    def add(self,product,quantity):
        for i in self.__shopping_list:
            if i["product"] == product:
                return False
        self.__shopping_list.append(
            {
                "id":self.__id,
                "product":product,
                "quantity":quantity,
                "bought":False,
            }
        )
        return True

    def bought(self,id):
        for i in self.__shopping_list:
            if i["id"] == id:
                i["bought"] = True
        return False
    def list_not_bought(self):
        not_bought = []
        for i in self.__shopping_list:
            if i["bought"] == False:
                not_bought.append(i)
        return not_bought
    def delete(self,id):
        for i in self.__shopping_list:
            if i["id"] == id:
                self.__shopping_list.remove(i)
        return False

if __name__ == "__main__":
    shop=ShopList()
    print(shop.add("Мёд","3"))
    print(shop.add("Молоко","3"))
    print(shop.shopping_list)
    print(shop.bought(1))
    print(shop.list_not_bought())
    print(shop.delete(1))
    print(shop.shopping_list)
