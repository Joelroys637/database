import streamlit as st


def main():
    original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;"> </h1>'
    st.markdown(original_title, unsafe_allow_html=True)



# Set the background image
    background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://directory.edugorilla.com/wp-content/uploads/sites/6/2018/03/318a8eaacbd67f8a5474ff7861a463f2.jpeg");
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









    st.title("Dalmia higher secondary school")
    st.header("Details:")
    st.header("DALMIA HR.SEC.SCHOOL, DALMIAPURAM was established in 1950 and it is managed by the Pvt. Aided.")
    st.image("images.jpg",width=700)


    st.header("The school has Private building. It has got 22 classrooms for instructional purposes. All the classrooms are in good condition. It has 2 other rooms for non-teaching activities. The school has a separate room for Head master/Teacher. The school has Pucca boundary wall. The school has have electric connection. The source of Drinking Water in the school is Tap Water and it is functional.")
    
    st.image("event.jpeg")

    
    st.header("It is located in Urban area. It is located in PULLAMBADI block of TIRUCHIRAPPALLI district of Tamil Nadu.")
    c1,c2=st.columns(2,gap="small")
    
    c1.image("location.png")
    c2.header("DALMIA SCHOOL DALMIAPURAM,Trichy-621 651,Tamilnadu")
    st.header("Contact: +123456789")
    st.header("mail: dalmiaschool@gmail.com")
