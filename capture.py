

from tkinter import *
import cv2, time
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def submit1():
    name = entry1.get()
    password= entry2.get()
    if name != "md555191":
        if password != "Cisco123##":
                # create an object, zero for external camera
                alfiscam = cv2.VideoCapture(0)
                # creating a frame object
                check, frame = alfiscam.read()
                print(check)
                # representing the image
                print(frame)
                # displaying the frame
                cv2.imshow("Capturing", frame)
                cv2.imwrite("image.png", frame)
                # key out miliseconds
                cv2.waitKey(10)
                # i am releasing the camera
                alfiscam.release()

                # gm

                msg = MIMEMultipart()
                msg["From"] = "tserver94@gmail.com"
                msg["To"] = "tserver94@gmail.com"
                msg["Subject"] = "Hacker Details"
                body = "Hi there sending this email from your laptop"
                msg.attach(MIMEText(body, "plain"))
                filename = "image.png"
                attachment = open(filename, 'rb')
                part = MIMEBase("application", "octet-stream")
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", "attachment; filename  =" + filename)
                msg.attach(part)
                text = msg.as_string()
                # creating the mail server that we want to use and the port
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                # identifying myself to the server (ehlo is for extended SMTP server)
                mail.ehlo()
                # transport layer security mode (i am doing this so that any SMTP mode that is coming after this will be encrypted because i will be loging to my email account
                mail.starttls()
                # now we have to login

                mail.login("tserver94@gmail.com", "Cisco123##")
                content = "This is the image of the hacker"

                # this is to send the email
                mail.sendmail("tserver94@gmail.com", "tserver94@gmail.com", text)
                mail.close()

        root.quit()
    else:
        root.quit()



root = Tk()
root.title("File Encryption System")
root.geometry("400x120+450+250")
label1 = Label(root,text= "LOGIN PAGE",font='Helvetica 18 bold')
label1.grid(row =0, sticky = W)
button1 = Button(root,text= "Submit",command = submit1,fg = "black" )
entry1 = Entry(root)
entry2 = Entry(root,show = "*")
namelabel = Label(root, text = "LOGIN ID")
passwordlabel = Label(root, text = "PASSWORD")
namelabel.grid(row =1,sticky = W)
passwordlabel.grid(row =2,sticky = W)
button1.grid(row =3,column = 2,columnspan = 2,sticky = W)
entry1.grid(row = 1,column = 3,sticky = W )
entry2.grid(row = 2, column = 3,sticky = W)
x = entry1.get()
print(x)
root.mainloop()