from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import ImageTk, Image

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
        root.geometry("650x450")
        title_lbl = Label(root, text="بيان المقررات", font=("Arial", 16))
        title_lbl.pack()
        return root

    # def create_background_image(self):
    #     canvas_width = 650
    #     canvas_height = 450
    #     canvas = Canvas(self.root, width=canvas_width, height=canvas_height)
    #     background_image = ImageTk.PhotoImage(Image.open("assets/bg.png"))
    #     canvas.create_image(0, 0, image=background_image, anchor=NW)
    #     canvas.image = background_image  # Keep a reference to avoid garbage collection
    #     canvas.pack(fill=BOTH, expand=True)

    def create_student_info_frame(self):
        student_name = "شمس مجدي"
        student_gpa = 3.75
        student_year = "الفرقة الثالثة"

        student_frame = Frame(self.root)
        student_frame.pack(pady=10)

        student_name_lbl = Label(student_frame, text=f"اسم الطالب: {student_name}", font=("Arial", 12))
        student_name_lbl.grid(row=0, column=1, padx=10, pady=5)

        student_gpa_lbl = Label(student_frame, text=f"المعدل التراكمي: {student_gpa}", font=("Arial", 12))
        student_gpa_lbl.grid(row=0, column=0, padx=10, pady=5)

        student_year_lbl = Label(student_frame, text=f"العام الدراسى: {student_year}", font=("Arial", 12))
        student_year_lbl.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

    def create_courses_table(self):
        courses = [
            ("A", 3, "Structural programming", "CS101"),
            ("B+", 3, "Discrete mathematics", "MA102"),
            ("B", 3, "Physics", "PH103"),
            ("A-", 2, "English", "EN104")
        ]

        courses_frame = Frame(self.root)
        courses_frame.pack(pady=10)

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

    def create_back_button(self):
        back_button = Button(self.root, text="BACK", font=("Arial", 12, 'bold'), fg="white", bg="dark blue", command=self.root.quit)
        back_button.pack(side=LEFT, anchor="sw", padx=7, pady=5)

# if __name__ == "__main__":
app = StudentInfoApp()
