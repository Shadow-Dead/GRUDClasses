from tkinter import *
from tkinter import ttk

from Task4.Controllers.NewFilmsController import *

class FilmsView(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1500x500")
        self.title("Таблица фильмов")
        self.id = 0

        def click(event):
            values = self.tree.item(self.tree.focus(), "values")
            self.id = values[0]
        self.base_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=10)
        self.base_frame.pack(anchor='center', fill='x',padx=10,pady=10)
        columns=('id','title','year','rating','watched')
        self.tree = ttk.Treeview(self.base_frame,columns=columns,show="headings")
        self.tree.pack(fill='both',expand=1)
        self.tree.bind("<ButtonRelease-1>", click)
        self.table()

    def table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        lst=[]
        for i in FilmsController.get():
            lst.append(
                (
                    i.id,
                    i.title,
                    i.year,
                    i.rating,
                    i.watched,
                )
            )
        self.tree.heading('id', text="№")
        self.tree.heading('title', text="Название")
        self.tree.heading('year', text="Год")
        self.tree.heading('rating', text="Рейтинг")
        self.tree.heading('watched', text="Просмотрена")
        for i in lst:
            self.tree.insert('','end',values=i)


if __name__ == "__main__":
    window = FilmsView()
    window.mainloop()