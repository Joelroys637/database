import streamlit as st
import sqlite3
import pandas as pd
from PIL import Image
import io








def view_selected_students():
    st.title("View Selected Students")
    conn = sqlite3.connect('selected_students.db')
    c = conn.cursor()
    c.execute('SELECT * FROM selected_students')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['Name', 'Email'])
    conn.close()

    st.dataframe(df)
