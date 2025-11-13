from Task1.Models.Task import Task
class TaskControllers:
    obj = Task()
    @classmethod
    def add(cls,task,completed = False):
        cls.obj.tasks = {
            "task": task,
            "completed": completed
        }
        return True

    @classmethod
    def get(cls):
        return cls.obj.tasks

    @classmethod
    def __main__(cls,id):
        for i in cls.get():
            if i['id'] == id:
                i["completed"] = True
                return i
        return (f'Задачи с id {id} нет в базе данных')

    @classmethod
    def delete(cls,id):
        for i in cls.get():
            if i['id'] == id:
                cls.get().remove(i)
                return True
        return f'Задачи с id {id} нет в базе данных'

if __name__ == "__main__":
    print(TaskControllers.get())
    print(TaskControllers.add("Ажумания"))
    print(TaskControllers.completed(3))
    print(TaskControllers.delete(2))
    print(TaskControllers.get())
