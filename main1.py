import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3
import dataentry as data
import base64
import admin as adm
import header_menu_remove as hedremove
import smtplib
import home 


#remove the header bar in streamlit
hedremove.headerhide()



    
original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;"> </h1>'
st.markdown(original_title, unsafe_allow_html=True)



# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


input_style = """
<style>
input[type="text"] {
    background-color: transparent;
    color: #a19eae;  // This changes the text color inside the input box
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)
# Create a connection to the SQLite database
conn = sqlite3.connect('login.db')
c = conn.cursor()

# Create a table for storing user credentials if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT,phone TEXT)''')
conn.commit()
#data open function in dataentryform
def open_path():
    
    data.main()
    
#option code
    
selected = option_menu(
    menu_title="",
    options=["HOME","sigup","login","Admin"],
    icons=["house","upload","upload"],
    orientation="horizontal",
)
if selected=="HOME":
    home.main()
    
elif selected =="sigup":
    
    def create_user_table():
        user=st.text_input('username')
        password1=st.text_input('password')
        phone=st.text_input('Mobile number OR Email id')
        #sending gmail messge
        email_sender = "pythonleo637@gmail.com"
        email_receiver = phone
        subject = "Congratulations To SIGUP Dalmia School website "
        body = f'''hi {user} you have successfully sigup in school webpage
                   Thank you for comming to visite dalmia school
                         YOU'S Detail:
                                 ID:{user}
                                 PASSWORD:{password1}'''

        try:
            
            text=f"subject:{subject}\n\n{body}"

            server=smtplib.SMTP("smtp.gmail.com",587)
 
            server.starttls()

            server.login(email_sender,"dttp oczk lhik geoy")

            server.sendmail(email_sender,email_receiver,text)

            st.write("pleas check mail"+email_receiver)
        except:
            st.write("NOTICE** Kindly Enter a Email Id")
        
        if not user:
            
            st.stop()
        if st.button("SIGUP"):
            
            c.execute("INSERT INTO users VALUES (?, ?, ?)", (user,password1,phone))
            st.success("Sigup Successfully Thank you!")
        
            st.balloons()
            conn.commit()
        
    
    create_user_table()
    
        
elif selected =="login":
    def login(username, password):
        
        # Query the database to check if the username and password combination exists
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        
        if c.fetchone():
            return True
        else:
            return False
    
    text_input = st.empty()
    text_input_container = st.empty()
    check=st.empty()
    username = text_input.text_input('Username')
    password = text_input_container.text_input('Password', type='password')
    ck1=check.checkbox("login",)
    if ck1==True:
    
        if login(username, password):
           if username != " ":
               text_input.empty()
               if password !=" ":
                   text_input_container.empty()
                   if check!=" ":
                       check.empty()
           open_path()
        else:
            st.error('Incorrect username or password')
    
elif selected =="Admin":
    name=st.text_input("Enter admin name ")
    if st.button("LOGIN ADMIN PAGE"):
        if name=="leojoelroys":
            
            adm.back()
            adm.main()
        else:
            
            st.error('Not acccess this page because only admin can access this page')
    
