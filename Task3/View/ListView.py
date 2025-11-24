from tkinter import *
from tkinter import ttk

from Task3.Controllers.ShopController import *

class ListView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Продуктовый магазин «ТрактирЪ»")
        self.geometry("1500x500")

        self.base_frame = ttk.Frame(self, borderwidth=1, relief="solid", padding=10)
        self.base_frame.pack(anchor='center', fill='x', padx=10, pady=10)
        columns = ("id", "product", "quantity" ,"bought")
        self.tree = ttk.Treeview(self.base_frame, columns=columns, show="headings")
        self.tree.pack(fill="both",expand=1)
        self.tree.bind("<ButtonRelease-1>", self.click)
        self.table()
        self.buy = ttk.Button(text="Купить", command=self.buy)

    def table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        lst = []
        for i in ShopController.get():
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

    def click(self):
        values = self.tree.item(self.tree.focus(), "values")
    def buy(self):
        ShopController.bought()

if __name__ == "__main__":
    window = ListView()
    window.mainloop()