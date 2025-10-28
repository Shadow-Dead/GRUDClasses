class PhoneBook:
    def __init__(self):
        self.__contacts = [
            {"id":1,"name":"Иван","phone":"+79123456789","email":"ivan@mail.ru"},
        ]
        self.__id=2
    @property
    def contacts(self):
        return self.__contacts
    @contacts.setter
    def contacts(self,dict):
        dict['id'] = self.__id
        self.contacts.append(dict)
        self.__id +=1

if __name__ == "__main__":
    pb = PhoneBook()
    print(pb.contacts)
    pb.contacts = {"id":1,"name":"Вася","phone":"+7646164363","email":"vasya@mail.ru"}
    print(pb.contacts)