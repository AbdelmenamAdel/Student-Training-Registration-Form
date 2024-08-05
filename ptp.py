
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Style
from tkinter.ttk import Treeview
#from tkinter.ttk import *
import sqlite3


def add_corces():

    root =Tk()


    sub_name=StringVar()
    sub_code=StringVar()
    sub_hour=StringVar()



    root.title('تسجيل المقرارت')
    root.geometry('1080x615+0+0')
    root.configure(bg='#1c5e80')

    entries_frame=Frame(root)

    entries_frame.place_configure(x=5,y=5,width=400,height =510)
    title=Label(entries_frame,text='اختيار المستوي..',font=(14))
    title.place_configure(x=250,y=1)
    level=['المستوي الاول', 'المستوي الثاني','المستوي الثالث','المستوي الرابع']

    first_grade = [
            ("c++","cs50", 3),
            ("oop","gh5",3),
        ]

    second_grade = [
            ("data structuer","cs50", 3),
            ("algorithm","gh5",3),
        ]


    third_grade = [
            ("database","cs50", 3),
            ("is","gh5",3),
        ]


    fourth_grade = [
            ("math","cs50", 3),
            ("english","gh5",3),
        ]




    #grade_var = StringVar() ,textvariable = grade_var
    selcet_level=Combobox(entries_frame,width=18,values=level,state='readonly')
    selcet_level.place_configure(x=100,y=3)

    def add_sub():
        root2=Tk()
        root2.geometry('400x250')
        sub_name =Label(root2,text='اسم المقرر',)
        sub_name.place(x=290,y=110)

        txt_namesub=Entry(root2,textvariable=sub_name,width=20)
        txt_namesub.place_configure(x=150,y=110)


        sub_code =Label(root2,text='كود المقرر',)
        sub_code.place(x=290,y=140)

        txt_codesub=Entry(root2,textvariable=sub_code,width=20)
        txt_codesub.place_configure(x=150,y=140)


        sub_hour =Label(root2,text='عدد الساعات',)
        sub_hour.place(x=290,y=170)

        txt_hoursub=Entry(root2,textvariable=sub_hour,width=20)
        txt_hoursub.place_configure(x=150,y=170)

        def savedata():
            con = sqlite3.Connection('db.db')
            
            info = (txt_namesub.get(), txt_codesub.get(), txt_hoursub.get())
            if selcet_level.get() == level[0]:
                #first_grade.append(info)
                x = 1
                con.execute('''INSERT INTO course(course_name,course_code,course_hours,subject,year) VALUES(?,?,?,?,?)''',(info[0],info[1],info[2],"m",x))
                show_table5()
            elif selcet_level.get() == level[1]:
                 #second_grade.append(info)
                 x = 2
                 con.execute('''INSERT INTO course(course_name,course_code,course_hours,subject,year) VALUES(?,?,?,?,?)''',(info[0],info[1],info[2],"m",x))
                 show_table5()
            elif selcet_level.get() == level[2]:
                #third_grade.append(info)
                x = 3
                con.execute('''INSERT INTO course(course_name,course_code,course_hours,subject,year) VALUES(?,?,?,?,?)''',(info[0],info[1],info[2],"m",x))
                show_table5()
            elif selcet_level.get() == level[3]:
                #fourth_grade.append(info)
                x = 4
                con.execute('''INSERT INTO course(course_name,course_code,course_hours,subject,year) VALUES(?,?,?,?,?)''',(info[0],info[1],info[2],"m",x))
                show_table5()
            #show_table5()
            con.commit()
            con.close()
            root2.destroy()
        btn_save = Button(root2,text = 'save',command=savedata)
        btn_save.pack_configure(anchor='center',side='bottom')
    
        root2.mainloop()
        
        

    def delet():
        con = sqlite3.Connection('db.db')
        
        for student in tv.selection():
            con.execute('DELETE FROM course WHERE course_name = ?',(student,))
                #tv.delete(student)
        show_table5()
        con.commit()
        con.close()
                
    
    bt_add=Button(entries_frame,text='Add',command= add_sub)
    bt_delet=Button(entries_frame,text='Delete', command= delet)


    bt_delet.pack_configure(anchor='center',side='bottom')
    bt_add.pack_configure(anchor='center',side='bottom',)


    tree_frame=Frame(root,)
    tree_frame.place(x=420,y=5,width=500,height=510)
    style=Style()
    style.configure("mystyle.Treeview",font=('Calibri',13 ),rowheight=50)
    style.configure('mystyle.Treeview.Heading',font=('Calibri',13 ))
    tv=Treeview(tree_frame,columns=(1,2,3) ,style="mystyle.Treeview")

    tv.heading("1", text="اسم المقرر")
    tv.column("1", width="140")
    tv.heading("2", text="عدد الساعات")
    tv.column("2", width="140")
    tv.heading("3", text="كود المقرر")
    tv.column("3", width="140")
    tv['show']='headings'

    tv.place(x=1,y=1,height=600)

    def hide():
        root.geometry("400x510")
        #print(selcet_level.get())
    def show():
        root.geometry('1080x615+0+0')
    bthide =Button(entries_frame,text="Hide_Table",command=hide)
    bthide.place(x=100,y=270)
    


    def show_table5():
        
        con = sqlite3.Connection('db.db')
        
        if selcet_level.get() == level[0]:
            for item in tv.get_children():
                tv.delete(item)
            res = con.execute('SELECT course_name,course_hours,course_code FROM course WHERE year = 1').fetchall()
            for sub in res:
                tv.insert("",'end',iid=sub[0],values=sub )
                tv.grid(row=0,column=0)
        elif selcet_level.get() == level[1]:
            for item in tv.get_children():
                tv.delete(item)
            res = con.execute('SELECT course_name,course_hours,course_code FROM course WHERE year = 2').fetchall()    
            for sub in res:
                tv.insert("",'end',iid=sub[0],values=sub )
                tv.grid(row=0,column=0)
                
        elif selcet_level.get() == level[2]:
            for item in tv.get_children():
                tv.delete(item)
            res = con.execute('SELECT course_name,course_hours,course_code FROM course WHERE year = 3').fetchall()
            for sub in res:
                tv.insert("",'end',iid=sub[0],values=sub )
                tv.grid(row=0,column=0)
        elif selcet_level.get() == level[3]:
            for item in tv.get_children():
                tv.delete(item)
            res = con.execute('SELECT course_name,course_hours,course_code FROM course WHERE year = 4').fetchall()
            for sub in res :
                tv.insert("",'end',iid=sub[0],values=sub )
                tv.grid(row=0,column=0)
        con.commit()
        con.close()

    btshow5 =Button(entries_frame,text="Show_Table",command=show_table5)
    btshow5.place(x=200,y=270)

    def backf():
        root.destroy()
        admin_info()
    
    btback =Button(entries_frame,text="Back",command=backf)
    btback.pack_configure(anchor='center',side='bottom')
    root.mainloop()





