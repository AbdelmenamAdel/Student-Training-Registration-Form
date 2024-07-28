from tkinter import *
from tkinter.ttk import Treeview
from PIL import ImageTk, Image
from constants import *
class StudentInfoApp:
    def __init__(self):
        self.root = self.create_root_window()
        # self.create_background_image()
        self.create_student_info_frame()
        self.create_courses_table()
        self.create_back_button()
        self.root.mainloop()

    def create_root_window(self):
        root = Tk()
        root.title("نظام المقررات")
        root.geometry(geometry)
        return root

    def create_background_image(self):
        # Create a canvas to hold the background image
        self.canvas = Canvas(self.root, width=650, height=450)
        self.canvas.pack(fill=BOTH, expand=True)

        # Load and resize the background image
        bg_image = Image.open("assets/bg.png")
        bg_image = bg_image.resize((int(width), int(height)))
        self.bg_image = ImageTk.PhotoImage(bg_image)

        # Add the background image to the canvas
        self.canvas.create_image(0, 0, image=self.bg_image, anchor=NW)

    def create_student_info_frame(self):
        student_name = "شمس مجدي"
        student_gpa = 3.75
        student_year = "الفرقة الثالثة"

        student_frame = Frame(self.root)
        student_frame.pack(pady=pady20)

        student_name_lbl = Label(student_frame, text=f"اسم الطالب :  {student_name}", font=("Arial", 12))
        student_name_lbl.grid(row=0, column=1, padx=10, pady=5)

        student_gpa_lbl = Label(student_frame, text=f"المعدل التراكمي :  {student_gpa}", font=("Arial", 12))
        student_gpa_lbl.grid(row=0, column=0, padx=10, pady=5)

        student_year_lbl = Label(student_frame, text=f"العام الدراسى :   {student_year}", font=("Arial", 12))
        student_year_lbl.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        student_frame.place(relx=0.5, rely=0.3, anchor=CENTER)

    def create_courses_table(self):
        courses = [
            ("A", 3, "Structural programming", "CS101"),
            ("B+", 3, "Discrete mathematics", "MA102"),
            ("B", 3, "Physics", "PH103"),
            ("A-", 2, "English", "EN104")
        ]

        courses_frame = Frame(self.root)
        courses_frame.pack(pady=pady20)

        columns = ("grade", "credits", "course_name", "course_code")
        tree = Treeview(courses_frame, columns=columns, show="headings")

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

        courses_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

    def create_back_button(self):
        back_button = Button(self.root, text="BACK", font=("Arial", 12, 'bold'), fg="white", bg="dark blue", command=self.pop)
        back_button.pack(side=LEFT, anchor="sw", padx=padx20, pady=pady20)
    def pop(self):
        self.root.destroy()
        from login_view import LoginView
        LoginView()

# StudentInfoApp()
