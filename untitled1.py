import sqlite3
from tkinter import *
from tkinter.ttk import Treeview, Button, Scrollbar, Style

class Database:
    def __init__(self, db_name='db.db'):
        self.db_name = db_name

    def execute_query(self, query, params=()):
        with sqlite3.Connection(self.db_name) as con:
            cursor = con.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def execute_non_query(self, query, params=()):
        with sqlite3.Connection(self.db_name) as con:
            cursor = con.cursor()
            cursor.execute(query, params)
            con.commit()

class SubjectManager:
    def __init__(self, db):
        self.db = db

    def get_subjects(self, year):
        query = 'SELECT course_id, course_name, course_hours, course_code FROM course WHERE year = ?'
        return self.db.execute_query(query, (year,))

    def register_subject(self, subject_id, student_id):
        query = 'INSERT INTO regestered(subject_id, student_id) VALUES (?, ?)'
        self.db.execute_non_query(query, (subject_id, student_id))

class SubjectManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Subject Manager')
        self.db = Database()
        self.subject_manager = SubjectManager(self.db)
        self.initialize_ui()

    def initialize_ui(self):
        self.columns = ['id', 'Subject Name', 'Number of hours']

        # Setup Treeview for available subjects
        self.tree = Treeview(self.root, columns=self.columns, show='headings')
        self.tree.column('Subject Name', width=200, anchor='center')
        self.tree.column('Number of hours', width=300, anchor='center')
        self.tree.heading('id', text='كود المقرر')
        self.tree.heading('Subject Name', text='اسم المقرر')
        self.tree.heading('Number of hours', text='عدد الساعات')

        # Setup Treeview for selected subjects
        self.tree2 = Treeview(self.root, columns=self.columns, show='headings')
        self.tree2.column('Subject Name', width=200, anchor='center')
        self.tree2.column('Number of hours', width=300, anchor='center')
        self.tree2.heading('id', text='Id')
        self.tree2.heading('Subject Name', text='Subject Name')
        self.tree2.heading('Number of hours', text='Number of hours')

        self.load_subjects()
        self.create_buttons()

        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.grid(row=0, column=0, columnspan=2)
        self.tree2.grid(row=1, column=0, columnspan=2)
        scrollbar.grid(row=0, column=2, columnspan=2, sticky=N + S)

        style = Style()
        style.configure('Treeview', font=('Arial', 12), rowheight=30, foreground='#e5e5e5', background='#14213d')
        style.map('Treeview', foreground=[('selected', '#000000')], background=[('selected', '#fca311')])
        style.configure('Treeview.Heading', font=('Tahoma', 14))

    def load_subjects(self):
        subjects = self.subject_manager.get_subjects(year=1)
        for sub in subjects:
            self.tree.insert("", 'end', iid=sub[0], values=sub)

    def create_buttons(self):
        btn_save = Button(self.root, text='Save', command=self.save_selected)
        btn_save.grid(row=2, column=0, columnspan=2)

        btn_add = Button(self.root, text='Add', command=self.add_selected)
        btn_add.grid(row=3, column=0, columnspan=2)

        btn_del = Button(self.root, text='Delete', command=self.delete_selected)
        btn_del.grid(row=4, column=0, columnspan=2)

        btn_back = Button(self.root, text='Back', command=self.logout)
        btn_back.grid(row=5, column=0, columnspan=2)

    def save_selected(self):
        for selected in self.tree2.get_children():
            subje = self.tree2.item(selected)['values']
            self.subject_manager.register_subject(subject_id=subje[0], student_id=1)
        self.logout()

    def delete_selected(self):
        for selected in self.tree2.selection():
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
        subjects = self.subject_manager.get_subjects(year=1)
        for sub in subjects:
            self.tree.insert("", 'end', iid=sub[0], values=sub)

    def logout(self):
        self.root.destroy()
        # Call student_information() function if needed

def main():
    root = Tk()
    app = SubjectManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()