#-----------------------------------------------------------------------#
'''
def mainn():
    root = Tk()
    frame1 = Frame(root)
    frame2 = Frame(root)

    first_grade = [
        ("Ahmed Mohamed", 1, 19, "male", 3.1),
        ("Mohamed Ahmed", 2, 19, "male", 3.3),
        ("Yasmine Mohamed", 3, 19, "female", 0.1),
        ("Ahmed Mahamod", 4, 19, "male", 2.5)
    ]

    second_grade = [
        ("Wael Ryad", 5, 20, "male", 3.5),
        ("Ahmed Ibrahim", 6, 20, "male", 3.2),
        ("Hossam Ashraf", 7, 20, "male", 2.4),
        ("Aisha Khaled", 8, 20, "female", 1.5)
    ]

    third_grade = [
        ("Hegazy Naser", 9, 21, "male", 3.8),
        ("Reda Ahmed", 10, 21, "male", 3.9),
        ("Ahmed Mohamed", 11, 21, "male", 3.7),
        ("Esraa Ahmed", 12, 21, "female", 3.6)
    ]

    fourth_grade = [
        ("Mohamed Ahmed", 13, 22, "male", 3.9),
        ("Saad Mohamed", 14, 22, "male", 3.8),
        ("Ahmed Mohamed", 15, 22, "male", 4.0)
    ]

    gradess = ["Grade one", "Grade two", "Grade three", "Grade four"]
    grade_var = StringVar()
    grade_var.set(gradess[0])

    grades = Combobox(frame1, values=gradess, state='readonly', textvariable=grade_var)
    lbl = Label(frame1, text="Choose Grade : ")

    columns = ["name", "id", "age", "gender", "gpa"]
    student_table = Treeview(frame2, columns=columns, show="headings")
    student_table.heading(columns[0], text="Name")
    student_table.heading(columns[1], text="ID")
    student_table.heading(columns[2], text="Age")
    student_table.heading(columns[3], text="Gender")
    student_table.heading(columns[4], text="GPA")

    student_table.column("name", anchor='center')
    student_table.column("id", anchor='center')
    student_table.column("age", anchor='center')
    student_table.column("gender", anchor='center')
    student_table.column("gpa", anchor='center')

    style = Style()
    style.configure(student_table, font=("Arial", 12), rowheight=30)

    def add():
        def app():
            choosen_gender = "Male" if gender_var.get() == 1 else "Female"
            info = (username_entry.get(), id_entry.get(), age_entry.get(), choosen_gender, gpa_entry.get())

            if grade_var.get() == gradess[0]:
                first_grade.append(info)
            elif grade_var.get() == gradess[1]:
                second_grade.append(info)
            elif grade_var.get() == gradess[2]:
                third_grade.append(info)
            elif grade_var.get() == gradess[3]:
                fourth_grade.append(info)
            show_table()

        root2 = Tk()
        root2.geometry("200x500")
        frameADD = Frame(root2)

        username_lbl = Label(frameADD, text="Username : ")
        password_lbl = Label(frameADD, text="Password : ")
        age_lbl = Label(frameADD, text="Age : ")
        email_lbl = Label(frameADD, text="Email : ")
        gender_lbl = Label(frameADD, text="Gender : ")
        gpa_lbl = Label(frameADD, text="GPA : ")
        id_lbl = Label(frameADD, text="ID : ")

        username_entry = Entry(frameADD)
        password_entry = Entry(frameADD)
        email_entry = Entry(frameADD)
        age_entry = Entry(frameADD)
        gpa_entry = Entry(frameADD)
        id_entry = Entry(frameADD)

        gender_var = IntVar()
        gender_var.set(1)

        gender_radbtn = Radiobutton(frameADD, text="Male", value=1, variable=gender_var)
        gender_radbtn2 = Radiobutton(frameADD, text="Female", value=2, variable=gender_var)

        save_btn = Button(frameADD, text="Save", command=app)

        username_lbl.pack()
        username_entry.pack()
        password_lbl.pack()
        password_entry.pack()
        age_lbl.pack()
        age_entry.pack()
        email_lbl.pack()
        email_entry.pack()
        gender_lbl.pack()
        gender_radbtn.pack()
        gender_radbtn2.pack()
        gpa_lbl.pack()
        gpa_entry.pack()
        id_lbl.pack()
        id_entry.pack()
        save_btn.pack()
        def back():
            root2.destroy()
            #mainn()
        back_btn = Button(frameADD, text="Back",command=back)
        back_btn.pack()
        frameADD.place(anchor='center', relx=0.5, rely=0.5)
        #root.destroy()

        root2.mainloop()

    add_btn = Button(frame2, text="Add", command=add)
    def delete():
        for student in student_table.selection():
            student_table.delete(student)
            #if student in
    
    delete_btn = Button(frame2, text="Delete",command=delete)


    def back2():
        root.destroy()
        admin_info()

    btn_back = Button(frame2, text="Back",command=back2)

    
    def show_table():
        # Clear the existing data in the table
        for i in student_table.get_children():
            student_table.delete(i)

        if grade_var.get() == gradess[0]:
            for student in first_grade:
                student_table.insert("", "end", values=student)
        elif grade_var.get() == gradess[1]:
            for student in second_grade:
                student_table.insert("", "end", values=student)
        elif grade_var.get() == gradess[2]:
            for student in third_grade:
                student_table.insert("", "end", values=student)
        elif grade_var.get() == gradess[3]:
            for student in fourth_grade:
                student_table.insert("", "end", values=student)

        student_table.pack(padx=10, pady=10)
        delete_btn.pack(padx=10, pady=10)
        add_btn.pack(padx=10, pady=10)
        btn_back.pack(padx=10, pady=10)
        frame2.pack(side="right")

    show_btn = Button(frame1, text="Show", command=show_table)

    lbl.grid(column=0, row=0, padx=10, pady=10)
    grades.grid(column=1, row=0, padx=10, pady=10)
    show_btn.grid(column=1, row=1, padx=10, pady=10)

    frame1.pack(side="left")
    root.mainloop()


#mainn()




#from tkinter import *
#from tkinter.ttk import *


first_grade = [
        ("Ahmed Mohamed", 1, 19, "male", 3.1),
        ("Mohamed Ahmed", 2, 19, "male", 3.3),
        ("Yasmine Mohamed", 3, 19, "female", 0.1),
        ("Ahmed Mahamod", 4, 19, "male", 2.5)
    ]
second_grade = [
        ("Wael Ryad", 5, 20, "male", 3.5),
        ("Ahmed Ibrahim", 6, 20, "male", 3.2),
        ("Hossam Ashraf", 7, 20, "male", 2.4),
        ("Aisha Khaled", 8, 20, "female", 1.5)
    ]
third_grade = [
        ("Hegazy Naser", 9, 21, "male", 3.8),
        ("Reda Ahmed", 10, 21, "male", 3.9),
        ("Ahmed Mohamed", 11, 21, "male", 3.7),
        ("Esraa Ahmed", 12, 21, "female", 3.6)
    ]
fourth_grade = [
        ("Mohamed Ahmed", 13, 22, "male", 3.9),
        ("Saad Mohamed", 14, 22, "male", 3.8),
        ("Ahmed Mohamed", 15, 22, "male", 4.0)
    ]

def insert_table(list):
    for student in list:
        student_table.insert("", 'end', values=student)




def show_table():
    con = sqlite3.Connection('db.db')
    if grade_var.get() == gradess[0]:

        insert_table(first_grade)
    elif grade_var.get() == gradess[1]:
        insert_table(second_grade)
    elif grade_var.get() == gradess[2]:
        insert_table(third_grade)
    elif grade_var.get() == gradess[3]:
        insert_table(fourth_grade)
    con.commit()
    con.close()

    student_table.pack(padx=10, pady=10)



'''




