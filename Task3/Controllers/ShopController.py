from Task3.Models.ShopModel import *


class ShopController:

    @classmethod
    def add(cls,product,quantity):
        # вывзываем метод из peewee
        Shop.create(product=product,quantity=quantity,bought=False)
    @classmethod
    def update(cls,id,**kwargs):
        Shop.update(**kwargs).where(Shop.id == id).execute()

    #отметить купленным
    @classmethod
    def bought(cls,id):
        cls.update(id, bought = True)

    @classmethod
    def get(cls):
        return Shop.select() # список объектов из таблицы
    @classmethod
    def get_not_bought(cls):
        return Shop.select().where(Shop.bought == False)

    @classmethod
    def delete(cls,id):
        Shop.delete_by_id(id)

if __name__ == "__main__":
    # ShopController.add('хлеб',2)
    ShopController.update(1,product= 'батон',quantity= 4, bought = True)
    ShopController.bought(2)
    print(ShopController.get())
    for element in ShopController.get():
        print(element.id,element.product,element.quantity, element.bought)
    print('******************')
    for element in ShopController.get_not_bought():
        print(element.id, element.product, element.quantity, element.bought)

    ShopController.delete(4)