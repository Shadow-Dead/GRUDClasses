from tkinter import *
from tkinter import ttk

from Task1.Controllers.NewTaskController import *
from Task1.Views.AddView import AddView


class TaskView(Tk):

    def __init__(self):
        super().__init__()
        self.title("Список задач")
        self.id=0
        self.geometry("1500x500")

        self.task = ttk.Entry()
        self.task.pack()
        # self.task.insert()

        self.status_lst = [False,True]
        self.status = ttk.Combobox(values=self.status_lst,state="readonly")
        self.status.pack()

        self.update = ttk.Button(text="Изменить",command=self.update)
        # self.update.pack(anchor="s")
        self.update.pack()

        def test(event):
            values = self.tree.item(self.tree.focus(), "values", )
            self.id = values[0]
            # print(values[0])
            self.task.delete(0,999)
            self.task.insert(0, values[1])
            self.status.set(values[2])

        # table
        self.frame_table = ttk.Frame(self, borderwidth=1, relief="solid", padding=[10, 10])
        self.frame_table.pack(anchor='center', fill="x", padx=10, pady=10)
        columns = ("id", "task", "status")
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill="both", expand=1)
        self.tree.bind("<ButtonRelease-1>", test)
        self.table()

        self.delete = ttk.Button(text="Удалить",command=self.delete)
        # self.delete.pack(anchor="sw")
        self.delete.pack()

        self.add = ttk.Button(text="Добавить",command=self.add)
        # self.add.pack(anchor="se")
        self.add.pack()


    def delete(self):
        values=self.tree.item(self.tree.focus(),"values",)
        TaskController.delete(values[0])
        self.table()

    def update(self):
        # values=self.tree.item(self.tree.focus(),"values",)
        # print(values[0])
        if self.id == 0:
            return None
        TaskController.update(self.id,task=self.task.get(),completed=self.status.current())
        self.task.get()
        self.table()
        return True

    def add(self):
        window = AddView()
    def table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        tasks = TaskController.get()
        lst = []
        for i in tasks:
            lst.append(
                (
                    i.id,  # id записи
                    i.task,  # значение записи
                    i.completed,
                )
            )
        self.tree.heading("id", text="#")
        self.tree.heading("task", text="Задача")
        self.tree.heading("status", text="Статус")
        for i in lst:
            self.tree.insert("","end",values=i)

if __name__ == "__main__":
    window = TaskView()
    window.mainloop()