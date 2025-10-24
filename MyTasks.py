
class MyTasks:
    """
    : управлять списком задач с полями: id, задача, статус (выполнено/невыполнено)
    """
    def __init__(self):
        """
        Конструктор в котором задаю атрибуты список дел и идентификаторы дел
        список дел состоит из словарей
        """
        self.__tasks = [
            {"id":1,"task":"Купить молоко","completed":False},
            {"id":2,"task":"Сделать уроки","completed":True},
        ] # Атрибут класса - список с двумя Делами
        self.id = 3 # Атрибут класса - для автоматического создания id

    # Методы CRUD - Create, Read, Update, Delete
    def add(self,task):
        """
        Создаёт новое дело в виде словаря {"id":1,"task":"Купить молоко","completed":False}
        И добавляет в список атрибута self.tasks
        :Params:
            task(str): Дело в виде строки
            ud(int): создаётся автоматически с помощью атрибута self.id
            completed(boolean): автоматически присваиваеться False
        :Returns:
            True
        """
        self.tasks.append(
            {
                "id":self.id,
                "task":task,
                "completed":False
            }
        )
        self.id+=1 # Увеличить на 1. Следующий id будет на 1 больше
        return True
    # Показать всё
    @property
    def tasks(self):
        """
        Выводит информацию о делах
        :return: Список словарей с делами
        """
        return self.__tasks
    # Отметить выполненной - Update
    def completed(self,id):
        """
        Меняем значения completed на True у словаря с id == id из аргумента
        :param id: Словарь с данным id
        :return: Task - словарь
        """
        for i in self.tasks:
            if i['id'] == id:
                i['completed'] = True
                return i
        return f"Задачи с id {id} не существует."
    # Удалить
    def delete(self, id):
        for i in self.tasks:
            if i['id'] == id:
                self.__tasks.remove(i)
                return True
        return f"Задачи с id {id} не существует."
if __name__ == "__main__":
    task = MyTasks()
    print(task.add("Ажумания"))
    print(task.tasks)
    print(task.completed(3))
    print(task.completed(4))
    print(task.delete(2))
    print(task.tasks)
