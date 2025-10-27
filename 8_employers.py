class Employers:
    def __init__(self):
        self.__employees = [
            {"id": 1, "name": "Мария", "position": "Разработчик", "salary": 100000,"department": "IT"}
        ]
        self.__id=2
    @property
    def employees(self):
        return self.__employees

    def add(self,name,position,salary,department):
        for i in self.__employees:
            if i["name"] == name:
                return False
        self.__employees.append(
            {
                "id": 1,
                "name": "Мария",
                "position": "Разработчик",
                "salary": 100000,
                "department": "IT"
            }
        )
        self.__id += 1
        return True

    def new_salary(self,id,salary):
        for i in self.__employees:
            if i["id"] == id:
                i["salary"] = salary
                return True
        return False

    def employers_by_department(self,department):
        lst = []
        for i in self.__employees:
            if i["department"] == department:
                lst.append(i)
        return lst

    def fired(self,id):
        for i in self.__employees:
            if i["id"] == id:
                self.__employees.remove(i)
                return True
        return False

if __name__ == "__main__":
    employer = Employers()
    print(employer.add("Ivan","Developer",120000,"IT"))
    print(employer.add("Vasya","Manager",140000,"CEO"))
    print(employer.employees)
    print(employer.new_salary(2,110000))
    print(employer.employers_by_department("IT"))