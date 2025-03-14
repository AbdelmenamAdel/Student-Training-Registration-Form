from tkinter import *
from tkinter.ttk import Treeview
from PIL import ImageTk, Image
from constants import *
from courses_registration_crud import CoursesRegistrationCRUD
from models import StudentModel
from student_view import StudentView

class StudentInfoView:
    def __init__(self,student: StudentModel):
        self.student=student
        self.subject_manager = CoursesRegistrationCRUD(self.student[3])
        self.root = self.create_root_window()
        self.create_background_image()
        self.root_frame = Frame(self.root,padx=padx20, pady=pady20)
        self.root_frame.pack_propagate(False)
        self.create_student_info_frame()
        self.create_courses_table()
        self.create_back_button()
        self.root.mainloop()

    def create_root_window(self):
        root = Tk()
        root.configure(bg="#2c3e50")
        root.resizable(False, False)
        root.title("نظام المقررات")
        root.geometry(geometry)
        return root

    def create_background_image(self):
        # Create a canvas to hold the background image
        self.canvas = Canvas(self.root, width=650, height=450)
        self.canvas.pack(fill=BOTH, expand=True)

        # Load and resize the background image
        bg_image = Image.open("assets/bg.jpg")
        bg_image = bg_image.resize((int(width), int(height)))
        self.bg_image = ImageTk.PhotoImage(bg_image)

        # Add the background image to the canvas
        self.canvas.create_image(0, 0, image=self.bg_image, anchor=NW)
    def create_student_info_frame(self):
        student_name = self.student[1]
        student_gpa = self.student[5]
        student_year = self.student[6]

        student_name_lbl = Label(self.root_frame, text=f"Student Name :      {student_name}", font=("Arial", 12))
        student_name_lbl.grid(row=0, column=0, padx=10, pady=5)

        student_gpa_lbl = Label(self.root_frame, text=f"Student GPA :      {student_gpa}", font=("Arial", 12))
        student_gpa_lbl.grid(row=0, column=1, padx=10, pady=5)

        student_year_lbl = Label(self.root_frame, text=f"Student Level :      {student_year}", font=("Arial", 12))
        student_year_lbl.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        self.root_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def create_courses_table(self):
        courses = [
            ( "Structural programming", 3, "CS101"),
            ( "Discrete mathematics", 3, "MA102"),
            ( "Physics", 3, "PH103"),
            ( "English",  2,"EN104")
        ]
            
        columns = ( "course_name","credits", "course_code")
        tree = Treeview(self.root_frame, columns=columns, show="headings",)

        tree.heading("course_code", text="كود المقرر")
        tree.heading("credits", text="عدد الساعات")
        tree.heading("course_name", text="اسم المقرر")

        tree.column("course_name", width=170)
        tree.column("credits", width=80, anchor="center")
        tree.column("course_code", width=100, anchor="center")
        
        student_id = self.subject_manager.get_student_id()
        subjects = self.subject_manager.get_registered_subjects(student_id)
        for sub in subjects:
            tree.insert("", 'end', iid=sub[0], values=(sub[1],sub[3],sub[2]))
        tree.grid(row=2, column=0, columnspan=2, pady=10)

    def create_back_button(self):
        back_button = Button(self.root_frame, text="BACK", font=("Arial", 12, 'bold'), fg="white", bg="dark blue", command=self.pop)
        back_button.pack(side=LEFT, anchor="sw", padx=padx20, pady=pady20)

    def pop(self):
        self.root.destroy()
        StudentView(student=self.student)