def mainn():
    root = Tk()
    frame1 = Frame(root)
    frame2 = Frame(root)

    first_grade = [
        ("Ahmed Mohamed", 1, 19, "male", 3.1),
        ("Mohamed Ahmed", 2, 19, "male", 3.3),
        ("Yasmine Mohamed", 3, 19, "female", 0.1),
        ("Ahmed Mahamod", 4, 19, "male", 2.5)
    ]

    second_grade = [
        ("Wael Ryad", 5, 20, "male", 3.5),
        ("Ahmed Ibrahim", 6, 20, "male", 3.2),
        ("Hossam Ashraf", 7, 20, "male", 2.4),
        ("Aisha Khaled", 8, 20, "female", 1.5)
    ]

    third_grade = [
        ("Hegazy Naser", 9, 21, "male", 3.8),
        ("Reda Ahmed", 10, 21, "male", 3.9),
        ("Ahmed Mohamed", 11, 21, "male", 3.7),
        ("Esraa Ahmed", 12, 21, "female", 3.6)
    ]

    fourth_grade = [
        ("Mohamed Ahmed", 13, 22, "male", 3.9),
        ("Saad Mohamed", 14, 22, "male", 3.8),
        ("Ahmed Mohamed", 15, 22, "male", 4.0)
    ]

    gradess = ["Grade one", "Grade two", "Grade three", "Grade four"]
    grade_var = StringVar()
    grade_var.set(gradess[0])

    grades = Combobox(frame1, values=gradess, state='readonly', textvariable=grade_var)
    lbl = Label(frame1, text="Choose Grade : ")

    columns = ["name", "id", "age", "gender", "gpa"]
    student_table = Treeview(frame2, columns=columns, show="headings")
    student_table.heading(columns[0], text="Name")
    student_table.heading(columns[1], text="ID")
    student_table.heading(columns[2], text="Email")
    student_table.heading(columns[3], text="Year")
    student_table.heading(columns[4], text="GPA")

    student_table.column("name", anchor='center')
    student_table.column("id", anchor='center')
    student_table.column("age", anchor='center')
    student_table.column("gender", anchor='center')
    student_table.column("gpa", anchor='center')

    style = Style()
    style.configure(student_table, font=("Arial", 12), rowheight=30)

    def add():
        def app():
            #choosen_gender = "Male" if gender_var.get() == 1 else "Female"
            info = (username_entry.get(), email_entry.get(), password_entry.get(), gpa_entry.get())
            con = sqlite3.Connection('db.db')
            if grade_var.get() == gradess[0]:
                con.execute('''INSERT INTO stud(stu_name,stu_email,stu_password,stu_gpa,year) VALUES(?,?,?,?,?)''',(info[0],info[1],info[2],info[3],1))
                con.commit()
                con.close()
                back()
                #first_grade.append(info)
            elif grade_var.get() == gradess[1]:
                con.execute('''INSERT INTO stud(stu_name,stu_email,stu_password,stu_gpa,year) VALUES(?,?,?,?,?)''',(info[0],info[1],info[2],info[3],2))
                con.commit()
                con.close()
                back()
                #second_grade.append(info)
            elif grade_var.get() == gradess[2]:
                con.execute('''INSERT INTO stud(stu_name,stu_email,stu_password,stu_gpa,year) VALUES(?,?,?,?,?)''',(info[0],info[1],info[2],info[3],3))
                con.commit()
                con.close()
                back()
                #third_grade.append(info)
            elif grade_var.get() == gradess[3]:
                con.execute('''INSERT INTO stud(stu_name,stu_email,stu_password,stu_gpa,year) VALUES(?,?,?,?,?)''',(info[0],info[1],info[2],info[3],4))
                con.commit()
                con.close()
                back()
                #fourth_grade.append(info)
            back()
            show_table()

        root2 = Toplevel()
        root2.geometry("200x500")
        frameADD = Frame(root2)

        username_lbl = Label(frameADD, text="Username : ")
        password_lbl = Label(frameADD, text="Password : ")
        email_lbl = Label(frameADD, text="Email : ")
        gpa_lbl = Label(frameADD, text="GPA : ")
        #gender_lbl = Label(frameADD, text="Gender : ")
        #gpa_lbl = Label(frameADD, text="GPA : ")
        #id_lbl = Label(frameADD, text="ID : ")

        username_entry = Entry(frameADD)
        password_entry = Entry(frameADD)
        email_entry = Entry(frameADD)
        #age_entry = Entry(frameADD)
        gpa_entry = Entry(frameADD)
        #id_entry = Entry(frameADD)

        #gender_var = IntVar()
        #gender_var.set(1)

        #gender_radbtn = Radiobutton(frameADD, text="Male", value=1, variable=gender_var)
        #gender_radbtn2 = Radiobutton(frameADD, text="Female", value=2, variable=gender_var)

        save_btn = Button(frameADD, text="Save", command=app)

        username_lbl.pack()
        username_entry.pack()
        password_lbl.pack()
        password_entry.pack()
        #age_lbl.pack()
        #age_entry.pack()
        email_lbl.pack()
        email_entry.pack()
        #gender_lbl.pack()
        #gender_radbtn.pack()
        #gender_radbtn2.pack()
        gpa_lbl.pack()
        gpa_entry.pack()
        #id_lbl.pack()
        #id_entry.pack()
        save_btn.pack()
        def back():
            root2.destroy()
            #mainn()
        back_btn = Button(frameADD, text="Back",command=back)
        back_btn.pack()
        frameADD.place(anchor='center', relx=0.5, rely=0.5)
        #root.destroy()

        root2.mainloop()

    add_btn = Button(frame2, text="Add", command=add)
    def delete():
        con = sqlite3.Connection('db.db')
        for selected in student_table.selection():
            student_table.delete(selected)
        for itm in student_table.get_children():
            subje = student_table.item(itm)['values']
            print(subje[1])
            con.execute('DELETE FROM stud WHERE stu_id = ?',(subje[1],))
            #student_table.delete(student)
        con.commit()
        con.close()
        show_table()
            #if student in
    
    delete_btn = Button(frame2, text="Delete",command=delete)


    def back2():
        root.destroy()
        admin_info()

    btn_back = Button(frame2, text="Back",command=back2)

    
    def show_table():
        # Clear the existing data in the table
        con = sqlite3.Connection('db.db')
        
        for i in student_table.get_children():
            student_table.delete(i)

        if grade_var.get() == gradess[0]:
            resu = con.execute('SELECT stu_name,stu_id,stu_email,year,stu_gpa FROM stud WHERE year = 1').fetchall()
            for student in resu:
                student_table.insert("", "end", values=student)
        elif grade_var.get() == gradess[1]:
            resu = con.execute('SELECT stu_name,stu_id,stu_email,year,stu_gpa FROM stud WHERE year = 2').fetchall()
            for student in resu:
                student_table.insert("", "end", values=student)
        elif grade_var.get() == gradess[2]:
            resu = con.execute('SELECT stu_name,stu_id,stu_email,year,stu_gpa FROM stud WHERE year = 3').fetchall()
            for student in resu:
                student_table.insert("", "end", values=student)
        elif grade_var.get() == gradess[3]:
            resu = con.execute('SELECT stu_name,stu_id,stu_email,year,stu_gpa FROM stud WHERE year = 4').fetchall()
            for student in resu:
                student_table.insert("", "end", values=student)

        con.commit()
        con.close()
        student_table.pack(padx=10, pady=10)
        delete_btn.pack(padx=10, pady=10)
        add_btn.pack(padx=10, pady=10)
        btn_back.pack(padx=10, pady=10)
        frame2.pack(side="right")

    show_btn = Button(frame1, text="Show", command=show_table)

    lbl.grid(column=0, row=0, padx=10, pady=10)
    grades.grid(column=1, row=0, padx=10, pady=10)
    show_btn.grid(column=1, row=1, padx=10, pady=10)

    frame1.pack(side="left")
    root.mainloop()


