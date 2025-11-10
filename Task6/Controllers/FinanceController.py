from Task6.Models.Finance import Finance

class FinanceController:
    obj = Finance()
    @classmethod
    def add(cls,amount,category,date,description):
        for i in cls.obj.expenses:
            if i["description"] == description and i["date"] == date:
                return False
        cls.obj.expenses ={
                "id": 0,
                "amount": amount,
                "category": category,
                "date": date,
                "description": description
        }
        return True

    @classmethod
    def get(cls):
        return cls.obj.expenses

    @classmethod
    def amount_by_category(cls, category):
        amount = 0
        for i in cls.get():
            if i['category'] == category:
                amount += i['amount']
        return amount

    @classmethod
    def spending_by_time(cls, start_date, end_date):
        lst = []
        for i in cls.get():
            if start_date <= i['date'] <= end_date:
                lst.append(i)
        return lst

if __name__ == "__main__":
    print(FinanceController.add(2000,"Еда","2024-01-13","Магазин"))
    print(FinanceController.get())
    print(FinanceController.amount_by_category("Еда"))
    print(FinanceController.spending_by_time("2024-01-10","2024-01-30"))