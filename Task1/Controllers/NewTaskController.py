from Task1.Models.TaskModel import Task

class TaskController:
    """
    Через модель Task подключаемся к базе данных таблице task
    и управляем данными
    Model.create(), for executing INSERT queries

    Model.save() and Model.update(), for executing UPDATE queries

    Model.delete_instance() and Model.delete(), for executing DELETE queries

    Model.select(), for executing SELECT queries
    """
    @classmethod
    def add(cls,task):
        Task.create(task=task)
    @classmethod
    def get(cls):
        return Task.select()
    @classmethod
    def show(cls,id):
        return Task.get_or_none(id=id) # работает с уникальными полями

    @classmethod
    def update(cls,id,**kwargs):
        Task.update(**kwargs).where(Task.id == id).execute()

    @classmethod
    def delete(cls,id):
        Task.delete_by_id(id)

if __name__ == "__main__":
    # TaskController.add("Отдохнуть")
    for task in TaskController.get():
        print(
            task.id, # id записи
            task.task, # значение записи
            task.completed, # состояние записи
        )
    TaskController.update(3,task="Работать",completed=True)
    # TaskController.delete(2)
    for task in TaskController.get():
        print(
            task.id, # id записи
            task.task, # значение записи
            task.completed, # состояние записи
        )