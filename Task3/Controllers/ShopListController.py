from Task3.Models.ShopList import ShopList

class ShopListController:
    obj = ShopList()
    @classmethod
    def add(cls,product,quantity):
        cls.obj.shopping_list = {
            "id":0,
            "product":product,
            "quantity":quantity,
            "bought":False,
        }
        return True
    
    @classmethod
    def get(cls):
        return cls.obj.shopping_list
    
    @classmethod
    def bought(cls,id):
        for i in cls.get():
            if i["id"] == id:
                i["bought"] = True
        return False
    @classmethod
    def list_not_bought(cls):
        not_bought = []
        for i in cls.get():
            if i["bought"] == False:
                not_bought.append(i)
        return not_bought
    @classmethod
    def delete(cls,id):
        for i in cls.get():
            if i["id"] == id:
                cls.get().remove(i)
        return False
    
if __name__ == "__main__":
    print(ShopListController.get())
    ShopListController.add("Мёд","5")
    print(ShopListController.get())
    print(ShopListController.list_not_bought())
    print(ShopListController.delete(1))
    print(ShopListController.get())