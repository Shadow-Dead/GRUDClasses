import datetime

from Task12.Models.ProjectModel import *

class ProjectController:
    @classmethod
    def add(cls,name,status,deadline,priority):
        Project.create(name=name,status=status,deadline=deadline,priority=priority)
    @classmethod
    def get(cls):
        return Project.select()
    @classmethod
    def change_status(cls,id,status):
        Project.update(status=status).where(Project.id == id).execute()
    @classmethod
    def priority(cls):
        return Project.select().order_by(Project.priority)
    @classmethod
    def outdated(cls):
        return Project.select().where(Project.deadline < datetime.datetime.now())

if __name__ == "__main__":
    # ProjectController.add("Веб-сайт","В процессе","2025-11-11","средняя")
    # ProjectController.add("Приложение","В процессе","2025-12-25","низкая")
    for i in ProjectController.get():
        print(i.id,i.name,i.status,i.deadline,i.priority)
    ProjectController.change_status(1,"Завершен")
    print("Сортировка")
    for i in ProjectController.priority():
        print(i.id,i.name,i.status,i.deadline,i.priority)
    print("outdated:")
    for i in ProjectController.outdated():
        print(i.id,i.name,i.status,i.deadline,i.priority)