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
        self.base_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=[8,10])
        self.base_frame.pack(anchor='center', fill='x', padx=10, pady=10)
        self.add_movie_title = ttk.Label(self.base_frame, text= "Добавить фильм")
        self.add_movie_title.pack()
        # название фильма
        self.name_film = ttk.Label(self.base_frame, text="Введите название фильма")
        self.name_film.pack()
        self.name_film_input = ttk.Entry(self.base_frame)
        self.name_film_input.pack()
        # название фильма
        self.year_film = ttk.Label(self.base_frame, text="Введите год выпуска фильма")
        self.year_film.pack()
        self.year_film_input = ttk.Entry(self.base_frame)
        self.year_film_input.pack()
        # кнопка
        self.add_film_button = ttk.Button(self.base_frame,text="Добавить фильм",command=self.add_film)
        self.add_film_button.pack()

        # update rating
        self.rating_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=[8,10])
        self.rating_frame.pack(anchor='center', padx=10, pady=10)
        self.label = ttk.Label(self.rating_frame,text="Введите id фильма и рейтинг")
        self.label.pack()
        self.id_input = ttk.Entry(self.rating_frame)
        self.id_input.pack()
        self.rating_input = ttk.Entry(self.rating_frame)
        self.rating_input.pack()
        self.rating_button = ttk.Button(self.rating_frame,text="Изменить рейтинг", command=self.update_rating)
        self.rating_button.pack()

        # columns=('id','title','year','rating','watched')
        # self.tree = ttk.Treeview(self.base_frame,columns=columns,show="headings")
        # self.tree.pack(fill='both',expand=1)
        # self.tree.bind("<ButtonRealise-1>")
        # self.table()

    def update_rating(self):
        self.id = self.id_input.get()
        self.rating = self.rating_input.get()
        if not self.id or not self.rating:
            self.label['text'] = "Введите id фильма и рейтинг"
        elif not self.id.isdigit():
            self.label['text'] = "id фильма и рейтинг должны быть числами"
        try:
            float(self.rating)
        except ValueError:
            self.label['text'] = "Введите id фильма и рейтинг"
            return
        else:
            print("сделать потом")

    def add_film(self):
        if self.name_film_input.get() == "":
            self.name_film_input.focus()
            return None
        if self.year_film_input.get() == "":
            self.year_film_input.focus()
            return None
        FilmsController.add(
            title=self.name_film_input.get(),
            year=self.year_film_input.get(),
        )
        return True
if __name__ == "__main__":
    window = FilmsView()
    window.mainloop()