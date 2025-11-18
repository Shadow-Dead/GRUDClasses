from Task18.Models.EquipModel import *

class EquipController:
    @classmethod
    def add(cls,name,type,serial,status,user):
        EquipModel.create(name=name,type=type,serial=serial,status=status,user=user)
    @classmethod
    def get(cls):
        return EquipModel.select()
    @classmethod
    def change_status(cls,id,status):
        EquipModel.update(status=status).where(EquipModel.id==id).execute()
    @classmethod
    def find_by_user(cls,user):
        return EquipModel.select().where(EquipModel.user==user)
    @classmethod
    def delete(cls,id):
        EquipModel.delete_by_id(id)

if __name__ == "__main__":
    # EquipController.add("Ноутбук Dell","ноутбук","ABC123","в работе","Петр")
    # EquipController.add("Google Pixel","смартфон","GRG532","в работе","Саша")
    # EquipController.add("Apple Watch","смарт-часы","MLY076","выполнен","Петр")
    for i in EquipController.get():
        print(i.id,i.name,i.type,i.serial,i.status,i.user)
    EquipController.change_status(2,"выполнен")
    for i in EquipController.find_by_user(""):
        print(i.id,i.name,i.type,i.serial,i.status,i.user)
    # EquipController.delete(4)