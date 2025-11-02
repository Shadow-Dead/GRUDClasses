class FinanceAccounting:
    def __init__(self):
        self.__expenses = [
            {"id": 1, "amount": 1500, "category": "Еда", "date": "2024-01-20","description": "Продукты"}
        ]
        self.__id = 2
    @property
    def expenses(self):
        return self.__expenses

    def add(self,amount,category,date,description):
        for i in self.__expenses:
            if i["description"] == description and i["date"] == date:
                return False
        self.__expenses.append(
                {
                    "id": self.__id,
                    "amount": amount,
                    "category": category,
                    "date": date,
                    "description": description
                }
        )
        self.__id+=1
        return True

    def amount_by_category(self,category):
        amount = 0
        for i in self.__expenses:
            if i['category'] == category:
                amount +=i['amount']
        return amount

    def spending_by_time(self,start_date,end_date):
        lst=[]
        for i in self.__expenses:
            if start_date <= i['date'] <= end_date:
                lst.append(i)
        return lst



if __name__ == "__main__":
    spending = FinanceAccounting()
    print(spending.add(5000,"Еда","2024-01-23","Ресторан"))
    print(spending.expenses)
    print(spending.amount_by_category("Еда"))
    print(spending.spending_by_time("2024-01-10","2024-01-20"))