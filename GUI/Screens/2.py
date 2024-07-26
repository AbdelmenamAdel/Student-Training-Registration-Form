from tkinter import *

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

lbl1 = Label(root, text = ': اسم الطالب -', font =font1, bg= 'light blue')
lbl2 = Label(root, text = ': الايميل الجامعي -',font =font1, bg= 'light blue')
lbl3 = Label(root, text = ': الرقم القومي -', font =font1, bg= 'light blue')

lbl1.place(x=450, y=20)
lbl2.place(x=435, y=70)
lbl3.place(x=445, y=120)

lbl5 = Label(root, text = 'شريف ايهاب صالح', font=font2, bg= 'white')
lbl6 = Label(root, text = 'sherif45871@fci.bu.edu.eg', font=font2, bg= 'white')
lbl7 = Label(root, text = '15963589476125', font=font2, bg= 'white')

lbl5.place(x=298, y=23)
lbl6.place(x=190, y=72)
lbl7.place(x=272, y=124)

btn1 = Button(root, text='تعديل المقررات', font=font3, bg= 'white')
btn2 = Button(root, text='تعديل الطلاب', font=font3, bg= 'white')
btn3 = Button(root, text='تسجيل الخروج', font=font3, bg= 'white')

btn3.place(x=245, y=330)
btn2.place(x=80, y=280)
btn1.place(x=420, y=280)

root.mainloop()