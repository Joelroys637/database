import streamlit as st
import sqlite3
from PIL import Image
import io

def main():
    original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;"> </h1>'
    st.markdown(original_title, unsafe_allow_html=True)


# Set the background image
    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img.freepik.com/premium-photo/blue-modern-abstract-futuristic-technology-background-24_769134-546.jpg");
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
    conn = sqlite3.connect('dataentryform.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS dataform (Name TEXT, Age TEXT,Gender TEXT,community TEXT,cast TEXT,religion TEXT,date_of_birth TEXT,blood_group TEXT,Aadhaar_no TEXT,state TEXT,address TEXT)''')
    conn.commit()

    def create_dataform_table():
        name,age,Gen=st.columns(3,gap="small")
        comm,cas,rel,date=st.columns(4,gap="small")
        blood,aadh,sta,addre=st.columns(4,gap="small")
        
        
    
        conn = sqlite3.connect('dataentryform.db')
        c = conn.cursor()

        name1=name.text_input('Name of the Applicant')
        age1=age.text_input('Age')
        gender=Gen.text_input('Gender')
        community=comm.text_input('Community')
        cast=cas.text_input('Cast')
        religion=rel.text_input('Religion')
        date_of_birth=date.date_input('Date Of Birth')
        blood_group=blood.text_input('Blood Group')
        aadhaar=aadh.text_input('Aadhaar')
        state=sta.text_input('State')
        address=addre.text_input('Address')
        

        # Image upload widget
        image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

        # Your existing code for text inputs...

        if st.button('Submit'):
            if image is not None:
                # Convert image to bytes
                img_bytes = image.read()

                # Insert data into SQLite database
                c.execute("INSERT INTO dataform (Name, Age, Gender, Community, Cast, Religion, Date_Of_Birth, Blood_Group, Aadhaar_no, State, Address, Image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name1, age1, gender, community, cast, religion, date_of_birth, blood_group, aadhaar, state, address, img_bytes))
            else:
                # Insert data without image
                c.execute("INSERT INTO dataform (Name, Age, Gender, Community, Cast, Religion, Date_Of_Birth, Blood_Group, Aadhaar_no, State, Address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name1, age1, gender, community, cast, religion, date_of_birth, blood_group, aadhaar, state, address))

            conn.commit()
            st.success("Thank you")

    create_dataform_table()
