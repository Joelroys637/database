import streamlit as st
import smtplib


def gmail(id):
    
# Taking inputs
    email_sender ='pythonleo637@gmail.com'
    email_receiver = 'joelroys637@gamil.com'
    subject = "hi"
    body = "hi i am python"

        
    text=f"subject:{subject}\n\n{body}"

    server=smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(email_sender,"dttp oczk lhik geoy")

    server.sendmail(email_sender,email_receiver,text)

    st.write("email send"+email_receiver)
