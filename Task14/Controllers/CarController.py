from Task14.Model.CarModel import *

class CarController:
    @classmethod
    def add(cls,brand,model,year,color,price):
        CarModel.create(brand=brand,model=model,year=year,color=color,price=price)
    @classmethod
    def get(cls):
        return CarModel.select()
    @classmethod
    def find_by_brand(cls,brand):
        return CarModel.select().where(CarModel.brand==brand)
    @classmethod
    def find_by_year(cls,year):
        return CarModel.select().where(CarModel.year==year)
    @classmethod
    def change_price(cls,id,price):
        CarModel.update(price=price).where(CarModel.id==id).execute()

if __name__ == "__main__":
    # CarController.add("BMW","E39",2001,"черный",1200000)
    # for i in CarController.get():
    #     print(i.id,i.brand,i.model,i.year,i.color,i.price)
    for i in CarController.find_by_brand("Toyota"):
        print(i.id,i.brand,i.model,i.year,i.color,i.price)
    for i in CarController.find_by_year(2001):
        print(i.id,i.brand,i.model,i.year,i.color,i.price)
    CarController.change_price(1,"1800000")