from tkinter import *
from PIL import Image , ImageTk


root = Tk()
root['bg']='light blue'
root.title("بيانات الطالب")
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

#img = Image.open('images/image.jpeg')

#img_tk = ImageTk.PhotoImage(img)
#lbl = Label(root, image=img_tk)
#lbl.pack()
lbl1 = Label(root, text = ': الاسم -', font =font1, bg= 'light blue')
lbl2 = Label(root, text = ': الفرقه -',font =font1, bg= 'light blue')
lbl3 = Label(root, text = ': المعدل التراكمي -',font =font1, bg= 'light blue')
lbl4 = Label(root, text = ': عدد الساعات المجتازه -',font =font1, bg= 'light blue')

lbl1.place(x=510, y=20)
lbl2.place(x=505, y=70)
lbl3.place(x=435, y=120)
lbl4.place(x=387, y=170)



lbl5 = Label(root, text = 'شريف ايهاب صالح', font=font2, bg= 'white')
lbl6 = Label(root, text = 'الثانيه', font=font2, bg= 'white')
lbl7 = Label(root, text = '3.75', font=font2, bg= 'white')
lbl8 = Label(root, text = '66', font=font2, bg= 'white')

lbl5.place(x=372, y=23)
lbl6.place(x=460, y=72)
lbl7.place(x=400, y=124)
lbl8.place(x=357, y=174)



btn1 = Button(root, text='تسجيل المقررات', font=font3, bg= 'white')
btn2 = Button(root, text='بيان بالمقررات المسجله', font=font3, bg= 'white')
btn3 = Button(root, text='تسجيل الخروج', font=font3, bg= 'white')

btn3.place(x=270, y=320)
btn2.place(x=70, y=250)
btn1.place(x=420, y=250)

root.mainloop()