from tkinter import END, LEFT, Button, Frame, Image, Label, Tk
from tkinter.ttk import Treeview


def stuudent_corces_regestered():
 

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

    def CoursesTable(root, courses):
       courses_frame = Frame(root)
       courses_frame.pack()


       columns = ("grade","credits","course_name","course_code")

       tree =Treeview(courses_frame, columns=columns, show="headings")


       tree.heading("course_code", text="كود المقرر")
       tree.heading("course_name", text="اسم المقرر")
       tree.heading("credits", text="عدد الساعات")
       tree.heading("grade", text="الدرجة")


       tree.column("course_name", width=200)
       tree.column("credits", width=100)
       tree.column("grade", width=50)
       tree.column("course_code", width=100)


       for course in courses:
           tree.insert(END, values=course)

       tree.pack()

    


    def BackButton(root):
        def logout():
            root.destroy()
            # student_information()
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