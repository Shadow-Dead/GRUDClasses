from Task2.Models.PhoneBookModel import PhoneBook

class PhoneBookController:
    @classmethod
    def add(cls,name,number,email):
        PhoneBook.create(name=name,number=number,email=email)
    @classmethod
    def get(cls):
        return PhoneBook.select()
    @classmethod
    def show(cls,id):
        return PhoneBook.get_or_none(id)
    @classmethod
    def find(cls,name):
        lst = []
        for i in PhoneBook.get():
            if i.name == name:
                lst.append({i.id,i.number,i.phone,i.email})

if __name__ == "__main__":
    print(PhoneBookController.add("Вася", "+712345678", "vasya@mail.ru"))