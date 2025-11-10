from Task2.Models.PhoneBookModel import PhoneBook

class PhoneBookController:
    @classmethod
    def add(cls,name,phone,email):
        PhoneBook.create(name=name,phone=phone,email=email)
    @classmethod
    def get(cls):
        return PhoneBook.select()
    @classmethod
    def show(cls,id):
        return PhoneBook.get_or_none(id)
    @classmethod
    def find(cls,name):
        return PhoneBook.select().where(PhoneBook.name == name)

if __name__ == "__main__":
    # print(PhoneBookController.add("Вася", "+712345678", "vasya@mail.ru"))
    print(PhoneBookController.get())
    for i in PhoneBookController.get():
        print(i.id,i.name,i.phone,i.email)
    print(PhoneBookController.show(1))
    for i in PhoneBookController.find("Вася"):
        print(i.id,i.name,i.phone,i.email)