from tkinter import Tk, Label, Entry, Button,messagebox,Frame
from GUI.Constants.constants import *
class login_view():
    def login_attempt(self, username_entry, password_entry,email_entry):
        self.username = username_entry.get()
        self.password = password_entry.get()
        # ! Replace this with your login validation logic (checking a database)
        if self.username == "admin" and self.password == "1234":
            print("Login successful!")
            messagebox.showinfo("Success", "Login successful!")
        else:
            print("Invalid username or password")
            messagebox.showerror("Error", "Invalid username or password")
        
    # ! Create the Root screen 
    root = Tk()

    # ! Create the Root screen frame
    root_frame = Frame(root, bg=background_color, padx=padx, pady=pady)
    root_frame.place(relx=0.5, rely=0.5,anchor='center')

    # ! Set title and screen size
    root.title("Login Screen")
    root.geometry(login_geometry)
    root.resizable(False, False)

    # ! Set background color
    root.configure(bg=background_color)  # Light gray background

    # ! Style labels
    username_label = Label(root_frame, text="Username:", font=(font_style_arial, font_size_12, "bold"), fg=black)  # Black text
    username_label.grid(row=0, column=0, pady=pady, padx=padx)  # Add padding

    password_label = Label(root_frame, text="Password:", font=(font_style_arial, font_size_12, "bold"), fg=black)
    password_label.grid(row=1, column=0, pady=pady, padx=padx)

    # ! Style entry fields
    username_entry = Entry(root_frame, font=(font_style_arial, font_size_12), bg=white, fg=black)  # White background, black text
    username_entry.grid(row=0, column=1, pady=pady, padx=padx)

    password_entry = Entry(root_frame, font=(font_style_arial, font_size_12), show="*", bg=white, fg=black)
    password_entry.grid(row=1, column=1, pady=pady, padx=padx)

    # ! Style button
    login_button = Button(root_frame, text="Login", command=login_attempt, font=(font_style_arial, font_size_12, "bold"), bg=primary_color, fg=white,width=10)  # Green button, white text
    login_button.grid(row=2, columnspan=2, pady=10, padx=10)

    root.mainloop()
