from tkinter import *
from tkinter import ttk

from Task6.Controllers.NewFinanceController import *

class TableView(Tk):
    def __init__(self):
        super().__init__()
        self.title('Финансы')
        self.base_frame = ttk.Frame(self,borderwidth=1,relief='solid',padding=10)
        self.base_frame.pack(anchor='center',fill='x',padx=10,pady=10)
        self.mode = 0
        self.table_mode = ()

        self.amount_label = ttk.Label(self.base_frame,text="(Название категории)")
        self.amount_label.pack()
        self.amount_sum = ttk.Label(self.base_frame,background="#ffffff",width=30)
        self.amount_sum.pack()

        self.table_label = ttk.Label(self.base_frame)
        self.table_label.pack()
        columns=('id','amount','category','date','description')
        self.tree = ttk.Treeview(self.base_frame,columns=columns,show='headings')
        self.tree.pack(fill='both',expand=1)
        self.tree.bind("<<TreeviewSelect>>",self.select)
        self.table()

        self.time_label = ttk.Label(self.base_frame,text="Напишите дату начало и конца")
        self.time_label.pack()
        self.start_time_entry = ttk.Entry(self.base_frame)
        self.start_time_entry.pack()
        self.end_time_entry = ttk.Entry(self.base_frame)
        self.end_time_entry.pack()
        self.time_button = ttk.Button(self.base_frame,text="Вывести",command=self.spend_by_time)
        self.time_button.pack()

    def table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        lst=[]
        table_mode = FinanceController.get()
        for i in table_mode:
            lst.append(
                (
                    i.id,
                    i.amount,
                    i.category,
                    i.date,
                    i.description,
                )
            )
        self.tree.heading('id',text='#')
        self.tree.heading('amount',text='Количество')
        self.tree.heading('category',text='Категория')
        self.tree.heading('date',text='Дата')
        self.tree.heading('description',text='Описание')
        for i in lst:
            self.tree.insert('','end',values=i)

    def select(self,event):
        values = self.tree.item(self.tree.focus(),'values')
        if values != "":
            print(values)
            self.amount_label['text']=values[2]
            self.amount_sum['text']=FinanceController.amount_by_category(values[2])

    def spend_by_time(self):
        start = self.start_time_entry.get()
        end = self.end_time_entry.get()
        if start != "" or end != "":
            self.table_label['text']=f"Сумма трат за {start} - {end}"
            self.table_mode=FinanceController.spending_by_time(start,end)
            self.mode = 1
            self.table()

if __name__ == "__main__":
    window = TableView()
    window.mainloop()