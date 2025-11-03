from Task8.Models.Employer import Employers

class EmployerController:
    obj = Employers()
    @classmethod
    def add(cls,name,position,salary,department):
        for i in cls.obj.employers:
            if i["name"] == name:
                return False
        cls.obj.employers={
                "id": 0,
                "name": name,
                "position": position,
                "salary": salary,
                "department": department
        }
        return True

    @classmethod
    def get(cls):
        return cls.obj.employers

    @classmethod
    def new_salary(cls,id,salary):
        for i in cls.get():
            if i["id"] == id:
                i["salary"] = salary
                return True
        return False

    @classmethod
    def employers_by_department(cls,department):
        lst = []
        for i in cls.get():
            if i["department"] == department:
                lst.append(i)
        return lst

    @classmethod
    def fired(cls,id):
        for i in cls.get():
            if i["id"] == id:
                cls.get().remove(i)
                return True
        return False

if __name__ == "__main__":
    print(EmployerController.add("Ivan","Developer",120000,"IT"))
    print(EmployerController.add("Vasya","Manager",140000,"CEO"))
    print(EmployerController.get())
    print(EmployerController.new_salary(2,110000))
    print(EmployerController.employers_by_department("IT"))