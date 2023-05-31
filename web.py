import streamlit as st
from modules import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App.")
st.subheader("This is the third version of my Python TodoApp")
st.write("This app allow you to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()  # needed for checkboxes to rerun the app

st.text_input(label="Enter a todo", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

# st.session_state
