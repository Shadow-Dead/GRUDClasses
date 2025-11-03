class Employers:
    def __init__(self):
        self.__employers = [
            {"id": 1, "name": "Мария", "position": "Разработчик", "salary": 100000,"department": "IT"}
        ]
        self.__id=2
    @property
    def employers(self):
        return self.__employers

    @employers.setter
    def employers(self,dict):
        dict['id'] = self.__id
        self.employers.append(dict)
        self.__id += 1

if __name__ == "__main__":
    employer = Employers()
    print(employer.employers)
    employer.employers = {"id": 1, "name": "Ivan", "position": "Developer", "salary": 120000,"department": "IT"}
    print(employer.employers)