from tkinter import *
from tkinter.ttk import Combobox, Style, Treeview
import sqlite3
from constants import *
from models import CourseModel
from cources_crud_operations import CoursesCRUD
class CoursesInfoView:
    def __init__(self,admin):
        self.admin=admin
        self.root = Tk()
        self.root.title('تسجيل المقرارت')
        self.root.geometry(geometry)
        self.root.resizable(False, False)
        self.root.configure(bg=common_color)
        self.courseCRUD = CoursesCRUD()
        self.sub_name = StringVar()
        self.sub_code = StringVar()
        self.sub_hour = StringVar()

        self.level = ['المستوي الاول', 'المستوي الثاني', 'المستوي الثالث', 'المستوي الرابع']

        self.create_widgets()
        self.create_treeview()

        self.root.mainloop()

    def create_widgets(self):
        self.entries_frame = Frame(self.root, bg=common_color)
        self.entries_frame.place(x=25, y=50, width=150)

        title = Label(self.entries_frame, text='اختيار المستوي', font=(14), bg='#1c5e80', fg='white')
        title.pack(pady=10)

        self.selcet_level = Combobox(self.entries_frame, values=self.level, state='readonly', width=18)
        self.selcet_level.pack(pady=10)

        self.bt_show = Button(self.entries_frame, text='Show Table', command=self.show_table, width=btn_width)
        self.bt_show.pack(pady=5)
        self.bt_add = Button(self.entries_frame, text='Add', command=self.add_sub, width=btn_width)
        self.bt_add.pack(pady=5)
        self.bt_delete = Button(self.entries_frame, text='Delete', command=self.delete, width=btn_width)
        self.bt_delete.pack(pady=5)
        self.bt_back = Button(self.entries_frame, text='Back', command=self.back, width=btn_width)
        self.bt_back.pack(pady=5)

    def create_treeview(self):
        tree_frame = Frame(self.root)
        tree_frame.place(x=200, y=25, width=520, height=450)

        style = Style()
        style.configure("mystyle.Treeview", font=('Calibri', 13), rowheight=50)
        style.configure('mystyle.Treeview.Heading', font=('Calibri', 13))

        self.tv = Treeview(tree_frame, columns=(1, 2, 3), style="mystyle.Treeview")
        self.tv.heading("1", text="اسم المقرر")
        self.tv.column("1", width=200)
        self.tv.heading("2", text="عدد الساعات")
        self.tv.column("2", width=50)
        self.tv.heading("3", text="كود المقرر")
        self.tv.column("3", width=50)
        self.tv['show'] = 'headings'
        self.tv.pack(fill=BOTH, expand=True)

    def add_sub(self):
        self.root2 = Toplevel(self.root)
        self.root2.geometry('400x250+500+250')
        self.root2.resizable(False, False)
        self.root2.title('تسجيل المقرر')
        self.root2.configure(bg=common_color)

        self.root2_frame = Frame(self.root2, bg=common_color)
        self.root2_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.sub_name = StringVar()
        self.sub_code = StringVar()
        self.sub_hour = StringVar()

        sub_name_lbl = Label(self.root2_frame, text='اسم المقرر', background=common_color, font=(14), bg='#1c5e80', fg='white')
        sub_name_lbl.grid(row=0, column=1, pady=10, padx=10)
        txt_namesub = Entry(self.root2_frame, textvariable=self.sub_name, width=20)
        txt_namesub.grid(row=0, column=0, pady=10, padx=10)

        sub_code_lbl = Label(self.root2_frame, text='كود المقرر', background=common_color, font=(14), bg='#1c5e80', fg='white')
        sub_code_lbl.grid(row=1, column=1, pady=10, padx=10)
        txt_codesub = Entry(self.root2_frame, textvariable=self.sub_code, width=20)
        txt_codesub.grid(row=1, column=0, pady=10, padx=10)

        sub_hour_lbl = Label(self.root2_frame, text='عدد الساعات', background=common_color, font=(14), bg='#1c5e80', fg='white')
        sub_hour_lbl.grid(row=2, column=1, pady=10, padx=10)
        txt_hoursub = Entry(self.root2_frame, textvariable=self.sub_hour, width=20)
        txt_hoursub.grid(row=2, column=0, pady=10, padx=10)

        btn_save = Button(self.root2_frame, text='Save', command=self.savedata, width=btn_width)
        btn_save.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

    def savedata(self):
        # con = sqlite3.connect('Database/student_registration_system.db')
        course=CourseModel(name=self.sub_name.get(),code=self.sub_code.get(),hours=self.sub_hour.get(),grade=(self.level.index(self.selcet_level.get()) + 1))
        # con.execute('''INSERT INTO Courses (name, code, hours, grade) VALUES (?,?,?,?)''', (course.name,course.code,course.hours,course.grade))
        # con.commit()
        # con.close()
        self.courseCRUD.insert_course(course)
        self.show_table()
        self.root2.destroy()

    def delete(self):
        # con = sqlite3.Connection('Database/student_registration_system.db')
        for cid in self.tv.selection():
            self.courseCRUD.delete_course(cid)
            # con.execute('DELETE FROM Courses WHERE cid = ?', (cid,))
        # con.commit()
        # con.close()
        self.show_table()

    def show_table(self):
        # con = sqlite3.Connection('Database/student_registration_system.db')
        grade = self.level.index(self.selcet_level.get()) + 1
        for item in self.tv.get_children():
            self.tv.delete(item)
        res = self.courseCRUD.read_courses(grade)
        # res = con.execute('SELECT * FROM Courses WHERE grade = ?', (grade,)).fetchall()
        for sub in res:
            self.tv.insert('', 'end', iid=sub[0], values=(sub[1],sub[3],sub[2]))
        # con.commit()
        # con.close()

    def back(self):
        self.root.destroy()
        from admin_view import AdminView
        AdminView(admin=self.admin)
        

