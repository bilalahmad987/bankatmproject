import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import*
import random
import sqlite3
from tkinter import messagebox






win=tk.Tk()
win.title("habib bank limited")
tabControl = ttk.Notebook(win)
icon = PhotoImage(file="bb.png")
win.tk.call("wm",'iconphoto',win._w,icon)
#-----------------------------database--------------------------------#
def add_btn1():
	import sqlite3
	db = sqlite3.connect("atm_databse.db")
	db1 = sqlite3.connect("admin.db")

	mycursor=db.cursor()
	mycursor1=db1.cursor()
	#mycursor.execute("CREATE TABLE name(acc_no smallint(10),name VARCHAR(100),branch VARCHAR(100), pass smallint UNSIGNED,cnic smallint UNSIGNED,contactno smallint UNSIGNED,ACC VARCHAR(100),REFERENCE VARCHAR(100))")
	mycursor.execute("INSERT INTO  atm(name, acc_no, branch, acc_type,cnic,bal,pass,contactno) VALUES (?,?,?,?,?,?,?,?)",(text_input3.get(),text_input2.get(), text_input4.get(),text_input8.get(),text_input6.get(),text_input9.get(),text_input5.get(),text_input7.get()))
	mycursor1.execute("INSERT INTO atm(name,acc_no,acc_type,bal,pass)VALUES (?,?,?,?,?)",(text_input3.get(),text_input2.get(),text_input8.get(),text_input9.get(),text_input5.get())) 

	db.commit()
	db1.commit()

	
	db.close()

#--------------------------tabs----------------------------------#
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text='MAIN AREA')

tab2=ttk.Frame(tabControl)

tabControl.add(tab2,text='OPEN ACCOUNT')
tab3=ttk.Frame(tabControl)

tabControl.add(tab3,text='ATM')




tabControl.pack(expand=1,fill="both")



#-----------------------functions------------------------------------------#
def info():
	from tkinter import messagebox as mBox
	from tkinter import Tk
	root = Tk()
	root.withdraw()
	mBox.showinfo('', 'A Python GUI created using tkinter:\nThe year is2015\nThe year is2015\nThe year is2015\nThe year is2015\nThe year is2015\nThe year is2015\nThe year is2015')
#---------------------tab1 button-------------------------------------------#
addbtn=ttk.Button(tab1,text="ABOUT US",width=50,command=info).grid(row=0,column=0,padx=10,pady=10)
addbtn=ttk.Button(tab1,text="QUERY",width=50).grid(row=1,column=0,padx=10,pady=10)
addbtn=ttk.Button(tab1,text="DEPOSIT MONEY",width=50).grid(row=2,column=0,padx=10,pady=10)
addbtn=ttk.Button(tab1,text="WITHDRAW MONEY",width=50).grid(row=3,column=0,padx=10,pady=10)
addbtn=ttk.Button(tab1,text="OPEN ACCOUNT",width=50).grid(row=4,column=0,padx=10,pady=10)
#---------------------TAB2 DATA--------------------------------------------#
bill_no=StringVar()
def acc_no():
	global operator
	operator=""
	text_input2.set("")
	x=random.randint(100000,9999999)
	bill_no.set(str(x))
	
	
	text_roll.insert(50,str(x))

text_input2 = tk.StringVar()
operator =""
text_input3 = tk.StringVar()
operator =""
text_input4 = tk.StringVar()
operator =""
text_input5 = tk.StringVar()
operator =""
text_input6 = tk.StringVar()
operator =""
text_input7 = tk.StringVar()
operator =""
text_input8 = tk.StringVar()
operator =""
text_input9 = tk.StringVar()
operator =""

b1=ttk.Label(tab2,text="ACCNT NO",font=("time new roman",8,"bold","italic"))
b1.grid(row=0,column=0,columnspan=2,pady=3)
text_roll=tk.Entry(tab2,textvariable=text_input2,highlightcolor="#50A8B0",highlightthickness=3,highlightbackground="white",font=("time new roman",15,"bold","italic"))
text_roll.grid(row=0,column=2,pady=10,padx=20)
b11=ttk.Label(tab2,text="NAME",font=("time new roman",8,"bold","italic"))
b11.grid(row=1,column=0,columnspan=2,pady=3)
text_roll1=tk.Entry(tab2,textvariable=text_input3,highlightcolor="#50A8B0",highlightthickness=3,highlightbackground="white",font=("time new roman",15,"bold","italic"))
text_roll1.grid(row=1,column=2,pady=10,padx=20)
b1=ttk.Label(tab2,text="BRANCH",font=("time new roman",8,"bold","italic"))
b1.grid(row=2,column=0,columnspan=2,pady=3)
text_roll21=tk.Entry(tab2,textvariable=text_input4,highlightcolor="#50A8B0",highlightthickness=3,highlightbackground="white",font=("time new roman",15,"bold","italic"))
text_roll21.grid(row=2,column=2,pady=10,padx=20)

