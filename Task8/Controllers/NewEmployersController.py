from Task8.Models.Employers import *

class EmployersController:
    @classmethod
    def add(cls,name,position,salary,department):
        Employers.create(name=name,position=position,salary=salary,department=department)
    @classmethod
    def get(cls):
        return Employers.select()
    @classmethod
    def update(cls,id,**kwargs):
        Employers.update(**kwargs).where(Employers.id == id).execute()
    @classmethod
    def salary(cls,id,salary):
        # Employers.update(salary=salary).where(Employers.id == id).execute()
        cls.update(id, salary=salary)
    @classmethod
    def employers_by_department(cls,department):
        return Employers.select().where(Employers.department == department)
    @classmethod
    def fired(cls,id):
        Employers.delete_by_id(id)

if __name__ == "__main__":
    # EmployersController.add("Ivan","Developer",120000,"IT")
    # EmployersController.add("Vasya","Manager",140000,"CEO")
    for i in EmployersController.get():
        print(i.id,i.name,i.position,i.salary,i.department)
    EmployersController.salary(2,150000)
    for i in EmployersController.get():
        print(i.id,i.name,i.position,i.salary,i.department)
    for i in EmployersController.employers_by_department("IT"):
        print(i.id,i.name,i.position,i.salary,i.department)
    EmployersController.fired(1)
    for i in EmployersController.get():
        print(i.id,i.name,i.position,i.salary,i.department)
