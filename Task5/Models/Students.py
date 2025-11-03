class StudentsInfo:
    def __init__(self):
        self.__students = [
            {"id": 1, "name": "Анна", "age": 20, "grade": "A"},
            {"id": 2, "name": "Петр", "age": 19, "grade": "B"}
        ]
        self.__id = 3
    
    @property
    def students(self):
        return self.__students
    
    @students.setter
    def students(self, student_dict):
        student_dict['id'] = self.__id
        self.__students.append(student_dict)
        self.__id += 1

if __name__ == "__main__":
    students = StudentsInfo()
    print(students.students)
    students.students = {"name": "Иван", "age": 21, "grade": "C"}
    print(students.students)