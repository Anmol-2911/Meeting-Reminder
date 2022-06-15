#!/usr/bin/env python3
import datetime
from email.message import EmailMessage
def sending_email(subject,body):
    message= EmailMessage()
    sender = str(input("Enter the sender's email address: "))
    recipient=["usernameabc2911@gmail.com","userabc2911@gmail.com"]
    message["From"]=sender
    message["To"]=recipient
    message["Subject"]=subject
    message.set_content(body)
    import smtplib
    mail_server=smtplib.SMTP_SSL("smtp.google.com")
    import getpass
    mail_pass=getpass.getpass("Enter your Password ")
    try:

        mail_server.login(sender,mail_pass)
        mail_server.send_message(message)
        mail_server.quit()
        a=datetime.datetime.now()
        print("Email sent to: {} at {}".format(recipient,a))
    except:
        print("Error: Mail not Sent")
