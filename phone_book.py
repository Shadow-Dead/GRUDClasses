class PhoneBook:
    def __init__(self):
        self.__contacts = [
            {"id":1,"name":"Иван","phone":"+79123456789","email":"ivan@mail.ru"},
        ]
        self.__id=2
    @property
    def contacts(self):
        return self.__contacts
    def add(self, name, phone, mail):
        self.__contacts.append(
            {
                "id":self.__id,
                "name":name,
                "phone":phone,
                "email":mail
            }
        )
        self.__id += 1
        return True
    def find(self, name):
        for i in self.contacts:
            if i["name"] == name:
                return i
        return None
    def update(self, id, **kwargs):
        for i in self.contacts:
            if i["id"] == id:
                i.update(kwargs)
                return True
        return None
    def delete(self, id):
        for i in self.contacts:
            if i["id"] == id:
                self.__contacts.remove(i)
                return True
        return None

if __name__ == "__main__":
    PBook = PhoneBook()
    print(PBook.add("Vasya","88005553535","VasyaPupkin@mail.ru"))
    print(PBook.contacts)
    print(PBook.find("Vasya"))
    print(PBook.update(2,name="Василий Пупкин"))
    print(PBook.delete(1))
    print(PBook.contacts)
