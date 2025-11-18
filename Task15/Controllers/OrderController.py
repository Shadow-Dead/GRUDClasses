from Task15.Models.OrderModel import *

class OrderController:
    @classmethod
    def add(cls,customer,product,amount,status,order_date):
        OrderModel.create(customer=customer,product=product,amount=amount,status=status,order_date=order_date)
    @classmethod
    def get(cls):
        return OrderModel.select()
    @classmethod
    def change_status(cls,id,status):
        OrderModel.update(status=status).where(OrderModel.id==id).execute()
    @classmethod
    def customer_order(cls,customer):
        return OrderModel.select().where(OrderModel.customer==customer)
    @classmethod
    def cancel_order(cls,id):
        OrderModel.delete_by_id(id)

if __name__ == "__main__":
    # OrderController.add("Иван","Ноутбук",1,"доставляеться","2024-01-20")
    # OrderController.add("Сергей","Смартфон",3,"доставляеться","2024-01-23")
    # OrderController.add("Иван","Смарт-часы",10,"доставлен","2024-01-12")
    for i in OrderController.get():
        print(i.id,i.customer,i.product,i.amount,i.status,i.order_date)
    OrderController.change_status(1,"доставлен")
    for i in OrderController.customer_order("Иван"):
        print(i.id,i.customer,i.product,i.amount,i.status,i.order_date)
    OrderController.cancel_order(4)