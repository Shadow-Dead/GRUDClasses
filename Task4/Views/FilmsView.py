from tkinter import *
from tkinter import ttk

from Task4.Controllers.NewFilmsController import *

class FilmsView(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1500x500")
        self.title("Таблица фильмов")
        self.id = 0
        self.mode = 0
        self.found = []

        self.base_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=10)
        self.base_frame.pack(anchor='center', fill='x',padx=10,pady=10)
        columns=('id','title','year','rating','watched')
        self.tree = ttk.Treeview(self.base_frame,columns=columns,show="headings")
        self.tree.pack(fill='both',expand=1)
        # self.tree.bind("<ButtonRelease-1>", click)
        self.tree.bind("<<TreeviewSelect>>", self.item_select)
        self.table()

        self.rating_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=10)
        self.rating_frame.pack(fill='x',padx=10,pady=10)
        self.rating_title = ttk.Label(self.rating_frame, text='(Название фильма)')
        self.rating_title.pack(anchor='w')
        self.rating_entry = ttk.Entry(self.rating_frame)
        self.rating_entry.pack(anchor='w')
        self.rating_submit = ttk.Button(self.rating_frame,text="Изменить рейтинг", command=self.change_rating)
        self.rating_submit.pack(anchor='w')

        self.find_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=10)
        self.find_frame.pack(fill='x',padx=10,pady=10)
        self.find_title = ttk.Label(self.rating_frame, text='Напишите название фильма')
        self.find_title.pack(anchor='w')
        self.find_entry = ttk.Entry(self.rating_frame)
        self.find_entry.pack(anchor='w')
        self.find_submit = ttk.Button(self.rating_frame,text="Найти", command=self.find)
        self.find_submit.pack(anchor='w')
        self.mode_button = ttk.Button(self.rating_frame,text="Непросмотренные", command=self.not_watched)
        self.mode_button.pack(anchor='w')

    def table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        lst=[]
        if self.mode == 1:
            mode = FilmsController.not_watched()
        elif self.mode == 2:
            mode = self.found
        else:
            mode = FilmsController.get()
        for i in mode:
            if i.watched:
                watched = 'Просмотрен'
            else:
                watched = 'НЕ Просмотрен'
            lst.append(
                (
                    i.id,
                    i.title,
                    i.year,
                    i.rating,
                    watched,
                )
            )
        self.tree.heading('id', text="№")
        self.tree.heading('title', text="Название")
        self.tree.heading('year', text="Год")
        self.tree.heading('rating', text="Рейтинг")
        self.tree.heading('watched', text="Просмотрена")
        for i in lst:
            self.tree.insert('','end',values=i)

    def item_select(self, event):
        values = self.tree.item(self.tree.focus(), "values")
        if values != '':
            self.id = values[0]
            self.rating_title["text"] = f'{values[1]} - {values[2]}'
            self.rating_entry.delete(0,"end")
            self.rating_entry.insert(0,values[3])

    def change_rating(self):
        if self.id == 0:
            return None
        FilmsController.give_rating(self.id,rating=self.rating_entry.get())
        self.table()
        return True

    def not_watched(self):
        if self.mode == 0:
            self.mode = 1
            self.mode_button['text'] = "Просмотренные"
        else:
            self.mode = 0
            self.mode_button['text'] = "Непросмотренные"
        self.table()

    def find(self):
        self.found = FilmsController.find(self.find_entry.get())
        self.mode = 2
        self.table()


if __name__ == "__main__":
    window = FilmsView()
    window.mainloop()