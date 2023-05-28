from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type a ToDo please.")
input_box = sg.InputText(tooltip="Enter a todo", key="task")
add_todo_button = sg.Button("Add")

window = sg.Window("My ToDo application",
                   layout=[[label], [input_box, add_todo_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)  # Add
    print(values)  # {'task': 'Add warm'}

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["task"].capitalize() + '\n'
        todos.append(new_todo)
        functions.write_todos(todos)

    elif event == sg.WIN_CLOSED:
        break


window.close()
