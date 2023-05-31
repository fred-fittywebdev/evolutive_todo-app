import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("My Todo App.")
st.subheader("This is the third version of my Python TodoApp")
st.write("This app allow you to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")