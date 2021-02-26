from tkinter import *
import random,string

def power():
    lbl.config(text="Your password: {}".format(assign_password()))


def assign_password():

    au2="".join(random.choice(string.ascii_uppercase) for x in range(2))
    digits2="".join(random.choice(string.digits) for x in range(2))
    punctuation2="".join(random.choice(string.punctuation) for x in range(2))
    letters=string.ascii_letters+string.digits+string.punctuation
    lst="".join(random.choice(letters) for x in range(4))
    lst2=au2+digits2+punctuation2
    xpsw=lst+lst2
    psw=list(xpsw)
    result="".join(psw)
    return result





window=Tk()

window.title("programmer")
window.geometry("500x300")

your_password=Frame(window)
your_password.grid()

lbl=Label(your_password,text="Your password:",font="Calibri 14 bold")
lbl.grid(padx=10,pady=10)

button=Button(your_password,text ="ASSIGN PASSWORD",font="Calibri 12 bold",width=50,height=5,command=power)
button.grid(padx=40,pady=80)

window.mainloop()