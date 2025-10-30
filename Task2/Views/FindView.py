from tkinter import *
from tkinter import ttk

from Task2.Controllers.PhoneBookController import PhoneBookController

class FindView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Список контактов")
        self.geometry("500x200")

        # Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.frame_add, text="Поиск о имени")
        self.add_title.pack()
        # name
        self.name = ttk.Label(self.frame_add,text="Введите имя")
        self.name.pack()
        # input name
        self.input_name = ttk.Entry(self.frame_add)
        self.input_name.pack()

        # output
        self.button = ttk.Button(self.frame_add, text="Добавить контакт", command=self.find_by_name)
        self.button.pack()
        # contact
        self.contact = ttk.Label(self.frame_add,text="")
        self.contact.pack()

    def find_by_name(self):
        PhoneBookController.find(self.input_name.get())