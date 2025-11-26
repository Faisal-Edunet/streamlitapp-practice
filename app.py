import streamlit as st

st.title("Hello from Streamlit + uv 🚀")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome, {name}!")