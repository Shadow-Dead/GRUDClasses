from Task15.Models.OrderModel import *

class OrderController:
    @classmethod
    def add(cls,customer,product,amount,status,order_date):
        OrderModel.create(customer=customer,product=product,amount=amount,status=status,order_date=order_date)