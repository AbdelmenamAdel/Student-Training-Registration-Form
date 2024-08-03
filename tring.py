import sqlite3
from tkinter import N, S, VERTICAL, Button, Scrollbar, Tk
from tkinter.ttk import Style, Treeview


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
        # student_information()
        
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
select()