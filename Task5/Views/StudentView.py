from tkinter import *
from tkinter import ttk

from Task5.Controllers.NewStudentsController import *

class StudentView(Tk):
    def __init__(self,student_id):
        super().__init__()
        self.student_id = student_id
        self.student = Student.get_by_id(self.student_id)

        self.title("Список студентов")
        self.geometry("500x140")

        self.base_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=10)
        self.base_frame.pack(anchor='center',fill='x',padx=10,pady=10)
        self.name_label = ttk.Label(self.base_frame,text=f"Студент - {self.student.name}, {self.student.age}")
        self.name_label.pack()
        self.grade_cb = ttk.Combobox(self.base_frame,values=['A','B','C','D'],state="readonly")
        self.grade_cb.pack()
        self.grade_cb.set(self.student.grade)
        self.change_button = ttk.Button(self.base_frame,text="Изменить",command=self.update)
        self.change_button.pack()
        self.delete_button = ttk.Button(self.base_frame,text="Удалить студента",command=self.delete)
        self.delete_button.pack()

    def update(self):
        if self.name_label != "":
            StudentController.change_grade(self.student_id,self.grade_cb.get())
            self.destroy()

    def delete(self):
        if self.name_label != "":
            StudentController.delete(self.student_id)
            self.destroy()
