class Project:
    def __init__(self):
        self.__projects = [
            {
                "id": 1,
                "name": "Веб-сайт",
                "status": "в процессе",
                "deadline": "2024-03-01",
                "priority": "высокий"
            }
        ]
        self.__id = 2
    @property
    def projects(self):
        return self.__projects
    @projects.setter
    def projects(self,dict):
        dict['id'] = self.__id
        self.__projects.append(dict)
        self.__id += 1

if __name__ == "__main__":
    proj = Project()
    print(proj.projects)
    proj.projects = {
        "id": 0,
        "name": "Приложение",
        "status": "в процессе",
        "deadline": "2024-08-01",
        "priority": "средний"
    }
    print(proj.projects)