#mainn()




#from tkinter import *
#from tkinter.ttk import *


first_grade = [
        ("Ahmed Mohamed", 1, 19, "male", 3.1),
        ("Mohamed Ahmed", 2, 19, "male", 3.3),
        ("Yasmine Mohamed", 3, 19, "female", 0.1),
        ("Ahmed Mahamod", 4, 19, "male", 2.5)
    ]
second_grade = [
        ("Wael Ryad", 5, 20, "male", 3.5),
        ("Ahmed Ibrahim", 6, 20, "male", 3.2),
        ("Hossam Ashraf", 7, 20, "male", 2.4),
        ("Aisha Khaled", 8, 20, "female", 1.5)
    ]
third_grade = [
        ("Hegazy Naser", 9, 21, "male", 3.8),
        ("Reda Ahmed", 10, 21, "male", 3.9),
        ("Ahmed Mohamed", 11, 21, "male", 3.7),
        ("Esraa Ahmed", 12, 21, "female", 3.6)
    ]
fourth_grade = [
        ("Mohamed Ahmed", 13, 22, "male", 3.9),
        ("Saad Mohamed", 14, 22, "male", 3.8),
        ("Ahmed Mohamed", 15, 22, "male", 4.0)
    ]

def insert_table(list):
    for student in list:
        student_table.insert("", 'end', values=student)



