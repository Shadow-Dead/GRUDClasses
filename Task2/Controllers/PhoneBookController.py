from functools import cmp_to_key

from Task2.Models.PhoneBook import PhoneBook

class PhoneBookController:
    obj = PhoneBook()
    @classmethod
    def add(cls, name, phone, mail):
        cls.obj.contacts= {
                "id":0,
                "name":name,
                "phone":phone,
                "email":mail,
            }
    @classmethod
    def get(cls):
        return cls.obj.contacts
    @classmethod
    def find(cls,name):
        for i in cls.get():
            if i['name'] == name:
                return i
        return False
    @classmethod
    def update(cls, id, **kwargs):
        for i in cls.get():
            if i["id"] == id:
                i.update(kwargs)
                return True
        return None
    @classmethod
    def delete(cls, id):
        for i in cls.get():
            if i["id"] == id:
                cls.get().remove(i)
                return True
        return None

if __name__ == "__main__":
    print(PhoneBookController.get())
    print(PhoneBookController.add("Вася","+712345678","vasya@mail.ru"))
    print(PhoneBookController.get())
    print(PhoneBookController.find("Вася"))
    print(PhoneBookController.update(2,name="Vasya"))
    print(PhoneBookController.get())
    print(PhoneBookController.delete(2))
    print(PhoneBookController.get())
