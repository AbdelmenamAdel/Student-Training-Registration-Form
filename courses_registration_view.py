import sqlite3
from tkinter import *
from tkinter.ttk import Treeview, Button, Scrollbar, Style
from constants import *
from courses_registration_crud import CoursesRegistrationCRUD
from models import StudentModel
class CoursesRegistrationView:
    def __init__(self, student:StudentModel):
        self.root = Tk()
        self.student=student
        self.root.title('تسجيل المقررات')
        self.root.geometry("650x500+250+100")
        self.root.resizable(False, False)
        self.root.configure(bg=common_color)
        self.subject_manager = CoursesRegistrationCRUD(self.student[3])
        self.initialize_ui()
        self.load_subjects()
        self.load_registered_subjects()
        self.root.mainloop()

    def initialize_ui(self):
        self.columns = ['id', 'Subject Name', 'Subject Code']

        # Setup Treeview for available subjects
        self.tree = Treeview(self.root, height=5, columns=self.columns, show='headings')
        self.tree.column('Subject Name', width=200, anchor='center')
        self.tree.column('Subject Code', width=200, anchor='center')
        self.tree.column('id', width=200, anchor='center')
        self.tree.heading('id', text='Subject Id')
        self.tree.heading('Subject Name', text='Subject Name')
        self.tree.heading('Subject Code', text='Subject Code')

        # Setup Treeview for selected subjects
        self.tree2 = Treeview(self.root, height=5, columns=self.columns, show='headings')
        self.tree2.column('Subject Name', width=200, anchor='center')
        self.tree2.column('Subject Code', width=200, anchor='center')
        self.tree2.column('id', width=200, anchor='center')
        self.tree2.heading('id', text='Subject Id')
        self.tree2.heading('Subject Name', text='Subject Name')
        self.tree2.heading('Subject Code', text='Subject Code')

        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.tree2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        scrollbar.grid(row=0, column=3, rowspan=2, sticky=N+S)

        style = Style()
        style.configure('Treeview', font=('Arial', 12), rowheight=30, foreground='#e5e5e5', background='#14213d')
        style.map('Treeview', foreground=[('selected', '#000000')], background=[('selected', '#fca311')])
        style.configure('Treeview.Heading', font=('Tahoma', 14))

        self.create_buttons()

    def load_subjects(self):
        if(self.student[6]=="Grade one"):
            grade = 1
        elif(self.student[6]=="Grade two"):
            grade = 2
        elif(self.student[6]=="Grade three"):
            grade = 3
        else :
            grade = 4
        student_id = self.subject_manager.get_student_id()
        subjects = self.subject_manager.get_subjects(grade=grade)
        registered_subjects = self.subject_manager.get_registered_subjects(student_id)
        registered_subject_names = {sub[1] for sub in registered_subjects}

        for sub in subjects:
            if sub[1] not in registered_subject_names:
                self.tree.insert("", 'end', iid=sub[0], values=sub)

    def load_registered_subjects(self):
        student_id = self.subject_manager.get_student_id()
        subjects = self.subject_manager.get_registered_subjects(student_id)
        for sub in subjects:
            self.tree2.insert("", 'end', iid=sub[0], values=sub)

    def create_buttons(self):
        btn_add = Button(self.root, text='Add', command=self.add_selected)
        btn_add.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

        btn_save = Button(self.root, text='Save', command=self.save_selected)
        btn_save.grid(row=2, column=2, padx=10, pady=10, sticky='ew')

        btn_del = Button(self.root, text='Delete', command=self.delete_selected)
        btn_del.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

        btn_back = Button(self.root, text='Back', command=self.logout)
        btn_back.grid(row=3, column=2, padx=10, pady=10, sticky='ew')

    def save_selected(self):
        student_id = self.subject_manager.get_student_id()
        for selected in self.tree2.get_children():
            subject = self.tree2.item(selected)['values']
            self.subject_manager.register_subject(subject_name=subject[1], student_id=student_id)
        self.logout()

    def delete_selected(self):
        student_id = self.subject_manager.get_student_id()
        for selected in self.tree2.selection():
            subject = self.tree2.item(selected)['values']
            self.subject_manager.unregister_subject(subject_name=subject[1], student_id=student_id)
            self.tree2.delete(selected)
        self.refresh_tree()
    def add_selected(self):
        for selected in self.tree.selection():
            subject = self.tree.item(selected)['values']
            self.tree2.insert('', 'end', values=subject)
        for selected in self.tree.selection():
            self.tree.delete(selected)

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        self.load_subjects()

    def logout(self):
        self.root.destroy()
        from student_view import StudentView
        StudentView(self.student)