def show_table():
    if grade_var.get() == gradess[0]:
        insert_table(first_grade)
    elif grade_var.get() == gradess[1]:
        insert_table(second_grade)
    elif grade_var.get() == gradess[2]:
        insert_table(third_grade)
    elif grade_var.get() == gradess[3]:
        insert_table(fourth_grade)
    

    student_table.pack(padx=10, pady=10)
















#--------------------------------------------------------------------#

'''

def select():



    root = Tk()

    subjects = [(1, 'Computer Arch', 3), (2, 'System Analyses', 3), (3, 'Linear Algebra', 2)]

    subject2 = []

    columns = ['id', 'Subject Name', 'Number of hours']
    tree = Treeview(root, columns=columns, show='headings')
    tree.column('Subject Name', width=200, anchor='center')
    tree.column('Number of hours', width=300, anchor='center')
    tree.heading('id', text='Id')
    tree.heading('Subject Name', text='Subject Name')
    tree.heading('Number of hours', text='Number of hours')
    for subject in subjects:
        tree.insert('', 'end', iid=subject[0], values=subject)

    tree2 = Treeview(root, columns=columns, show='headings')
    tree2.column('Subject Name', width=200, anchor='center')
    tree2.column('Number of hours', width=300, anchor='center')
    tree2.heading('id', text='Id')
    tree2.heading('Subject Name', text='Subject Name')
    tree2.heading('Number of hours', text='Number of hours')


    def get_selected():
        for selected in tree.selection():
            print(tree.item(selected, 'values'))


    btn = Button(root, text='Save', command=get_selected)


    def delete_selected():
        for selected in tree2.selection():
            tree2.delete(selected)


    btn_Del = Button(root, text='Delete', command=delete_selected)


    def add_selected():
        for selected in tree.selection():
            subject2 = tree.item(selected)['values']
            tree2.insert('', 'end', values=subject2)


    btn_Add = Button(root, text='Add', command=add_selected)
    
    def logout():
        root.destroy()
        student_information()
        
    btn_back = Button(root, text='Back', command=logout)

    scrollbar = Scrollbar(root, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.grid(row=0, column=0, columnspan=2)

    tree2.grid(row=1, column=0, columnspan=2)

    btn.grid(row=2, column=0, columnspan=2)
    btn_Add.grid(row=3, column=0, columnspan=2)
    btn_Del.grid(row=4, column=0, columnspan=2)
    btn_back.grid(row=5, column=0, columnspan=2)
    scrollbar.grid(row=0, column=2, columnspan=2, sticky=N + S)
    style = Style()
    style.configure('Treeview', font=('Arial', 12), rowheight=30, foreground='#e5e5e5', background='#14213d')
    style.map('Treeview', foreground=[('selected', '#000000')], background=[('selected', '#fca311')])
    style.configure('Treeview.Heading', font=('Tahoma', 14))
    root.mainloop()





'''





