import streamlit as st
import sqlite3
import pandas as pd
from PIL import Image
import io
import smtplib

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
    conn = sqlite3.connect('dataentryform.db')
    c = conn.cursor()
    c.execute('SELECT * FROM dataform')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=[desc[0] for desc in c.description])
    st.write(df.drop(columns=['image']))
    for index, row in df.iterrows():
        if row['image'] is not None:
            image = Image.open(io.BytesIO(row['image']))
            st.image(image, caption=f"image for {row['Name']}", use_column_width=True)
    return df

def create_selected_students_db():
    conn = sqlite3.connect('selected_students.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS selected_students (
            Name TEXT,
            Email TEXT,
        
        )
    ''')
    conn.commit()
    conn.close()

def insert_selected_student(student_data):
    conn = sqlite3.connect('selected_students.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO selected_students (Name, Email)
        VALUES (?, ?)
    ''', student_data)
    conn.commit()
    conn.close()

def main():
    st.title("STUDENT DATA")
    if 'df' not in st.session_state:
        st.session_state.df = view_data()

    df = st.session_state.df
    st.subheader("Select Students to send the message in email ID")

    with st.form(key='student_form'):
        student_options = df['Name'].tolist()
        selected_students = st.multiselect('Select Students', student_options)
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        email_sender = "pythonleo637@gmail.com"
        subject = "Congratulations, you have been selected"
        body = '''Congratulations, you have been selected for 11th class. Please come and meet the principal.
                  School opening next week.
                  THANK YOU!'''

        for student in selected_students:
            email = df[df['Name'] == student]['Email'].values[0]
            st.write(f"Selected student to send the message {student}: {email}")

            try:
                text = f"Subject: {subject}\n\n{body}"

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email_sender, "dttp oczk lhik geoy")
                server.sendmail(email_sender, email, text)
                server.quit()

                st.write(f"Email sent successfully to {email}")

                # Save the selected student's data into the new database
                student_data = (student, email)
                insert_selected_student(student_data)
                st.write(f"Data for {student} saved in selected_students database.")

            except Exception as e:
                st.write(f"Failed to send email to {email}. Error: {e}")

if __name__ == "__main__":
    
    create_selected_students_db()
    
