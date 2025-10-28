
class Pet:
    """
    Класс для описания питомцев ветеринарной клиники

    """
    def __init__(self):
        self.__pets= [
            {"id": 1, "name": "Барсик", "type": "кот", "age": 3, "owner": "Мария","vaccinated": True}
        ] #список питомцев
        self.__id = 2
    @property
    def pets(self):
        return self.__pets
    @pets.setter
    def pets(self,dict):
        dict['id'] = self.__id
        self.pets.append(dict)
        self.__id += 1
    # def pets(self,name,type,age,owner,vaccinated=False):
    #     self.pets.append(
    #         {
    #             "id": self.__id,
    #             "name": name,
    #             "type": type,
    #             "age": age,
    #             "owner": owner,
    #             "vaccinated": vaccinated
    #         }
    #     )
    #     self.__id += 1

if __name__ == "__main__":
    pet = Pet()
    print(pet.pets)
    pet.pets = {"id": 1, "name": "Барсик", "type": "кот", "age": 3, "owner": "Мария","vaccinated": True}
    print(pet.pets)