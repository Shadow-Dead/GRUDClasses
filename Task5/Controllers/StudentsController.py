from Task5.Models.Students import StudentsInfo

class StudentsController:
    obj = StudentsInfo()
    
    @classmethod
    def add(cls, name, age, grade):
        for student in cls.get():
            if student["name"] == name:
                return False
        
        cls.obj.students = {
            "name": name,
            "age": age,
            "grade": grade
        }
        return True
    
    @classmethod
    def get(cls):
        return cls.obj.students
    
    @classmethod
    def change_grade(cls, id, grade):
        for student in cls.get():
            if student["id"] == id:
                student["grade"] = grade
                return True
        return False
    
    @classmethod
    def find_by_name(cls, name):
        for student in cls.get():
            if student["name"] == name:
                return student
        return False
    
    @classmethod
    def delete(cls, id):
        for student in cls.get():
            if student["id"] == id:
                cls.obj.students.remove(student)
                return True
        return False

if __name__ == "__main__":
    print(StudentsController.add("Иван", 20, "A"))
    print(StudentsController.get())
    print(StudentsController.find_by_name("Иван"))
    print(StudentsController.change_grade(3, "B"))
    print(StudentsController.delete(3))
    print(StudentsController.get())