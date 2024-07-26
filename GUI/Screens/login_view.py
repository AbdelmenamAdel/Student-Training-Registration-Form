from tkinter import StringVar, Tk, Label, Entry, Button, messagebox, Frame
from constants import *
class LoginView:
    def __init__(self):
        self.root = Tk()

        # Create the Root screen frame
        self.root_frame = Frame(self.root, bg=background_color, padx=padx, pady=pady)
        self.root_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Set title and screen size
        self.root.title("Login Screen")
        self.root.geometry(login_geometry)
        self.root.resizable(False, False)

        # Set background color
        self.root.configure(bg=background_color)  # Light gray background

        # Style labels
        username_label = Label(self.root_frame, text="Username:", font=(font_style_arial, font_size_12, "bold"), fg=black)  # Black text
        username_label.grid(row=0, column=0, pady=pady, padx=padx)  # Add padding

        password_label = Label(self.root_frame, text="Password:", font=(font_style_arial, font_size_12, "bold"), fg=black)
        password_label.grid(row=1, column=0, pady=pady, padx=padx)

        # Style entry fields
        self.username = StringVar()
        username_entry = Entry(self.root_frame, textvariable=self.username, font=(font_style_arial, font_size_12), bg=white, fg=black)  # White background, black text
        username_entry.grid(row=0, column=1, pady=pady, padx=padx)

        self.password = StringVar()
        password_entry = Entry(self.root_frame, textvariable=self.password, font=(font_style_arial, font_size_12), show="*", bg=white, fg=black)
        password_entry.grid(row=1, column=1, pady=pady, padx=padx)

        # Style button
        login_button = Button(self.root_frame, text="Login", command=self.login_attempt, font=(font_style_arial, font_size_12, "bold"), bg=primary_color, fg=white, width=10)  # Green button, white text
        login_button.grid(row=2, columnspan=2, pady=10, padx=10)

        self.root.mainloop()

    def login_attempt(self):
        username = self.username.get()
        password = self.password.get()
        # Replace this with your login validation logic (checking a database)
        if username == "admin" and password == "1234":
            print("Login successful!")
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()  # Close the login screen
            from shams import student_info # Open the main screen
            student_info()
        else:
            print("Invalid username or password")
            messagebox.showerror("Error", "Invalid username or password")

    def open_main_screen(self):
        main_screen = Tk()
        main_screen.title("Main Screen")
        main_screen.geometry("600x400")
        Label(main_screen, text="Welcome to the Main Screen!", font=("Arial", 16)).pack(pady=20)
        main_screen.mainloop()
