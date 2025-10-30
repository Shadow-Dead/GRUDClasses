from tkinter import *
from tkinter import ttk

from Task2.Controllers.PhoneBookController import PhoneBookController
from Task2.Views.FindView import FindView


class PhoneBookView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Список контактов")
        self.geometry("1500x500")

        # Добавить
        self.frame_add = ttk.Frame(self,borderwidth=1,relief=SOLID,padding=[10,10])
        self.frame_add.pack(anchor='center',fill=X,padx=10,pady=10)
        self.add_title = ttk.Label(self.frame_add,text="Добавить контакт")
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.frame_add,text="Введите имя")
        self.name.pack()
        # input name
        self.input_name = ttk.Entry(self.frame_add)
        self.input_name.pack()

        # phone
        self.phone = ttk.Label(self.frame_add,text="Введите телефон")
        self.phone.pack()
        # input phone
        self.input_phone = ttk.Entry(self.frame_add)
        self.input_phone.pack()

        # mail
        self.mail = ttk.Label(self.frame_add,text="Введите эл почту")
        self.mail.pack()
        # input mail
        self.input_mail = ttk.Entry(self.frame_add)
        self.input_mail.pack()

        # output
        self.Cbutton = ttk.Button(self.frame_add,text="Добавить контакт",command=self.add_contact)
        self.Cbutton.pack()
        # find
        self.Fbutton = ttk.Button(self.frame_add,text="Найти контакт",command=self.find_contact)
        self.Fbutton.pack()

        # table
        self.frame_table = ttk.Frame(self,borderwidth=1,relief=SOLID,padding=[10,10])
        self.frame_table.pack(anchor='center',fill=X,padx=10,pady=10)
        columns = ("id","name","phone","mail")
        self.tree = ttk.Treeview(self.frame_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH,expand=1)
        self.table()

    def table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        contacts = PhoneBookController.get()
        lst = []
        for i in contacts:
            lst.append(
                (
                    i["id"],
                    i["name"],
                    i["phone"],
                    i["email"],
                )
            )
        self.tree.heading('id', text="#")
        self.tree.heading('name', text="Имя")
        self.tree.heading('phone', text="Телефон")
        self.tree.heading('mail', text="Эл почта")
        for i in lst:
            self.tree.insert("",END,values=i)

    def add_contact(self):
        PhoneBookController.add(
            name=self.input_name.get(),
            phone=self.input_phone.get(),
            mail=self.input_mail.get(),
        )
        self.table()

    def find_contact(self):
        window = FindView()