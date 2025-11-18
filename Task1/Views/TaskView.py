import tkinter
from tkinter import *
from tkinter import ttk

from Task1.Controllers.NewTaskController import *

class TaskView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Моя задачи")
        self.geometry("500x800")

        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10,10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.frame_add, text="Добавить задачу")
        self.add_title.pack()

        self.task = ttk.Label(self.frame_add,text="Введите задачу")
        self.task.pack()
        self.unput_task = ttk.Entry(self.frame_add)
        self.unput_task.pack()

        self.status = tkinter.Listbox(self.frame_add,text="статус")
        self.status.pack()
        self.unput_status = ttk.Entry(self.frame_add)
        self.unput_status.pack()
if __name__ == "__main__":
    window = TaskView()
    window.mainloop()