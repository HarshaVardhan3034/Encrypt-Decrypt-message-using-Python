from tkinter import *
import pybase64
from tkinter import messagebox

window = Tk()
window.title("Encrypt And Decrypt")
window.config(background="aquamarine1")
window.geometry("500x500")

def clear():
    #clear
    my_text.delete(1.0, END)
    pass_entry.delete(0,END)
def encrypt():
    #get the text entered from the text box
    secret = my_text.get(1.0,END)

    my_text.delete(1.0,END)

    #logic
    if pass_entry.get() == "edbase64":
        #convert to byte
        secret=secret.encode("ascii")

        #convert to base64
        secret = pybase64.urlsafe_b64encode(secret)

        # convert back to ascii
        secret = secret.decode("ascii")

        #print to text bpx
        my_text.insert(END,secret)
    else:
        #messagebox
        messagebox.showwarning("Incorrect!!", "Incorrect Password, Try Again!..")



def decrypt():
    secret = my_text.get(1.0,END)

    my_text.delete(1.0,END)

    #logic
    if pass_entry.get() == "edbase64":
        #convert to byte
        secret=secret.encode("ascii")

        #convert to base64
        secret = pybase64.urlsafe_b64decode(secret)

        # convert back to ascii
        secret = secret.decode("ascii")

        #print to text bpx
        my_text.insert(END,secret)
    else:
        #messagebox
        messagebox.showwarning("Incorrect!!", "Incorrect Password, Try Again!..")

frame = Frame(window)
frame.pack(pady=20)

en_button = Button(frame,text="Encrypt",font=("Helvetica",18),command=encrypt)
en_button.grid(row=0,column=0)

de_button = Button(frame,text="Decrypt",font=("Helvetica",18),command=decrypt)
de_button.grid(row=0,column=1)

clear_button = Button(frame,text="Clear",font=("Helvetica",18),command=clear)
clear_button.grid(row=0,column=3)

enc_label = Label(window,text="Encrypt/Decrypt Text....",font=("Helvetica",18),bg="aquamarine1")
enc_label.pack()

my_text = Text(window,height=10,width=50,font=("Helvetica",16))
my_text.pack(pady=10)

password_label = Label(window,text="Enter your password....",font=("Helvetica",18),bg="aquamarine1")
password_label.pack()

pass_entry = Entry(window,font=("Helvetica",18),width=35,show='*')
pass_entry.pack(pady=10)
window.mainloop()