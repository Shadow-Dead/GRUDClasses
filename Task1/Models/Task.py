class Task:
    def __init__(self):
        """
        Конструктор в котором задаю атрибуты список дел и идентификаторы дел
        список дел состоит из словарей
        """
        self.__tasks = [
            {"id": 1, "task": "Купить молоко", "completed": False},
            {"id": 2, "task": "Сделать уроки", "completed": True},
        ]  # Атрибут класса - список с двумя Делами
        self.__id = 3  # Атрибут класса - для автоматического создания id

    @property
    def tasks(self):
        return self.__tasks
    @tasks.setter
    def tasks(self,dict):
        dict["id"] = self.__id
        self.tasks.append(dict)
        self.__id += 1

if __name__ == "__main__":
    task = Task()
    print(task.tasks)
    task.tasks = {"id": 1, "task": "Ажумания", "completed": False}
    print(task.tasks)