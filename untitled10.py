
'''
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Style
from tkinter.ttk import Treeview
#from tkinter.ttk import *
import sqlite3

def stuudent_corces_regestered():
 
    con = sqlite3.Connection('db.db')
    def root_window_title():
        root = Tk()
        root.title("نظام المقررات")
        root.geometry("650x450")
        title_lbl = Label(root, text="بيان المقررات", font=("Arial", 16))
        title_lbl.pack()
        return root


    def studentInfo_frame(root, student_name, student_gpa,student_year):

       student_frame = Frame(root)
       student_frame.pack()

       studentName_lbl = Label(student_frame, text=f"اسم الطالب: {student_name}", font=("Arial", 12))
       studentName_lbl.grid(row=0, column=1, padx=10, pady=5)

       studentGpa_lbl = Label(student_frame, text=f"المعدل التراكمي: {student_gpa}", font=("Arial", 12))
       studentGpa_lbl.grid(row=0, column=0, padx=10, pady=5)

       studentYear_lbl = Label(student_frame, text=f"العام الدراسى: {student_year}", font=("Arial", 12))
       studentYear_lbl.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
    


    def backGround_img():
        BGStudent_img=Image.open('imagess\istockphoto-176817032-1024x1024 (1).jpg') 
        img_tkStudent=ImageTk.PhotoImage(BGStudent_img)





    def CoursesTable(root, courses):
       courses_frame = Frame(root)
       courses_frame.pack()


       columns = ("grade","credits","course_name","course_code")

       tree =Treeview(courses_frame, columns=columns, show="headings")


       #tree.heading("course_code", text="كود المقرر")
       tree.heading("course_name", text="كود المقرر")
       tree.heading("credits", text="عدد الساعات")
       tree.heading("grade", text="اسم المقرر")


       tree.column("course_name", width=200)
       tree.column("credits", width=100)
       tree.column("grade", width=200)
       tree.column("course_code", width=0)

       res = con.execute('SELECT subject_id FROM regestered WHERE student_id = 1').fetchall()
       for course in res:
           res2 = con.execute('SELECT course_name,course_hours,course_code FROM course WHERE course_id = ?',(course)).fetchall()
           for selc in res2:
               tree.insert("", END, values=selc)
       #for course in courses:
        #   tree.insert("", END, values=course)

       tree.pack()

    


    def BackButton(root):
        def logout():
            root.destroy()
            student_information()
        back_button = Button(root, text="BACK",font=("Arial", 12,'bold'),fg="white", bg="dark blue",command=logout)
        back_button.pack(side=LEFT, anchor="sw", padx=7, pady=5)


    def student_info():
         student_name = "شمس مجدي"
         student_gpa = 3.75
         student_year = "الفرقة الثالثة"


         courses = [
        ("A",3,"Structural programming","CS101"),
        ("B+",3, "Discrete mathematics","MA102"),
        ( "B",3,"Physics","PH103"),
        ("A-",2,"English","EN104")
         ]

         root = root_window_title()
         studentInfo_frame(root, student_name, student_gpa ,student_year)
         CoursesTable(root, courses)
         BackButton(root)
         root.mainloop()


    student_info()
    
stuudent_corces_regestered()
'''



import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Style, Treeview
from PIL import Image, ImageTk

class Database:
    def __init__(self, db_name='db.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_courses(self, student_id):
        self.cursor.execute('SELECT subject_id FROM regestered WHERE student_id = ?', (student_id,))
        courses_ids = [course[0] for course in self.cursor.fetchall()]

        courses = []
        for course_id in courses_ids:
            self.cursor.execute('SELECT course_name, course_hours, course_code FROM course WHERE course_id = ?', (course_id,))
            course = self.cursor.fetchone()
            if course:
                courses.append(course)
        return courses

    def close(self):
        self.connection.close()

class Student:
    def __init__(self, name, gpa, year):
        self.name = name
        self.gpa = gpa
        self.year = year

class StudentCoursesApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("نظام المقررات")
        self.root.geometry("650x450")

        self.setup_ui()

    def setup_ui(self):
        self.title_lbl = Label(self.root, text="بيان المقررات", font=("Arial", 16))
        self.title_lbl.pack()

        self.student = Student("شمس مجدي", 3.75, "الفرقة الثالثة")
        self.create_student_info_frame()
        self.create_courses_table()
        self.create_back_button()

    def create_student_info_frame(self):
        student_frame = Frame(self.root)
        student_frame.pack()

        studentName_lbl = Label(student_frame, text=f"اسم الطالب: {self.student.name}", font=("Arial", 12))
        studentName_lbl.grid(row=0, column=1, padx=10, pady=5)

        studentGpa_lbl = Label(student_frame, text=f"المعدل التراكمي: {self.student.gpa}", font=("Arial", 12))
        studentGpa_lbl.grid(row=0, column=0, padx=10, pady=5)

        studentYear_lbl = Label(student_frame, text=f"العام الدراسى: {self.student.year}", font=("Arial", 12))
        studentYear_lbl.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

    def create_courses_table(self):
        courses_frame = Frame(self.root)
        courses_frame.pack()

        columns = ("grade", "credits", "course_name", "course_code")
        tree = Treeview(courses_frame, columns=columns, show="headings")

        tree.heading("course_name", text="كود المقرر")
        tree.heading("credits", text="عدد الساعات")
        tree.heading("grade", text="اسم المقرر")
        
        tree.column("course_name", width=200)
        tree.column("credits", width=100)
        tree.column("grade", width=200)
        tree.column("course_code", width=0)

        courses = self.db.get_courses(1)  # assuming student_id is 1
        for course in courses:
            tree.insert("", END, values=course)

        tree.pack()

    def create_back_button(self):
        back_button = Button(self.root, text="BACK", font=("Arial", 12, 'bold'), fg="white", bg="dark blue", command=self.go_back)
        back_button.pack(side=LEFT, anchor="sw", padx=7, pady=5)

    def go_back(self):
        self.root.destroy()
        # Assuming student_information() is defined elsewhere
        # student_information()

def main():
    root = Tk()
    app = StudentCoursesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()



