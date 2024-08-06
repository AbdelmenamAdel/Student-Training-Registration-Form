import sqlite3
from tkinter import *
from tkinter.ttk import Treeview, Button, Scrollbar, Style
from constants import *
from models import StudentModel
class Database:
    def __init__(self, db_name='Database/student_registration_system.db'):
        self.db_name = db_name

    def execute_query(self, query, params=()):
        with sqlite3.connect(self.db_name) as con:
            cursor = con.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
       
    def save_changes(self, query, params=()):
        with sqlite3.connect(self.db_name) as con:
            cursor = con.cursor()
            cursor.execute(query, params)
            con.commit()

class SubjectManager:
    def __init__(self, db,email):
        self.db = db
        self.email = email

    def get_subjects(self, grade):
        query = 'SELECT * FROM Courses WHERE grade = ?'
        return self.db.execute_query(query, (grade,))
    def get_student_id(self):
        query = 'SELECT sid FROM Students WHERE email = ?'
        return self.db.execute_query(query, (self.email,))
    def get_registered_subjects(self, student_id):
        query = 'SELECT subject_name FROM Registered WHERE student_id = ?'
        res = self.db.execute_query(query, (student_id,))
        subject_names = tuple([row[0] for row in res])
        if not subject_names:
            return []
        query = f'SELECT * FROM Courses WHERE name IN ({",".join("?" * len(subject_names))})'
        return self.db.execute_query(query, subject_names)

    def register_subject(self, subject_name, student_id):
        query = 'INSERT INTO Registered (subject_name, student_id) VALUES (?, ?)'
        self.db.save_changes(query, (subject_name, student_id))

    def unregister_subject(self, subject_name, student_id):
        query = 'DELETE FROM Registered WHERE subject_name = ? AND student_id = ?'
        self.db.save_changes(query, (subject_name, student_id))

class CoursesRegistrationView:
    def __init__(self, student:StudentModel):
        self.root = Tk()
        self.student=student
        self.student_email =self.student.email
        self.root.title('تسجيل المقررات')
        self.root.geometry("650x500+250+100")
        self.root.resizable(False, False)
        self.root.configure(bg=common_color)
        self.db = Database()
        self.subject_manager = SubjectManager(self.db, self.student_email)
        self.initialize_ui()
        self.load_subjects()
        self.load_registered_subjects()
        self.root.mainloop()

    def initialize_ui(self):
        self.columns = ['id', 'Subject Name', 'Number of hours']

        # Setup Treeview for available subjects
        self.tree = Treeview(self.root, height=5, columns=self.columns, show='headings')
        self.tree.column('Subject Name', width=200, anchor='center')
        self.tree.column('Number of hours', width=200, anchor='center')
        self.tree.column('id', width=200, anchor='center')
        self.tree.heading('id', text='Subject Code')
        self.tree.heading('Subject Name', text='Subject Name')
        self.tree.heading('Number of hours', text='Number of Hours')

        # Setup Treeview for selected subjects
        self.tree2 = Treeview(self.root, height=5, columns=self.columns, show='headings')
        self.tree2.column('Subject Name', width=200, anchor='center')
        self.tree2.column('Number of hours', width=200, anchor='center')
        self.tree2.column('id', width=200, anchor='center')
        self.tree2.heading('id', text='Subject Code')
        self.tree2.heading('Subject Name', text='Subject Name')
        self.tree2.heading('Number of hours', text='Number of Hours')

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
        if(self.student.grade=="Grade one"):
            grade = 1
        elif(self.student.grade=="Grade two"):
            grade = 2
        elif(self.student.grade=="Grade three"):
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
        for selected in self.tree2.get_children():
            subject = self.tree2.item(selected)['values']
            self.subject_manager.register_subject(subject_name=subject[1], student_id=1)
        self.logout()

    def delete_selected(self):
        for selected in self.tree2.selection():
            subject = self.tree2.item(selected)['values']
            self.subject_manager.unregister_subject(subject_name=subject[1], student_id=1)
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
        # Call student_information() function if needed
