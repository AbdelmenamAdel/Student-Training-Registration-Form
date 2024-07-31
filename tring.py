import re
from tkinter import Button, Entry, Frame, IntVar, Label, Radiobutton, Checkbutton, Tk, StringVar, BooleanVar, messagebox
from tkinter import ttk
from constants import *  # Ensure constants are defined here
from models import StudentModel
from student_crud_operations import StudentCRUD

class InsertStudentView:
    def __init__(self):
        self.root = Tk()
        self.root.title("Insert A New Student")
        self.root.geometry("500x600")
        self.root.configure(bg='#2c3e50')

        self.frame = Frame(self.root, padx=20, pady=20, bg='#34495e')
        self.frame.pack(pady=50)

        self.create_widgets()
        
        self.root.mainloop()

    def create_widgets(self):
        # ! Title
        title_lbl = Label(self.frame, text="Create An Account", font=('Arial', 18, 'bold'), bg='#34495e', fg='white')
        title_lbl.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # ! Labels and Entries
        labels = ["Student Name", "Email", "Password", "Confirm Password", "National ID", "GPA", "Passed Hours", "Grade"]
        self.entries = {}

        for i, text in enumerate(labels):
            lbl = Label(self.frame, text=f"{text}:", font=('Arial', 12), bg='#34495e', fg='white', anchor="n")
            lbl.grid(row=i+1, column=0, sticky="e", pady=pady10)
            if text != "Grade":
                entry = Entry(self.frame, width=25)
                entry.grid(row=i+1, column=1, pady=pady10, padx=padx10)
                self.entries[text] = entry

        # ! Grade Combobox
        gradess = ["Grade one", "Grade two", "Grade three", "Grade four"]
        self.grade_var = StringVar()
        self.grade_var.set(gradess[0])

        grades = ttk.Combobox(self.frame, values=gradess, state='readonly', textvariable=self.grade_var)
        grades.grid(row=8, column=1, pady=pady10)

        # ! Buttons
        save_btn = Button(self.frame, text="Insert Student", command=self.save)
        save_btn.grid(row=9, columnspan=2, pady=pady10)    
    def save(self):
        if(self.validate_entries()!=False):
            # ! Get values from entries
            student = StudentModel(
                username=self.entries["Student Name"].get(),
                email=self.entries["Email"].get(),
                password=self.entries["Password"].get(),
                Ssh=self.entries["National ID"].get(),
                gpa=self.entries["GPA"].get(),
                grade=self.grade_var.get(),
                passedHours=self.entries["Passed Hours"].get()
            )
            messagebox.showinfo("Success", "Student inserted successfully!")
            # ! Save student to database
            std=StudentCRUD()
            std.insert_student(student)
            std.read_students()
            # # ! Example usage of student object
            # print(student.username)
            # print(student.email)
            # print(student.password)
            # print(student.Ssh)
            # print(student.gpa)
            # print(student.grade)
            # print(student.passedHours)
    def is_valid_email(self, email):
        # ! Regex pattern for validating an Email
        pattern = r'^[a-zA-Z0-9_.+-]+@fci\.bu\.edu\.eg$'
        return re.match(pattern, email)
    def validate_entries(self):
        # ! Validate entries
        if self.entries["Email"].get() == "" or self.entries["Student Name"].get() == "" or self.entries["Password"].get() == "" or self.entries["National ID"].get() == "" or self.entries["GPA"].get() == "" or self.entries["Passed Hours"].get() == "" :
            messagebox.showerror("Error", "Please fill all fields")
            return False
        if self.entries["Password"].get() != self.entries["Confirm Password"].get():
            messagebox.showerror("Error", "Passwords don't match")
            return False
        if self.entries["National ID"].get().isdigit() == False:
            messagebox.showerror("Error", "National ID must be a number")
            return False
        if len(self.entries["National ID"].get()) != 14:
            messagebox.showerror("Error", "National ID lenth must be 14 digits")
            return False
        email = self.entries["Email"].get()
        if not self.is_valid_email(email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return False
        if self.entries["GPA"].get().isdigit() == False:
            messagebox.showerror("Error", "GPA must be a number")
            return False
        if self.entries["Passed Hours"].get().isdigit() == False:
            messagebox.showerror("Error", "Passed Hours must be a number")
            return False
   
if __name__ == "__main__":
    InsertStudentView()
