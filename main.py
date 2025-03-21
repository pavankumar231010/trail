import streamlit as st

st.title('Hello World')
st.write('This Is A simple Streamlit App')

st.chat_input("Enter Your search")

if st.button('Hello'):
    st.write('Hello, World!')
