from tkinter import *
import mysql.connector as m
from tkinter import messagebox

con = m.connect(host="localhost", user="root", passwd="tiger1234", database="python")
cur1 = con.cursor()
cur2=con.cursor()

i=0

def input(a,p):
    j = 1

    cur1.execute("show tables")
    r=cur1.fetchall()
    for m in r:
        if a in m:
            j=0
    if j==0:
        messagebox.showinfo("ERROR","USERNAME ALREADY EXISTS")

    else:
        cur2.execute("CREATE table {} (website varchar(30), username varchar(30), password varchar(30), PASSW varchar(30))".format(a))


        def accept():
            global i
            i+=1
            l4 = Label(inp, text="",font=" bold 20",fg="blue")
            l4.config(text="SUCCESSFULLY INPUT {} RECORD".format(i))
            l4.place(x=200, y=450)

            web=e1.get()
            us=e2.get()
            ps=e3.get()
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            cur2.execute("insert into {} values ('".format(a)+web+"', '"+us+"', '"+ps+"', '"+p+"')")
            con.commit()
    # cur.execute("insert into values ('"+web+"', '"+us+"', '"+ps+"')".format(a))
        inp=Tk()
        inp.configure(bg='#5CDB95')
        inp.title("window 2")
        inp.geometry("720x600")    # giving the window a size

        l1=Label(inp,text="Welcome {}".format(a),font=" bold 30 ",fg="#05386b",bg='#5CDB95')
        l1.place(x=240,y=30)
        l2=Label(inp,text="Enter your credentials ",font="bold 20",fg="#05386b",bg='#5CDB95')
        l2.place(x=10,y=120)

        l3 = Label(inp, text="WEBSITE/APP",font="bold 15",fg="RED",bg='#5CDB95')
        l3.place(x=10,y=180)
        w1l4 = Label(inp, text="USERNAME",font="bold 15",fg="RED",bg='#5CDB95')
        w1l4.place(x=10, y=240)
        w1l5 = Label(inp, text="PASSWORD",font="bold 15",fg="RED",bg='#5CDB95')
        w1l5.place(x=10, y=300)

        e1=Entry(inp,width=30,bd=3)
        e1.place(x=360,y=180)
        e2 = Entry(inp, width=30,bd=3)
        e2.place(x=360, y=240)
        e3 = Entry(inp, width=30,bd=3)
        e3.place(x=360, y=300)

        b1=Button(inp,text="SUBMIT",command=accept,fg="blue")
        b1.place(x=100,y=390)

        b2=Button(inp,text="DONE",command=quit,fg="red")
        b2.place(x=600, y=390)

        inp.mainloop()
