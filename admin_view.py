from tkinter import Frame, Tk, Label, Button

from models import AdminModel


class AdminView:
    def __init__(self,admin:AdminModel):
        self.root = Tk()
        self.admin=admin
        self.root_frame = Frame(self.root, bg='light blue')
        self.root_frame.pack(fill='both', expand=True)
        self.root_frame.place(relx=0.5, rely=0.5, anchor='center')
        self.run()

    def run(self):
        self.configure_root()
        self.create_widgets()
        self.position_widgets()
        self.root.mainloop()

    def configure_root(self):
        self.root.configure(bg='light blue')
        self.root.title("بيانات المشرف")
        width = 600
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.resizable(False, False)

    def create_widgets(self):
        font_title = ('Arial', 17, 'bold')
        font_content = ('Arial', 15)
        font_button = ('Arial', 14, 'bold')

        # Labels
        self.lbl1 = Label(self.root_frame, text=': اسم المشرف -', font=font_title, bg='light blue')
        self.lbl2 = Label(self.root_frame, text=': الايميل الجامعي -', font=font_title, bg='light blue')
        self.lbl3 = Label(self.root_frame, text=': الرقم القومي -', font=font_title, bg='light blue')

        self.lbl_student_name = Label(self.root_frame, text=self.admin[1], font=font_content, bg='white')
        self.lbl_student_email = Label(self.root_frame, text=self.admin[2], font=font_content, bg='white')
        self.lbl_student_id = Label(self.root_frame, text=self.admin[3], font=font_content, bg='white')

        # Buttons
        self.btn_edit_courses = Button(self.root_frame, text='تعديل المقررات', font=font_button, bg='white')
        self.btn_edit_students = Button(self.root_frame, text='تعديل الطلاب', font=font_button, bg='white')
        self.btn_logout = Button(self.root_frame, text='تسجيل الخروج', font=font_button, bg='white')

    def position_widgets(self):
        # Position labels using grid
        self.lbl1.grid(row=0, column=2, sticky='e', padx=10, pady=10)
        self.lbl_student_name.grid(row=0, column=1, sticky='w', padx=10, pady=10)

        self.lbl2.grid(row=1, column=2, sticky='e', padx=10, pady=10)
        self.lbl_student_email.grid(row=1, column=1, sticky='w', padx=10, pady=10)

        self.lbl3.grid(row=2, column=2, sticky='e', padx=10, pady=10)
        self.lbl_student_id.grid(row=2, column=1, sticky='w', padx=10, pady=10)

        # Position buttons using grid
        self.btn_edit_courses.grid(row=3, column=2, padx=10, pady=20, sticky='e')
        self.btn_edit_students.grid(row=3, column=1, padx=10, pady=20, sticky='w')
        self.btn_logout.grid(row=4, column=1, columnspan=2, pady=10)


