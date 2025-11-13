from Task6.Models.FinanceModel import *

class FinanceController(BaseModel):
    @classmethod
    def add(cls,amount,category,date,description):
        Finance.create(amount=amount,category=category,date=date,description=description)
    @classmethod
    def get(cls):
        return Finance.select()
    @classmethod
    def amount_by_category(cls,category):
        amount = 0
        for i in Finance.select().where(Finance.category == category):
            amount += i.amount
        return amount
    @classmethod
    def spending_by_time(cls, start_date, end_date):
        lst=[]
        for i in Finance.select():
            if start_date <= str(i.date) <= end_date:
                print(start_date <= str(i.date))
                l={i.id,i.amount,i.category,i.date,i.description}
                lst.append(l)
        return lst

if __name__ == "__main__":
    # FinanceController.add(2000,"Еда","2024-01-13","Магазин")
    for i in FinanceController.get():
        print(i.id,i.amount,i.category,i.date,i.description)
    print(FinanceController.amount_by_category("Еда"))
    print(FinanceController.spending_by_time("2024-01-15","2024-01-25"))