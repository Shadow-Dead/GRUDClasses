from Task5.Models.StudentModel import *

class StudentController:
    @classmethod
    def add(cls,name,age,grade):
        Student.create(name=name,age=age,grade=grade)
    @classmethod
    def get(cls):
        return Student.select()
    @classmethod
    def change_grade(cls,id, grade):
        Student.update(grade=grade).where(Student.id == id).execute()
    @classmethod
    def find(cls,name):
        return Student.select().where(Student.name==name)
    @classmethod
    def delete(cls,id):
        Student.delete_by_id(id)

if __name__ == "__main__":
    # StudentController.add("Вася","18","B")
    # StudentController.add("Ваня","19","A")
    # StudentController.add("Тема","17","B")
    for i in StudentController.get():
        print(i.id,i.name,i.age,i.grade)
    StudentController.change_grade(1,"A")
    StudentController.find("Вася")
    StudentController.delete(3)