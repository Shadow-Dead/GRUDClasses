class Finance:
    def __init__(self):
        self.__expenses = [
            {"id": 1, "amount": 1500, "category": "Еда", "date": "2024-01-20", "description": "Продукты"}
        ]
        self.__id = 2

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, dict):
        dict['id'] = self.__id
        self.expenses.append(dict)
        self.__id += 1

if __name__ == "__main__":
    finance = Finance()
    print(finance.expenses)
    finance.expenses = {"id": 1, "amount": 1500, "category": "Еда", "date": "2024-01-23", "description": "Ресторан"}
    print(finance.expenses)