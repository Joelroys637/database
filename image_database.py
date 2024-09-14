import streamlit as st
import sqlite3
from PIL import Image
import io
def main():
    
# Connect to SQLite database
    conn = sqlite3.connect('dataentryform.db')
    c = conn.cursor()

# Create table to store images if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS dataform
             (image BLOB)''')
    conn.commit()

# Function to convert image to binary data
    def img_to_bin(image):
        
       img_byte_array = io.BytesIO()
       image.save(img_byte_array, format=image.format)
       return img_byte_array.getvalue()

# Streamlit app title
    st.title("UPLOAD YOU PHOTO")

# File uploader for image
    uploaded_file = st.file_uploader("Choose an image only .jpg.png.jpeg", type=["jpg", "jpeg", "png"])

# If image is uploaded
    if uploaded_file is not None:
        
    # Display the image
       image = Image.open(uploaded_file)
       st.image(image, caption='Uploaded Image', use_column_width=True)

    # Button to save image to SQLite
       if st.button('Save Image'):
           
        # Convert image to binary
           img_bin = img_to_bin(image)
        # Insert image into database
           c.execute("INSERT INTO dataform (image) VALUES (?)", (sqlite3.Binary(img_bin),))
           conn.commit()
           st.success('you photo saved to the database.')
