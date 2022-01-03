from tkinter import messagebox
from tkinter import *
import mysql.connector as m

con = m.connect(host="localhost", user="root", passwd="tiger1234", database="python")
cur1= con.cursor()
cur2= con.cursor()

def take(a):

    def give():

        z=1
        cur1.execute("select website from {}".format(a))
        r1=cur1.fetchall()
        web = e1.get()
        e1.delete(0,END)
        for m in r1:
            if web in m:
                z=0
        if z==0:
            web="'"+web+"'"
            cur2.execute("select username,password from {} where website like {}".format(a,web))
            r2 = cur2.fetchall()
            for i in r2:
                k=i[0]
                j=i[1]

            messagebox.showinfo("USERNAME AND PASSWORD","USERNAME ---> {}\nPASSWORD-----> {}".format(k,j))
        else:
            messagebox.showinfo("ERROR","THE DETAILS OF THIS WEBSITE ARE NOT ENTERED")



    root = Tk()
    root.configure(bg='#5CDB95')
    root.title("window 3")
    root.geometry("720x600")

    l1 = Label(root, text="Welcome {}".format(a), font=" bold 30 ", fg="#05386b",bg='#5CDB95')
    l1.place(x=240, y=30)
    l2 = Label(root, text="ENTER THE WEBSITE/APP NAME ", font="bold 20", fg="#05386b",bg='#5CDB95')
    l2.place(x=10, y=120)

    e1 = Entry(root, width=30, bd=3)
    e1.place(x=360, y=120)

    b1 = Button(root, text="SUBMIT", command=give, fg="blue")
    b1.place(x=100, y=180)

    b2 = Button(root, text="DONE", command=quit, fg="red")
    b2.place(x=600, y=180)

    root.mainloop()
