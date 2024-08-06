from tkinter import Radiobutton, StringVar, Tk, Label, Entry, Button, messagebox, Frame
import lib
from admin_crud_operations import AdminCRUD
from constants import *
from student_crud_operations import StudentCRUD
class LoginView:
    def __init__(self):
        self.root = Tk()

        # Create the Root screen frame
        self.root_frame = Frame(self.root, bg=background_color, padx=padx20, pady=pady20)
        self.root_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Set title and screen size
        self.root.title("Login Screen")
        self.root.geometry(geometry)
        self.root.resizable(False, False)

        # Set background color
        self.root.configure(bg=background_color)  # Light gray background

        # Style labels
        username_label = Label(self.root_frame, text="Username:", font=(font_style_arial, font_size_12, "bold"), fg=black)  # Black text
        username_label.grid(row=0, column=0, pady=pady20, padx=padx20)  # Add padding

        password_label = Label(self.root_frame, text="Password:", font=(font_style_arial, font_size_12, "bold"), fg=black)
        password_label.grid(row=1, column=0, pady=pady20, padx=padx20)

        # Style entry fields
        self.username = StringVar()
        username_entry = Entry(self.root_frame, textvariable=self.username, font=(font_style_arial, font_size_12), bg=white, fg=black)  # White background, black text
        username_entry.grid(row=0, column=1, pady=pady20, padx=padx20)

        self.password = StringVar()
        password_entry = Entry(self.root_frame, textvariable=self.password, font=(font_style_arial, font_size_12), show="*", bg=white, fg=black)
        password_entry.grid(row=1, column=1, pady=pady20, padx=padx20)

        # Style radio buttons
        self.rbtn_var = StringVar()
        self.rbtn_var.set('Admin')
        rbtn1 = Radiobutton(self.root_frame, text="Admin", value='Admin', variable=self.rbtn_var, font='bold', command=self.display_option)
        rbtn2 = Radiobutton(self.root_frame, text="Student", value='Student', variable=self.rbtn_var, font='bold', command=self.display_option)
        rbtn1.grid(row=2, column=0, pady=pady20, padx=padx20)
        rbtn2.grid(row=2, column=1, pady=pady20, padx=padx20)
        # Style button
        login_button = Button(self.root_frame, text="Login", command=self.login_attempt, font=(font_style_arial, font_size_12, "bold"), bg=primary_color, fg=white, width=btn_width)  # ! Green button, white text
        login_button.grid(row=3, columnspan=2, pady=10, padx=10)
        self.root.mainloop()
    def display_option(self):
        choice = self.rbtn_var.get()
        if choice == "Admin":
            return 0
        elif choice == "Student":
            return 1
    def login_attempt(self):
        username = self.username.get()
        password = self.password.get()
        if (self.display_option() == 0):
            self.login_admin(username, password)
        elif (self.display_option() == 1):
            self.login_student(username, password)
    def login_admin(self, username, password):       
        admin=AdminCRUD()
        res=admin.search_admin(username, password)
        if res:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()  # !Close the login screen
            from admin_view import AdminView # !Open the main screen
            AdminView(admin=res)
        else:
            print("Invalid username or password")
            messagebox.showerror("Error", "Invalid username or password")

    def login_student(self, username, password):
        student=StudentCRUD()
        res=student.search_student(username,password)
        print(res)
        if res:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()  # !Close the login screen
            from student_view import StudentView
            StudentView(student=res)
        else:
            print("Invalid username or password")
            messagebox.showerror("Error", "Invalid username or password")
