from Task16.Models.PetModel import *

class PetController:
    @classmethod
    def add(cls,name,type,age,owner,vaccinated=False):
        PetModel.create(name=name,type=type,age=age,owner=owner,vaccinated=vaccinated)
    @classmethod
    def get(cls):
        return PetModel.select()
    @classmethod
    def vaccinated(cls,id):
        PetModel.update(vaccinated=True).where(PetModel.id == id).execute()
    @classmethod
    def list_owner(cls, owner):
        return PetModel.select().where(PetModel.owner==owner)
    @classmethod
    def pet_type(cls, type):
        return PetModel.select().where(PetModel.type==type)

if __name__ == "__main__":
    # PetController.add("Барсик","кот",3,"Мария")
    # PetController.add("Машка","кот",5,"Сергей")
    # PetController.add("Пушок","собака",5,"Сергей")
    for i in PetController.get():
        print(i.id,i.name,i.type,i.age,i.owner,i.vaccinated)
    PetController.vaccinated(1)
    for i in PetController.list_owner("Сергей"):
        print(i.id,i.name,i.type,i.age,i.owner,i.vaccinated)
    for i in PetController.pet_type("кот"):
        print(i.id,i.name,i.type,i.age,i.owner,i.vaccinated)