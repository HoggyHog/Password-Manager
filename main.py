from tkinter import *
import input
import show
import mysql.connector as m
from tkinter import messagebox

con = m.connect(host="localhost", user="root", passwd="tiger1234", database="python")
cur1 = con.cursor()
cur2 = con.cursor()

def yes():

    b2["state"]="disabled"

    def display():
        j = 1
        name = e3.get()
        cur1.execute("show tables")
        r1=cur1.fetchall()

        for i in r1:
            if name in i:
                j=0

        if j==0:
            pas=e4.get()
            cur2.execute("select PASSW from {}".format(name))        #string formatting
            r2=cur2.fetchall()

            for i in r2:
                k=i[0]
            if k==pas:
                show.take(name)
                mainn.destroy()
            else:
                messagebox.showerror("ERROR","WRONG PASSWORD")
        else:
            messagebox.showerror("ERROR","USERNAME DOESNT EXIST")

    l7 = Label(mainn, text="", bg='#5CDB95')
    l7.grid(row=4, column=0)

    l8 = Label(mainn, text="",bg='#5CDB95')
    l8.grid(row=5, column=0)

    l6=Label(mainn, text=" ENTER YOUR MASTER USERNAME ",bg='#5CDB95',fg="#05386b")
    l6.grid(row=6,column=0)

    e3 = Entry(mainn)
    e3.grid(row=7, column=0)

    l9 = Label(mainn, text="", bg='#5CDB95')
    l9.grid(row=8, column=0)

    l10 = Label(mainn, text=" ENTER YOUR MASTER PASSWORD ",bg='#5CDB95',fg="#05386b")
    l10.grid(row=9, column=0)

    e4 = Entry(mainn,show="*")
    e4.grid(row=10, column=0)

    l11 = Label(mainn, text="", bg='#5CDB95')
    l11.grid(row=11, column=0)

    b4=Button(mainn, text="SUBMIT",command=display,bg='#5CDB95',fg="#05386b")
    b4.grid(row=12,column=0)

def no():
    b1["state"] = "disabled"

    def accept():
        j=1
        name=e1.get()
        pas=e2.get()
        cpas=e3.get()
        if cpas==pas:
            j=0
        if j==0:
            input.input(name,pas)
        if j==0:
            mainn.destroy()
        else:
            messagebox.showerror("ERROR","PASSWORDS DON'T MATCH ")

    l3 = Label(mainn, text="\n",bg='#5CDB95')
    l3.grid(row=5, column=2)
    l4 = Label(mainn, text="PLEASE ENTER YOUR NEW MASTER USERNAME ",bg='#5CDB95',fg="#05386b")
    l4.grid(row=6, column=2)

    e1 = Entry(mainn)
    e1.grid(row=7, column=2)

    l6 = Label(mainn, text="",bg='#5CDB95')
    l6.grid(row=8, column=2)

    l5 = Label(mainn, text="PLEASE ENTER YOUR NEW MASTER PASSWORD ",bg='#5CDB95',fg="#05386b")
    l5.grid(row=9, column=2)

    e2 = Entry(mainn,show="*")
    e2.grid(row=10, column=2)

    l7 = Label(mainn, text="",bg='#5CDB95')
    l7.grid(row=11, column=2)

    l5 = Label(mainn, text="RECONFIRM YOUR PASSWORD",bg='#5CDB95',fg="#05386b")
    l5.grid(row=12, column=2)

    e3 = Entry(mainn,show="*")
    e3.grid(row=13, column=2)

    l8 = Label(mainn, text="",bg='#5CDB95')
    l8.grid(row=14, column=2)

    b3 = Button(mainn, text="SUBMIT", command=accept,bg='#5CDB95')
    b3.grid(row=15, column=2)


mainn = Tk()                                                           # tkinter object
mainn.configure(bg='#5CDB95')
l1=Label(mainn,text="HEY THERE",fg="#05386b",bg='#5CDB95',font="bold 17")
l2=Label(mainn,text="KEEP YOUR PASSWORDS SAFE WITH PASSWORD MANAGER",bg='#5CDB95',fg="#05386b",font="bold 17")
l3=Label(mainn,text="",bg="#5CDB95")
l9=Label(mainn,text="",bg="#5CDB95")


l1.grid(row=0,column=1)                         # making a table on the window
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l9.grid(row=1,column=1)


b1=Button(mainn,text="ARE YOU A REGISTERED USER", padx=50,fg="blue",command=yes)  # only name of the function
b2=Button(mainn,text="IF NOT, THEN CLICK HERE",padx = 50, fg="red",command=no)

b1.grid(row=4,column=0)
b2.grid(row=4,column=2)

mainn.mainloop()   # program execution gets over in split seconds
