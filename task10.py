from tkinter import *
from tkinter import filedialog
root = Tk()
root.geometry("250x100")
def dialog():
    root.fileName = filedialog.askopenfilename(filetypes=(("txt files", "*.txt"), ("all files","*.*")))
    print(root.fileName)
    label = Label(root, text=root.fileName)
    label.grid(row = 0,column = 0 ,columnspan = 6)
    f = open(root.fileName,'r')
    x = f.read()
    print(x)

def ecryptbutton():
    pass
def decryptbutton():
    pass

ecrypt = Button(root,text = "Encrypt",command = ecryptbutton,fg= "black").grid(row = 5, column = 2,columnspan = 2,sticky = W)
display = Label(root,text = "").grid(row=1,column = 1,columnspan = 3,sticky = W)
search = Button(root,text= "Submit",command = dialog,fg = "black" ).grid(row =3,column =4,columnspan = 3,sticky = W)
root.mainloop()