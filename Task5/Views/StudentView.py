from tkinter import *
from tkinter import ttk

from Task5.Controllers.NewStudentsController import *

class StudentView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Список студентов")
        self.geometry("1200x600")
        
        self.base_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=10)
        self.base_frame.pack(anchor='center', fill='x', padx=10, pady=10)
        columns = ('id','name','age','grade')
        self.tree = ttk.Treeview(self.base_frame,columns=columns,show="headings")
        self.tree.pack(fill='both',expand=1)
        self.table()

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

if __name__ == "__main__":
    window = StudentView()
    window.mainloop()