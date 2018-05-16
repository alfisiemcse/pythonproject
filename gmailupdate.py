import cv2, time
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


#create an object, zero for external camera
alfiscam = cv2.VideoCapture(0)
#creating a frame object
check,frame = alfiscam.read()
print(check)
#representing the image
print(frame)
#displaying the frame
cv2.imshow("Capturing",frame)
cv2.imwrite("image.png", frame)
#key out miliseconds
cv2.waitKey(10)
#i am releasing the camera
alfiscam.release()




# gm


msg = MIMEMultipart()
msg["From"] = "thalagari@gmail.com"
msg["To"] = "alfis.iemcse@gmail.com"
msg["Subject"] = "Hacker Details"
body = "Hi there sending this email from your laptop"
msg.attach(MIMEText(body,"plain"))
filename = "image.png"
attachment = open(filename,'rb')
part = MIMEBase("application","octet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header("Content-Disposition","attachment; filename  ="+filename)
msg.attach(part)
text = msg.as_string()
#creating the mail server that we want to use and the port
mail = smtplib.SMTP('smtp.gmail.com',587)
#identifying myself to the server (ehlo is for extended SMTP server)
mail.ehlo()
#transport layer security mode (i am doing this so that any SMTP mode that is coming after this will be encrypted because i will be loging to my email account
mail.starttls()
#now we have to login


mail.login("thalagari@gmail.com","alfisrubana4321")
content = "This is the image of the hacker"




#this is to send the email
mail.sendmail("thalagari@gmail.com","alfis.iemcse@gmail.com",text)
mail.close()

