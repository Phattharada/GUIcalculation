from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook
from tkinter import messagebox
GUI = Tk()
GUI.title('My program')
GUI.geometry('500x600')

#########################################

def math_additional():
	GUI2 = Toplevel()
	GUI2.title('หน้าต้างคณิตศาสตร์')
	GUI2.geometry('500x400')

	def Add():
		messagebox.showinfo('การบวก','ตัวอย่าง : 1+1 = 2')
	image_object = PhotoImage(file='object.png')

	logo2=ttk.Label(T2,text='object',image=image_object)
	logo2.pack()

	B = ttk.Button(GUI2,text='ตัวอย่างการบวกเลข',command=Add).pack(ipadx=20,ipady=10)


	GUI2.mainloop()



#########################################
menubar= Menu(GUI)
GUI.config(menu=menubar)

filemenu= Menu(menubar,tearoff=0)
filemenu.add_command(label='Exit',command=GUI.quit)
menubar.add_cascade(label='File',menu=filemenu)


mathmenu= Menu(menubar,tearoff=0)
mathmenu.add_command(label='การบวก',command=math_additional)
mathmenu.add_command(label='การลบ')
mathmenu.add_command(label='การคูณ')
mathmenu.add_command(label='การหาร')

menubar.add_cascade(label='คณิตศาสตร์',menu=mathmenu)
############################################333

FONT1 = ('TH SarabunPSK',16)

#สร้างแท็บ
Tap=ttk.Notebook(GUI)

T1 = Frame(Tap)
T2 = Frame(Tap)
T3 = Frame(Tap)

Tap.pack(fill = BOTH, expand=1)

Tap.add(T1,text='BEAM')
Tap.add(T2,text='Speed')
Tap.add(T3,text='Electricitty')

################### T1 #########################
#แปะรูป
img_beam = PhotoImage(file='beam.png')

logo=ttk.Label(T1,text='Beam',image=img_beam)
logo.pack()

#สร้างเฟรม
F1 = Frame(T1)
F1.pack()

#เก็บค่า
result = StringVar()
result2 = StringVar()
result3 = StringVar()

#ข้อความ+ช่องกรอก
P = Label(F1,text='กรุณากรอกความยาวหมายเลข 1',font=FONT1)
P.grid(row=0,column=0)
E1=ttk.Entry(F1,textvariable=result)
E1.grid(row=0,column=1,pady=10,padx=5)

P = Label(F1,text='กรุณากรอกความยาวหมายเลข 2',font=FONT1)
P.grid(row=1,column=0)
E2=ttk.Entry(F1,textvariable=result2)
E2.grid(row=1,column=1,pady=10,padx=5)

P = Label(F1,text='กรุณากรอกความยาวหมายเลข 3',font=FONT1)
P.grid(row=2,column=0)
E3=ttk.Entry(F1,textvariable=result3)
E3.grid(row=2,column=1,pady=10,padx=5)

#ฟังชั่นคำนวณ
def calc():
    a=float(result.get())
    b=float(result2.get())
    c=float(result3.get())
    calc= a*(b*c)
    textshow = 'ปริมาตรคอนกรีต = {:,.2f} ลบ.ม. '.format(calc)
    v_result.set(textshow)

#ปุ่ม
B1 = ttk.Button(T1,text='calculate',command=calc)
B1.pack(pady=20,ipadx=20,ipady=10)


v_result = StringVar()
v_result.set('------------- Result -------------')

Result = ttk.Label(T1,textvariable=v_result,foreground='red',font=FONT1)
Result.pack()
################################# T1 #####################################

############################T2##################################
O1 = Label(T2,text='คำนวณหาาอัตราเร็วปลาย(v) (m/s)',font=FONT1)
O1.pack(pady=10)

#แปะรูป2
image_object = PhotoImage(file='object.png')

logo2=ttk.Label(T2,text='object',image=image_object)
logo2.pack()

#สร้างเฟรม2
F2 = Frame(T2)
F2.pack()

#เก็บค่า2
res = StringVar()
res2 = StringVar()
res3 = StringVar()
cala = StringVar()

#ข้อความ+ช่องกรอก2
P1 = Label(F2,text='กรุณากรอกอัตราเร็วต้น(u) (m/s)',font=FONT1)
P1.grid(row=0,column=0)
E1=Entry(F2,textvariable=res)
E1.grid(row=0,column=1,pady=10,padx=5)

P2 = Label(F2,text='กรุณากรอกความเร่ง(a) (m/s^2)',font=FONT1)
P2.grid(row=1,column=0)
E2=Entry(F2,textvariable=res2)
E2.grid(row=1,column=1,pady=10,padx=5)

P3 = Label(F2,text='กรุณากรอกเวลาในการเคลื่อนที่(t) (s)',font=FONT1)
P3.grid(row=2,column=0)
E3=Entry(F2,textvariable=res3)
E3.grid(row=2,column=1,pady=10,padx=5)

#ฟังชั่นคำนวณ2
def speed():
    u=float(res.get())
    a=float(res2.get())
    t=float(res3.get())
    speed = u+(a*t)
    sh=f'อัตราเร็วปลาย(v) = {speed:,.2f} m/s'
    re.set(sh)

#ปุ่ม2
B1 = ttk.Button(T2,text='คำนวณ',command=speed)
B1.pack(pady=10,ipadx=20,ipady=10)

#แสดงคำตอบ2
re = StringVar()
re.set('-------อัตราเร็วปลาย(v)--------')

Re=ttk.Label(T2,textvariable=re,foreground='brown',font=FONT1)
Re.pack()
############################T2##################################




GUI.mainloop()

 


