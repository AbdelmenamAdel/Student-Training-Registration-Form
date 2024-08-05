import sqlite3
from tkinter import *
from tkinter.ttk import Combobox, Treeview, Style
from admin_view import AdminView
from constants import *
from models import AdminModel
from student_crud_operations import StudentCRUD

class StudentManager:
    def __init__(self,admin:AdminModel):
        self.root = Tk()
        self.admin=admin
        self.student=StudentCRUD()
        self.setup_ui()
        self.root.mainloop()
    def setup_ui(self):
        self.root.title("Student Manager")
        self.root.geometry(geometry)
        self.root.configure(bg='#2c3e50')
        self.frame1 = Frame(self.root, padx=20, pady=20,bg='#34495e')
        self.frame2 = Frame(self.root, padx=20, pady=20,bg='#34495e')
        
        self.gradess = ["Grade one", "Grade two", "Grade three", "Grade four"]
        self.grade_var = StringVar()
        self.grade_var.set(self.gradess[0])
        
        self.grades = Combobox(self.frame1, values=self.gradess, state='readonly', textvariable=self.grade_var)
        self.lbl = Label(self.frame1, text="Choose Grade : ", font=("Arial", 14),background='#34495e', foreground='white')
        
        columns = ["name",  "email","id", "grade", "gpa","passedHours"]
        self.student_table = Treeview(self.frame2, columns=columns, show="headings")
        self.setup_table_columns(columns)

        self.show_btn = Button(self.frame1, text="Show", command=self.show_table, font=("Arial", 12))
        self.add_btn = Button(self.frame2, text="Add", command=self.add_student, font=("Arial", 12))
        self.delete_btn = Button(self.frame2, text="Delete", command=self.delete_student, font=("Arial", 12))
        self.btn_back = Button(self.frame2, text="Back", command=self.go_back, font=("Arial", 12))
        
        self.lbl.grid(column=0, row=0, padx=10, )
        self.grades.grid(column=1, row=0, padx=10,)
        self.show_btn.grid(column=1, row=1, padx=10, pady=10)
        self.frame1.pack(side="top", fill="x")

    def setup_table_columns(self, columns):
        self.student_table.heading(columns[0], text="Name")
        self.student_table.heading(columns[1], text="Email")
        self.student_table.heading(columns[2], text="ID")
        self.student_table.heading(columns[3], text="Grade")
        self.student_table.heading(columns[4], text="GPA")
        self.student_table.heading(columns[5], text="Passed Hours")

        for col in columns:
            self.student_table.column(col, anchor='center')

        style = Style()
        style.configure("Treeview", font=("Arial", 12), rowheight=25)
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"))

    def add_student(self):
        from insert_student_view import InsertStudentView
        grade=self.grade_var.get()
        InsertStudentView(grade)
        self.show_table()
        

           

    def delete_student(self):
        selected_item = self.student_table.selection()
        id = self.student_table.item(selected_item)['values'][2]
        # ! Delete from database where ssh = item
        print(id)
        
        self.student.delete_student(id)
        self.show_table()

    def show_table(self):
        for item in self.student_table.get_children():
            self.student_table.delete(item)

        grade_index = self.gradess.index(self.grade_var.get()) 
        if grade_index == 0:
            grade = "Grade one"
        elif grade_index == 1:
            grade = "Grade two"
        elif grade_index == 2:
            grade = "Grade three"
        else:
            grade = "Grade four"
            
        students = self.student.read_students(grade)
        for student in students:
            self.student_table.insert("", "end", values=(student[1], student[3], student[4], student[6],student[5],student[7]))

        self.student_table.pack(padx=10, pady=10)
        self.delete_btn.pack(padx=10, pady=10, side=LEFT)
        self.add_btn.pack(padx=10, pady=10, side=LEFT)
        self.btn_back.pack(padx=10, pady=10, side=LEFT)
        self.frame2.pack(fill="both", expand=True)

    def go_back(self):
        self.root.destroy()
        AdminView(self.admin)
