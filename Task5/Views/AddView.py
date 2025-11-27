from tkinter import *
from tkinter import ttk

from Task5.Controllers.NewStudentsController import *

class AddView(Tk):
    def __init__(self):
        super().__init__()

        self.base_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=10)
        self.base_frame.pack(anchor='center',fill='x',padx=10,pady=10)
        self.label = ttk.Label(self.base_frame,text="Добавить студента")
        self.label.pack()
        self.name_input = ttk.Entry(self.base_frame)
        self.name_input.pack()
        self.age_input = ttk.Entry(self.base_frame)
        self.age_input.pack()
        self.grade_cb = ttk.Combobox(self.base_frame,values=['A','B','C','D'],state="readonly")
        self.grade_cb.pack()
        self.grade_cb.set('A')
        self.submit = ttk.Button(self.base_frame,text="Добавить",command=self.submit)
        self.submit.pack()

    def submit(self):
        name = self.name_input.get()
        age = self.age_input.get()
        if name != '' or age != '':
            try:
                float(age)
            except ValueError:
                self.age_input.focus()
            else:
                StudentController.add(
                    name,
                    age,
                    self.grade_cb.get(),
                )
                self.destroy()
        else:
            self.name_input.focus()