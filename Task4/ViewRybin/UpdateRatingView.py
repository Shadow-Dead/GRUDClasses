from tkinter import *
from tkinter import ttk

from Task4.Controllers.NewFilmsController import *

class FilmsView(Tk):
    def __init__(self):
        super().__init__()
        # конфигурация окна
        self.title("Таблица фильмов")
        self.geometry("800x500")
        # добавить фильм