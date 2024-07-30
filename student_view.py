
from tkinter import *
from constants import*
from models import StudentModel
class StudentView:
    def __init__(self,student:StudentModel):
        self.root = Tk()
        self.student=student
        self.root_frame = Frame(self.root, bg=background_color)
        self.root_frame.pack(fill='both', expand=True)
        self.root_frame.place(relx=0.5, rely=0.5, anchor='center')
        self.run()

    def run(self):
        self.configure_root()
        self.create_widgets()
        self.position_widgets()
        self.root.mainloop()

    def configure_root(self):
        self.root.configure(bg=background_color)
        self.root.title("بيانات الطالب")
        self.root.geometry(geometry)
        self.root.resizable(False, False)

    def create_widgets(self):
        font_title = ('Arial', 17, 'bold')
        font_content = ('Arial', 15)
        font_button = ('Arial', 14, 'bold')

        # Labels
        self.lbl1 = Label(self.root_frame, text=': اسم الطالب -', font=font_title, bg=background_color)
        self.lbl2 = Label(self.root_frame, text=': الايميل الجامعي -', font=font_title, bg=background_color)
        self.lbl3 = Label(self.root_frame, text=': الرقم القومي -', font=font_title, bg=background_color)
        self.lbl4 = Label(self.root_frame, text=': المعدل التراكمي -', font=font_title, bg=background_color)
        self.lbl5 = Label(self.root_frame, text=': الفرقه -', font=font_title, bg=background_color)
        self.lbl6 = Label(self.root_frame, text=': الساعات المجتازه -', font=font_title, bg=background_color)

        self.lbl_student_name = Label(self.root_frame, text=self.student[1], font=font_content, bg=background_color)
        self.lbl_student_email = Label(self.root_frame, text=self.student[3], font=font_content, bg=background_color)
        self.lbl_student_id = Label(self.root_frame, text=self.student[4], font=font_content, bg=background_color)
        self.lbl_student_gpa = Label(self.root_frame, text=self.student[5], font=font_content, bg=background_color)
        self.lbl_student_grade = Label(self.root_frame, text=self.student[6], font=font_content, bg=background_color)
        self.lbl_student_passedHours = Label(self.root_frame, text=self.student[7], font=font_content, bg=background_color)

        # Buttons
        self.btn_edit_courses = Button(self.root_frame, text='تسجيل المقررات', font=font_button,  bg=primary_color, fg=white,width=12,command=self.modifay_cources)
        self.btn_edit_students = Button(self.root_frame, text='بيان بالمقررات المسجله', font=font_button,  bg=primary_color, fg=white,width=12,command=self.modifay_student)
        self.btn_logout = Button(self.root_frame, text='تسجيل الخروج', font=font_button,  bg=primary_color, fg=white,width=12,command=self.logout)
    def logout(self):
        self.root.destroy()
        from login_view import LoginView
        LoginView()
    def modifay_student(self):
        self.root.destroy()
       
        
    def modifay_cources(self):
        self.root.destroy()
        # add_corces()

    def position_widgets(self):
        # Position labels using grid
        self.lbl1.grid(row=0, column=3, sticky='e', padx=10, pady=10)
        self.lbl_student_name.grid(row=0, column=0, sticky='w', padx=padx10, pady=pady10)

        self.lbl2.grid(row=1, column=3, sticky='e', padx=10, pady=10)
        self.lbl_student_email.grid(row=1, column=0, sticky='w', padx=padx10, pady=pady10)

        self.lbl3.grid(row=2, column=3, sticky='e', padx=padx10, pady=pady10)
        self.lbl_student_id.grid(row=2, column=0, sticky='w', padx=padx10, pady=pady10)
       
        self.lbl4.grid(row=3, column=3, sticky='e', padx=10, pady=10)
        self.lbl_student_gpa.grid(row=3, column=0, sticky='w', padx=padx10, pady=pady10)

        self.lbl5.grid(row=4, column=3, sticky='e', padx=10, pady=10)
        self.lbl_student_grade.grid(row=4, column=0, sticky='w', padx=padx10, pady=pady10)

        self.lbl6.grid(row=5, column=3, sticky='e', padx=padx10, pady=pady10)
        self.lbl_student_passedHours.grid(row=5, column=0, sticky='w', padx=padx10, pady=pady10)

        # Position buttons using grid
        self.btn_edit_courses.grid(row=6, column=1,padx=15, pady=40, sticky='e')
        self.btn_edit_students.grid(row=6, column=2, padx=15, pady=40, sticky='w')
        self.btn_logout.grid(row=7,  columnspan=4, pady=0, sticky='s')
