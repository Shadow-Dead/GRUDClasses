from Task16.Models.Pet import Pet

class PetController:
    """
    Класс для управления моделью Pet
    методы:
        добавить питомца,
        поставить прививку,
        вывести список "питомцы владельца",
        найти по типу
    """
    # CRUD
    obj = Pet() # создал объект класса
    @classmethod
    def add(cls,name,type,age,owner,vaccinated=False):
        cls.obj.pets = {
            "name": name,
            "type": type,
            "age": age,
            "owner": owner,
            "vaccinated": vaccinated
        }
        return True

    # Proxy method
    @classmethod
    def get(cls):
        return cls.obj.pets

    #поставить прививку
    @classmethod
    def vaccinated(cls,id):
        """
        поменять значения ключа vaccinated на True, по id питомца
        :return:
        """
        for i in cls.get():
            if i['id'] == id:
                i["vaccinated"] = True
                return i
        return f'Питомца с id {id} нет в базе данных'
    # вывести список "питомцы владельца"
    @classmethod
    def list_owner(cls,owner):
        list = []
        for i in cls.get():
            if i['owner'] == owner:
                list.append(i["name"])
        return list
    # найти по типу
    @classmethod
    def pet_type(cls, type):
        result = False
        for i in cls.get():
            if i["type"] == type:
                result = True
        return result
if __name__ == "__main__":
    # pet = PetController()
    print(PetController.get())
    print(PetController.add("Машка","кошка",5,"Мария"))
    print(PetController.get())
    print(PetController.vaccinated(2))
    print(PetController.vaccinated(3))
    print(PetController.get())
    print(PetController.list_owner("Мария"))
    print(PetController.pet_type("кот"))