b1=ttk.Label(tab2,text="PASSWORD",font=("time new roman",8,"bold","italic"))
b1.grid(row=3,column=0,columnspan=2,pady=3)
text_roll19=tk.Entry(tab2,textvariable=text_input5,highlightcolor="#50A8B0",highlightthickness=3,highlightbackground="white",font=("time new roman",15,"bold","italic"),show="*")
text_roll19.grid(row=3,column=2,pady=10,padx=20)
b18=ttk.Label(tab2,text="CNIC",font=("time new roman",8,"bold","italic"))
b18.grid(row=4,column=0,columnspan=2,pady=3)
text_roll16=tk.Entry(tab2,textvariable=text_input6,highlightcolor="#50A8B0",highlightthickness=3,highlightbackground="white",font=("time new roman",15,"bold","italic"))
text_roll16.grid(row=4,column=2,pady=10,padx=20)
b16=ttk.Label(tab2,text="CONT NO",font=("time new roman",8,"bold","italic"))
b16.grid(row=5,column=0,columnspan=2,pady=3)
text_roll13=tk.Entry(tab2,textvariable=text_input7,highlightcolor="#50A8B0",highlightthickness=3,highlightbackground="white",font=("time new roman",15,"bold","italic"))
text_roll13.grid(row=5,column=2,pady=10,padx=20)
b13=ttk.Label(tab2,text="ACC TYPE",font=("time new roman",8,"bold","italic"))
b13.grid(row=6,column=0,columnspan=2,pady=3)
text_roll12=tk.Entry(tab2,textvariable=text_input8,highlightcolor="#50A8B0",highlightthickness=3,highlightbackground="white",font=("time new roman",15,"bold","italic"))
text_roll12.grid(row=6,column=2,pady=10,padx=20)
b11=ttk.Label(tab2,text="AMOUNTDEPOSIT",font=("time new roman",8,"bold","italic"))
b11.grid(row=7,column=0,columnspan=2,pady=3)
text_roll11=tk.Entry(tab2,textvariable=text_input9,highlightcolor="#50A8B0",highlightthickness=3,highlightbackground="white",font=("time new roman",15,"bold","italic"))
text_roll11.grid(row=7,column=2,pady=10,padx=20)
addbtn=ttk.Button(tab2,text="GENERATE ACC NO",width=25,command=acc_no).grid(row=8,column=2,pady=10,padx=20)
#processButton=ttk.Button(tab2,text="OPEN ACCOUNT",width=25).grid(row=9,column=2,pady=10,padx=20)

#--------------------------------------------tab2 btn---------------------------------#


processButton=ttk.Button(tab2,text="OPEN ACCOUNT",width=25,command=add_btn1)
processButton.grid(row=9,column=2,pady=10,padx=20)

#Balloons (Tooltips)

#-----------------------------tab3  deposit money--------------------------------------------------------#
ARIAL = ("arial",10,"bold")

