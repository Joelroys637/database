import streamlit as st
import sqlite3
import pandas as pd
from PIL import Image
import io
def back():
    original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;"> </h1>'
    st.markdown(original_title, unsafe_allow_html=True)


# Set the background image
    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
    background-image: url("http://localhost:8501/media/2298cc52c9b7f1b46af756061c29c1238d54626cc6d10dcf6355a357.jpg");
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


def view_data():
    conn=sqlite3.connect('dataentryform.db')
    c=conn.cursor()
    c.execute('SELECT * FROM dataform')
    data=c.fetchall()
    df=pd.DataFrame(data,columns=[desc[0] for desc in c.description])
    st.write(df.drop(columns=['image']))
    for index,row in df.iterrows():
             if row['image']is not None:
                 
             
                 image=Image.open(io.BytesIO(row['image']))
                 st.image(image,caption=f"image for {row['Name']}",use_column_width=True)
             
             
             
def main():
    st.title("STUDENT DATA")
    view_data()





