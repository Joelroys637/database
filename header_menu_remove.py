import streamlit as st


def headerhide():
    hide="""
    <style>
    #mainmenu {visiblity:hidden}
    
    header{visibility:hidden;}
    </style>
    """
    st.markdown(hide,unsafe_allow_html=True)