class Bank:
    def __init__(self,root):
        self.conn = sqlite3.connect("admin.db", timeout=100)
        self.login = False
        self.root = root
        self.header = Label(tab3,text="HBL BANK LIMITED",bg="#50A8B0",fg="white",font=("arial",20,"bold"))
        self.header.pack(fill=X)
        self.frame = Frame(tab3,bg="#728B8E",width=600,height=400)
        #Login Page Form Components
        self.userlabel =Label(self.frame,text="Account Number",bg="#728B8E",fg="white",font=ARIAL)
        self.uentry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",
           highlightthickness=2,
            highlightbackground="white")
        self.plabel = Label(self.frame, text="Password",bg="#728B8E",fg="white",font=ARIAL)
        self.pentry = Entry(self.frame,bg="honeydew",show="*",highlightcolor="#50A8B0",
           highlightthickness=2,
            highlightbackground="white")
        self.button22 = Button(self.frame,text="LOGIN",bg="#50A8B0",fg="white",font=ARIAL,command=self.verify)
        self.q = Button(self.frame,text="Quit",bg="#50A8B0",fg="white",font=ARIAL,command = self.root.destroy)
        self.userlabel.place(x=145,y=100,width=120,height=20)
        self.uentry.place(x=153,y=130,width=200,height=20)
        self.plabel.place(x=125,y=160,width=120,height=20)
        self.pentry.place(x=153,y=190,width=200,height=20)
        self.button22.place(x=155,y=230,width=120,height=20)
        self.q.place(x=480,y=360,width=120,height=20)
        



        self.frame.pack()
    def database_fetch(self):#Fetching Account data from database
        self.acc_list = []
        self.temp = self.conn.execute("select name,pass,acc_no,acc_type,bal from atm where acc_no = ? ",(self.ac,))
        for i in self.temp:
            self.acc_list.append("Name = {}".format(i[0]))
            self.acc_list.append("Account no = {}".format(i[2]))
            self.acc_list.append("Account type = {}".format(i[3]))
            self.ac = i[2]
            self.acc_list.append("Balance = {}".format(i[4]))

    def verify(self):#verifying of authorised user
        ac = False
        self.temp = self.conn.execute("select name,pass,acc_no,acc_type,bal from atm where acc_no = ? ", (int(self.uentry.get()),))
        for i in self.temp:
            self.ac = i[2]
            if i[2] == self.uentry.get():
                ac = True
            elif i[1] == self.pentry.get():
                ac = True
                m = "{} Login SucessFull".format(i[0])
                self.database_fetch()
                messagebox._show("Login Info", m)
                self.frame.destroy()
                self.MainMenu()
            else:
                ac = True
                m = " Login UnSucessFull ! Wrong Password"
                messagebox._show("Login Info!", m)

        if not ac:
            m = " Wrong Acoount Number !"
            messagebox._show("Login Info!", m)


    def MainMenu(self):#Main App Appears after logined !
        self.frame = Frame(tab3,bg="#728B8E",width=800,height=400)
        
        self.detail = Button(self.frame,text="Account Details",bg="#50A8B0",fg="white",font=ARIAL,command=self.account_detail)
        self.enquiry = Button(self.frame, text="Balance Enquiry",bg="#50A8B0",fg="white",font=ARIAL,command= self.Balance)
        self.deposit = Button(self.frame, text="Deposit Money",bg="#50A8B0",fg="white",font=ARIAL,command=self.deposit_money)
        self.withdrawl = Button(self.frame, text="Withdrawl Money",bg="#50A8B0",fg="white",font=ARIAL,command=self.withdrawl_money)
        self.q = Button(self.frame, text="Quit", bg="#50A8B0", fg="white", font=ARIAL, command=self.root.destroy)
        self.detail.place(x=0,y=0,width=200,height=50)
        self.enquiry.place(x=0, y=315, width=200, height=50)
        self.deposit.place(x=600, y=0, width=200, height=50)
        self.withdrawl.place(x=600, y=315, width=200, height=50)
        self.q.place(x=340, y=340, width=120, height=20)
        self.frame.pack()

    def account_detail(self):
        self.database_fetch()
        text = self.acc_list[0]+"\n"+self.acc_list[1]+"\n"+self.acc_list[2]
        self.label = Label(self.frame,text=text,font=ARIAL)
        self.label.place(x=200,y=100,width=300,height=100)

    def Balance(self):
        self.database_fetch()
        self.label = Label(self.frame, text=self.acc_list[3],font=ARIAL)
        self.label.place(x=200, y=100, width=300, height=100)

    def deposit_money(self):
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",
           highlightthickness=2,
            highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#50A8B0",fg="white",font=ARIAL)

        self.money_box.place(x=200,y=100,width=200,height=20)
        self.submitButton.place(x=445,y=100,width=55,height=20)
        self.submitButton.bind("<Button-1>",self.deposit_trans)

    def deposit_trans(self,flag):
        self.label = Label(self.frame, text="Transaction Completed !", font=ARIAL)
        self.label.place(x=200, y=100, width=300, height=100)
        self.conn.execute("update atm set bal = bal + ? where acc_no = ?",(self.money_box.get(),self.ac))
        self.conn.commit()

    def withdrawl_money(self):
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",
           highlightthickness=2,
            highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#50A8B0",fg="white",font=ARIAL)

        self.money_box.place(x=200,y=100,width=200,height=20)
        self.submitButton.place(x=445,y=100,width=55,height=20)
        self.submitButton.bind("<Button-1>",self.withdrawl_trans)

    def withdrawl_trans(self,flag):
        self.label = Label(self.frame, text="Money Withdrawl !", font=ARIAL)
        self.label.place(x=200, y=100, width=300, height=100)
        self.conn.execute("update atm set bal = bal - ? where acc_no = ?",(self.money_box.get(),self.ac))
        self.conn.commit()



obj = Bank(win)

win.mainloop()
