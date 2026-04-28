import streamlit as st
#title of app
st.title("my first streamilt app" )
#adding content
st.write("hello! I am creating a simple web application.")


# adding input
name=st.text_input("enter your name")
age=st.number_input("enter your age")



#display
if st.button("submit"):
 st.write("hello,{name}! Welcome to Streamlit.")
