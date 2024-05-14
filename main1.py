import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3
import dataentry as data
import base64
import admin as adm

original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;"> </h1>'
st.markdown(original_title, unsafe_allow_html=True)


# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img.freepik.com/free-vector/geometric-gradient-futuristic-background_23-2149116406.jpg?size=626&ext=jpg&ga=GA1.1.1224184972.1715472000&semt=ais_user");
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
#data open function
def open_path():
    
    data.main()
    

#option code

    
selected = option_menu(
    menu_title="",
    options=["sigup","login","Admin"],
    icons=["house","upload","upload"],
    orientation="horizontal",
)
    
if selected =="sigup":
    
    def create_user_table():
        user=st.text_input('username')
        password1=st.text_input('password')
        phone=st.text_input('Mobile number OR Email id')
        if st.button("SIGUP"):
            
            c.execute("INSERT INTO users VALUES (?, ?, ?)", (user,password1,phone))
            st.success("Sigup Successfully Thank you!")
        
            
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
    username = text_input.text_input('Username')
    password = text_input_container.text_input('Password', type='password')
    ck1=st.checkbox("login",)
    if ck1==True:
    
        if login(username, password):
           if username != " ":
               text_input.empty()
               if password !=" ":
                   text_input_container.empty()
           open_path()
        else:
            st.error('Incorrect username or password')
    
elif selected =="Admin":
    name=st.text_input("Enter you name")
    if st.button("LOGIN ADMIN PAGE"):
        if name=="leojoelroys":
            
            adm.back()
            adm.main()
        else:
            
            st.error('Not acccess this page because only admin can access this page')
    
