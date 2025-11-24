from tkinter import *
from tkinter import ttk

from Task3.Controllers.ShopController import *

class AddView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Добавление нового товара")
        self.geometry("300x180")
        self.add_frame=ttk.Frame(self,borderwidth=1, relief="solid", padding=10)
        self.add_frame.pack(anchor="center", fill='x', padx=10 ,pady=10)
        #fields
        self.product=ttk.Label(self.add_frame,text="Название")
        self.product.pack()
        self.product_input=ttk.Entry(self.add_frame)
        self.product_input.pack()
        self.quantity=ttk.Label(self.add_frame,text="Количество")
        self.quantity.pack()
        self.quantity_input=ttk.Entry(self.add_frame)
        self.quantity_input.pack()
        # self.bought=ttk.Label(self.add_frame,text="Куплено")
        # self.bought.pack()
        # self.bought_cb=ttk.Combobox(self.add_frame,values=[False,True],state="readonly")
        # self.bought_cb.pack()
        self.button=ttk.Button(self.add_frame,text="Добавить",command=self.add)
        self.button.pack()

    def add(self):
        ShopController.add(
            product=self.product_input.get(),
            quantity=self.quantity_input.get(),
        )
        return True

if __name__ == "__main__":
    window = AddView()
    window.mainloop()