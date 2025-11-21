from tkinter import *
from tkinter import ttk

from Task1.Controllers.NewTaskController import *

class AddView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Моя задачи")
        self.geometry("500x150")

        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10,10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.frame_add, text="Добавить задачу")
        self.add_title.pack()

        # Task name
        self.task = ttk.Label(self.frame_add,text="Введите задачу")
        self.task.pack()
        self.input_task = ttk.Entry(self.frame_add)
        self.input_task.pack()

        # Combobox
        self.status_lst = ["Не сделано","Сделано"]
        self.status_lst_var = [0,1]
        self.status = ttk.Combobox(self.frame_add,textvariable=self.status_lst_var,values=self.status_lst,state="readonly")
        self.status.pack()

        # button
        self.send = ttk.Button(self.frame_add,text="Добавить",command=self.add)
        self.send.pack()



    def add(self):
        print(self.input_task.get())
        print(self.status.get())
        TaskController.add(
            task=self.input_task.get(),
            status=self.status.get(),
        )

if __name__ == "__main__":
    window = AddView()
    window.mainloop()