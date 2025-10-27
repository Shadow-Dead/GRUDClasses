class StudentList:
    def __init__(self):
        self.__students = [
            {"id": 1, "name": "Анна", "age": 20, "grade": "A"},
            {"id": 2, "name": "Петр", "age": 19, "grade": "B"}
        ]
        self.__id = 3
    @property
    def students(self):
        return self.__students

    def add(self, name, age, grade):
        for i in self.__students:
            if i["name"]==name:
                return False
        self.__students.append(
            {
                "id": self.__id,
                "name": name,
                "age": age,
                "grade": grade
            },
        )
        self.__id += 1
        return True

    def change_grade(self,id,grade):
        for i in self.__students:
            if i["id"] == id:
                i["grade"] = grade
                return True
        return False

    def find_by_name(self,name):
        for i in self.__students:
            if i["name"] == name:
                return i
        return False

    def delete(self,id):
        for i in self.__students:
            if i["id"] == id:
                self.__students.remove(i)
                return True
        return False

if __name__ == "__main__":
    students = StudentList()
    print(students.add("Ivan",20,"A"))
    print(students.change_grade(3,"C"))
    print(students.students)
    print(students.find_by_name("Ivan"))
    print(students.delete(3))
    print(students.students)
