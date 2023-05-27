from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type a ToDo please.")
input_box = sg.InputText(tooltip="Enter a todo")
add_todo_button = sg.Button("Add")

window = sg.Window("My ToDo application", layout=[[label], [input_box, add_todo_button]])
window.read()
window.close()