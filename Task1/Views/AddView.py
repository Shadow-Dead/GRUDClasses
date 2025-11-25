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
        self.input_task = ttk.Entry(self.frame_add)
        self.input_task.pack()

        # Combobox
        self.status_lst = [False, True]
        self.status = ttk.Combobox(self.frame_add, values=self.status_lst, state="readonly")
        self.status.pack()

        # button
        self.send = ttk.Button(self.frame_add,text="Добавить",command=self.add)
        self.send.pack()



    def add(self):
        if self.input_task.get() == "":
            self.input_task.focus()
            return None
        TaskController.add(
            task=self.input_task.get(),
            status=self.status.current(),
        )

if __name__ == "__main__":
    window = AddView()
    window.mainloop()