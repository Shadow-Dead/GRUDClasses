from tkinter import *
from tkinter import ttk

from Task5.Controllers.NewStudentsController import *
from Task5.Views.StudentView import StudentView
from Task5.Views.AddView import AddView


class TableView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Список студентов")
        self.geometry("1200x340")
        
        self.base_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=10)
        self.base_frame.pack(anchor='center', fill='x', padx=10, pady=10)
        columns = ('id','name','age','grade')
        self.tree = ttk.Treeview(self.base_frame,columns=columns,show="headings")
        self.tree.pack(fill='both',expand=1)
        self.tree.bind("<Double-ButtonRelease-1>",self.open)
        self.tree.bind("<FocusIn>",self.update)
        self.table()

        self.add_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=10)
        self.add_frame.pack(anchor='e',fill='y',padx=10,pady=10)
        self.add_button = ttk.Button(self.add_frame,text="Добавить студента",command=self.add)
        self.add_button.pack(anchor="e")

    def table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        lst = []
        for i in StudentController.get():
            lst.append(
                (
                    i.id,
                    i.name,
                    i.age,
                    i.grade,
                )
            )
        self.tree.heading("id", text="№")
        self.tree.heading("name", text="Имя")
        self.tree.heading("age", text="Возраст")
        self.tree.heading("grade", text="Оценка")

        for i in lst:
            self.tree.insert('','end',values=i)

    def open(self, event):
        values = self.tree.item(self.tree.focus(),"values")
        if values != "":
            print(values[0])
            window_update = StudentView(values[0])

    def update(self,event):
        self.table()

    def add(self):
        window_add = AddView()

if __name__ == "__main__":
    window = TableView()
    window.mainloop()