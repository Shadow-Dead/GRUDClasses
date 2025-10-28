from tkinter import *
from tkinter import ttk

from Task16.Controllers.PetConroller import PetController


class PetView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Учёт домашних животных")
        self.geometry("1500x500")

        # раздел Добавить
        self.frame_add = ttk.Frame(self,borderwidth=1,relief=SOLID,padding=[10,10])
        self.frame_add.pack(anchor='center',fill=X,padx=10,pady=10)
        self.add_title = ttk.Label(self.frame_add,text="Добавить питомца")
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.frame_add,text="Введите имя питомца")
        self.name.pack()
        # Окно ввода данных
        self.input_name = ttk.Entry(self.frame_add)
        self.input_name.pack()

        # type
        self.type = ttk.Label(self.frame_add,text="Введите тип питомца")
        self.type.pack()
        # Окно ввода данных
        self.input_type = ttk.Entry(self.frame_add)
        self.input_type.pack()

        # age
        self.age = ttk.Label(self.frame_add,text="Введите возраст питомца")
        self.age.pack()
        # Окно ввода данных
        self.input_age = ttk.Entry(self.frame_add)
        self.input_age.pack()

        # owner
        self.owner = ttk.Label(self.frame_add,text="Введите имя хозяина питомца")
        self.owner.pack()
        # Окно ввода данных
        self.input_owner = ttk.Entry(self.frame_add)
        self.input_owner.pack()

        self.add_button = ttk.Button(self.frame_add,text="Добавить",command=self.add_pet)
        self.add_button.pack()
        # вывод
        # Таблица
        self.frame_table = ttk.Frame(self,borderwidth=1,relief=SOLID,padding=[10,10])
        self.frame_table.pack(anchor='center',fill=X,padx=10,pady=10)
        columns = ('id','name','type','age','owner','vaccinated')
        self.tree = ttk.Treeview(self.frame_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH,expand=1)
        self.table()


    def table(self):
        # очистить тиблицу
        for i in self.tree.get_children():
            self.tree.delete(i)
        # списоку животных
        pets = PetController.get()
        list_pets = [] # сюда будут передаваться кортежи с описанием животных
        for pet in pets:
            list_pets.append(
                (
                    pet['id'],
                    pet['name'],
                    pet['type'],
                    pet['age'],
                    pet['owner'],
                    pet['vaccinated'],
                )
            )
        # перевести название столбцев на русский
        self.tree.heading("id", text="#")
        self.tree.heading("name", text="Имя")
        self.tree.heading("type", text="Тип")
        self.tree.heading("age", text="Возраст")
        self.tree.heading("owner", text="Хозяин")
        self.tree.heading("vaccinated", text="Вакцинация")
        for pet in list_pets:
            self.tree.insert("",END,values=pet)
    def add_pet(self):
        PetController.add(
            name=self.input_name.get(),
            type=self.input_type.get(),
            age=self.input_age.get(),
            owner=self.input_owner.get(),
        )
        self.table()