def select():



    root = Tk()

    subjects = [(1, 'Computer Arch', 3), (2, 'System Analyses', 3), (3, 'Linear Algebra', 2)]

    subject2 = []
    con = sqlite3.Connection('db.db')

    columns = ['id', 'Subject Name', 'Number of hours']
    tree = Treeview(root, columns=columns, show='headings')
    tree.column('Subject Name', width=200, anchor='center')
    tree.column('Number of hours', width=300, anchor='center')
    tree.heading('id', text='كود المقرر')
    tree.heading('Subject Name', text='اسم المقرر')
    tree.heading('Number of hours', text='عدد الساعات')
    
    res = con.execute('SELECT course_id,course_name,course_hours,course_code FROM course WHERE year = 1').fetchall()
    for sub in res:
        tree.insert("",'end',iid=sub[0],values=sub )
    con.commit()
    con.close()
    
    
    #for subject in subjects:
        #tree.insert('', 'end', iid=subject[0], values=subject)

    tree2 = Treeview(root, columns=columns, show='headings')
    tree2.column('Subject Name', width=200, anchor='center')
    tree2.column('Number of hours', width=300, anchor='center')
    tree2.heading('id', text='كود المقرر')
    tree2.heading('Subject Name', text='اسم المقرر')
    tree2.heading('Number of hours', text='عدد الساعات')


    def get_selected():
        con = sqlite3.Connection('db.db')
        for selected in tree2.get_children():
            subje = tree2.item(selected)['values']
            con.execute('''INSERT INTO regestered(subject_id,student_id) VALUES(?,?)''',(subje[0],1))
            #print(tree.item(selected, 'values'))
            print(subje[0])
        con.commit()
        con.close()
        logout()
        
        
            


    btn = Button(root, text='Save', command=get_selected)


    def delete_selected():
        con = sqlite3.Connection('db.db')
        for selected in tree2.selection():
            tree2.delete(selected)
        for item in tree.get_children():
            tree.delete(item)
        res = con.execute('SELECT course_id,course_name,course_hours,course_code FROM course WHERE year = 1').fetchall()
        for sub in res:
            tree.insert("",'end',iid=sub[0],values=sub )
        con.commit()
        con.close()


    btn_Del = Button(root, text='Delete', command=delete_selected)


    def add_selected():
        for selected in tree.selection():
            subject2 = tree.item(selected)['values']
            tree2.insert('', 'end', values=subject2)
        for selected in tree.selection():
            tree.delete(selected)


    btn_Add = Button(root, text='Add', command=add_selected)
    
    def logout():
        root.destroy()
        student_information()
        
    btn_back = Button(root, text='Back', command=logout)

    scrollbar = Scrollbar(root, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.grid(row=0, column=0, columnspan=2)

    tree2.grid(row=1, column=0, columnspan=2)

    btn.grid(row=2, column=0, columnspan=2)
    btn_Add.grid(row=3, column=0, columnspan=2)
    btn_Del.grid(row=4, column=0, columnspan=2)
    btn_back.grid(row=5, column=0, columnspan=2)
    scrollbar.grid(row=0, column=2, columnspan=2, sticky=N + S)
    style = Style()
    style.configure('Treeview', font=('Arial', 12), rowheight=30, foreground='#e5e5e5', background='#14213d')
    style.map('Treeview', foreground=[('selected', '#000000')], background=[('selected', '#fca311')])
    style.configure('Treeview.Heading', font=('Tahoma', 14))
    root.mainloop()












#------------------------------------------------------------------#

'''
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
    


    def backGround_img():
        BGStudent_img=Image.open('imagess\istockphoto-176817032-1024x1024 (1).jpg') 
        img_tkStudent=ImageTk.PhotoImage(BGStudent_img)





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
           tree.insert("", END, values=course)

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

'''


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
       con.commit()
       con.close()
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



#-----------------------------------------------------------------------------------------------#
def admin_info():
    
    root = Tk()
    root['bg']='light blue'
    root.title("بيانات المشرف")

    font1=('Arial',17,'bold')
    font2=('Arial',15)
    font3 =('Arial',14,'bold')

    w = 600
    h = 400

    screenwidth = root.winfo_screenwidth()

    screenheight = root.winfo_screenheight()

    x = int((screenwidth-w)/2)
    y = int((screenheight-h)/2)

    root.geometry(f'{w}x{h}+{x}+{y}')

    root.resizable(False,False)


    def logout():
        root.destroy()
        main()

    def modifay_student():
        root.destroy()
        mainn()

    def modifay_corces():
        root.destroy()
        add_corces()

    lbl1 = Label(root, text = ': اسم الطالب -', font =font1, bg= 'light blue')
    lbl2 = Label(root, text = ': الايميل الجامعي -',font =font1, bg= 'light blue')
    lbl3 = Label(root, text = ': الرقم القومي -', font =font1, bg= 'light blue')
#lbl4 = Label(root, text = ': رقم التليفون -', font =font1, bg= 'light blue')

    lbl1.place(x=450, y=20)
    lbl2.place(x=435, y=70)
    lbl3.place(x=445, y=120)
#lbl4.place(x=460, y=170)

    lbl5 = Label(root, text = 'شريف ايهاب صالح', font=font2, bg= 'white')
    lbl6 = Label(root, text = 'sherif45871@fci.bu.edu.eg', font=font2, bg= 'white')
    lbl7 = Label(root, text = '15963589476125', font=font2, bg= 'white')
#lbl8 = Label(root, text = '01045692831', font=font2, bg= 'white')

    lbl5.place(x=298, y=23)
    lbl6.place(x=190, y=72)
    lbl7.place(x=272, y=124)
#lbl8.place(x=330, y=174)

    
    btn1 = Button(root, text='تعديل المقررات', font=font3, bg= 'white',command = modifay_corces)
    btn2 = Button(root, text='تعديل الطلاب', font=font3, bg= 'white', command = modifay_student)
    btn3 = Button(root, text='تسجيل الخروج', font=font3, bg= 'white', command = logout)

    btn3.place(x=245, y=330)
    btn2.place(x=80, y=280)
    btn1.place(x=420, y=280)

    root.mainloop()




#----------------------------------------------------------------------------------------------------------#
def student_information():
    
    root = Tk()
    root['bg']='light blue'
    root.title("بيانات الطالب")
    font1=('Arial',17,'bold')
    font2=('Arial',15)
    font3 =('Arial',14,'bold')

    w = 600
    h = 400 

    screenwidth = root.winfo_screenwidth()

    screenheight = root.winfo_screenheight()

    x = int((screenwidth-w)/2)
    y = int((screenheight-h)/2)

    root.geometry(f'{w}x{h}+{x}+{y}')
    
    root.resizable(False,False)

    def logout():
        root.destroy()
        main()
    def student_corces():
        root.destroy()
        stuudent_corces_regestered()
        #student_info()
    def student_selection():
        root.destroy()
        select()

#img = Image.open('images/image.jpeg')

#img_tk = ImageTk.PhotoImage(img)
#lbl = Label(root, image=img_tk)
#lbl.pack()
    
        
    lbl1 = Label(root, text = ': الاسم -', font =font1, bg= 'light blue')
    lbl2 = Label(root, text = ': الفرقه -',font =font1, bg= 'light blue')
    lbl3 = Label(root, text = ': المعدل التراكمي -',font =font1, bg= 'light blue')
    lbl4 = Label(root, text = ': عدد الساعات المجتازه -',font =font1, bg= 'light blue')

    lbl1.place(x=510, y=20)
    lbl2.place(x=505, y=70)
    lbl3.place(x=435, y=120)
    lbl4.place(x=387, y=170)



    lbl5 = Label(root, text = 'شريف ايهاب صالح', font=font2, bg= 'white')
    lbl6 = Label(root, text = 'الثانيه', font=font2, bg= 'white')
    lbl7 = Label(root, text = '3.5', font=font2, bg= 'white')
    lbl8 = Label(root, text = '66', font=font2, bg= 'white')

    lbl5.place(x=372, y=23)
    lbl6.place(x=460, y=72)
    lbl7.place(x=400, y=124)
    lbl8.place(x=357, y=174)



    btn1 = Button(root, text='تسجيل المقررات', font=font3, bg= 'white', command = student_selection)
    btn2 = Button(root, text='بيان بالمقررات المسجله', font=font3, bg= 'white', command = student_corces)
    btn3 = Button(root, text='تسجيل الخروج', font=font3, bg= 'white',command = logout)

    btn3.place(x=270, y=320)
    btn2.place(x=70, y=250)
    btn1.place(x=420, y=250)

    root.mainloop()



#-------------------------------------------------------------------------------------------------#

def main():
    flag = 5  
    root = Tk()
    frame1 = Frame(root)
    root.title('Log in')
    root.geometry('500x500')
    lbl_user = Label(frame1, text="Username", fg="black", font=("Tahoma", 12, 'bold'),width=20, height=5)
    txt_user = Entry(frame1)
    lbl_pass = Label(frame1, text="Password", fg="black", font=("Tahoma", 12, 'bold'),width=20, height=5)
    txt_pass = Entry(frame1,show='*')
    def display_option():
        choice = rbtn_var.get()
        #messagebox.showinfo("Info", "You chose {}".format(choice))
        if choice == "Admin":
            flag = 0
        elif choice == "Student":
            flag = 1
        return flag

    def check_user():
        valid_user = 'Shrouk'
        valid_pass = '123'
        username = txt_user.get()
        password = txt_pass.get()
        if username == valid_user and password == valid_pass:
            #messagebox.showinfo('Info', 'Valid data')
            if display_option() == 1:
                root.destroy()
                student_information()
            elif display_option() == 0:
                root.destroy()
                admin_info()
                
        else:
            messagebox.showerror('Error', 'Invalid data')
        
    rbtn_var = StringVar()
    rbtn_var.set('Admin')
    rbtn1 = Radiobutton(frame1, text="Admin", value='Admin', variable=rbtn_var, font='bold', command=display_option)
    rbtn2 = Radiobutton(frame1, text="Student", value='Student', variable=rbtn_var, font='bold', command=display_option)
    btn = Button(frame1, text="Log in",font='bold', command=check_user, background='darkred', foreground='white')
    lbl_user.grid(row=0, column=0)
    txt_user.grid(row=0, column=1)
    lbl_pass.grid(row=1, column=0)
    txt_pass.grid(row=1, column=1)
    rbtn1.grid(row=2, column=0)
    rbtn2.grid(row=2, column=1)
    btn.grid(row=3, column=0, columnspan=2)
    frame1.grid(row=0, column=0, columnspan=2)
    root.mainloop()

main()
