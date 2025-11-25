from tkinter import *
from tkinter import ttk

from Task3.Controllers.ShopController import *
from Task3.View.AddView import AddView


class ListView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Продуктовый магазин «ТрактирЪ»")
        self.geometry("1500x500")
        self.id=0
        self.mode = 0


        def click(event):
            values = self.tree.item(self.tree.focus(), "values")
            self.id = values[0]
        self.base_frame = ttk.Frame(self, borderwidth=1, relief="solid", padding=10)
        self.base_frame.pack(anchor='center', fill='x', padx=10, pady=10)
        columns = ("id", "product", "quantity" ,"bought")
        self.tree = ttk.Treeview(self.base_frame, columns=columns, show="headings")
        self.tree.pack(fill="both",expand=1)
        self.tree.bind("<ButtonRelease-1>", click)
        self.table()

        self.add = ttk.Button(self.base_frame,text="Добавить", command=self.add)
        self.add.pack(anchor='e')
        self.mode = ttk.Button(self.base_frame,text="Изменить режим", command=self.not_bought)
        self.mode.pack(anchor='e')

        self.buy = ttk.Button(text="Купить", command=self.buy)
        self.buy.pack()
        self.delete = ttk.Button(text="Удалить", command=self.delete)
        self.delete.pack()

    def table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        lst = []
        if self.mode == 1:
            mode = ShopController.get_not_bought()
        else:
            mode = ShopController.get()
        for i in mode:
            lst.append(
                (
                    i.id,
                    i.product,
                    i.quantity,
                    i.bought,
                )
            )
        self.tree.heading('id', text="#")
        self.tree.heading('product', text="Продукт")
        self.tree.heading('quantity', text="Количество")
        self.tree.heading('bought', text="Куплено")
        for i in lst:
            self.tree.insert('','end',values=i)

    def add(self):
        window = AddView()
    def not_bought(self):
        if self.mode == 0:
            self.mode = 1
        else:
            self.mode = 0
        self.table()
        return True
    def buy(self):
        if self.id == 0:
            return None
        ShopController.bought(self.id)
        self.table()
        return True
    def delete(self):
        if self.id == 0:
            return None
        ShopController.delete(self.id)
        self.table()
        return True

if __name__ == "__main__":
    window = ListView()
    window.mainloop()