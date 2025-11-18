from Task20.Models.ClientModel import *

class ClientController:
    @classmethod
    def add(cls,name,contact_person,phone,email,status):
        ClientModel.create(name=name,contact_person=contact_person,phone=phone,email=email,status=status)
    @classmethod
    def get(cls):
        return ClientModel.select()
    @classmethod
    def change_status(cls,id,status):
        ClientModel.update(status=status).where(ClientModel.id==id).execute()
    @classmethod
    def find_by_name(cls,name):
        return ClientModel.select().where(ClientModel.name==name)
    @classmethod
    def contacts(cls,person):
        return ClientModel.select().where(ClientModel.contact_person==person)

if __name__ == "__main__":
    # ClientController.add("ООО Ромашка","Ирина","+79998887766","info@romashka.ru","активный")
    # ClientController.add("ООО Бнал","Вася","+78005553535","info@obman.net","активный")
    for i in ClientController.get():
        print(i.id,i.name,i.contact_person,i.phone,i.email,i.status)
    ClientController.change_status(2,"не в сети")
    for i in ClientController.find_by_name("ООО Ромашка"):
        print(i.id,i.name,i.contact_person,i.phone,i.email,i.status)
    for i in ClientController.contacts("Вася"):
        print(i.id,i.name,i.contact_person,i.phone,i.email,i.status)