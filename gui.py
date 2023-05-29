from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type a ToDo please.")
input_box = sg.InputText(tooltip="Enter a todo", key="task")
add_todo_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window("My ToDo application",
                   layout=[[label], [input_box, add_todo_button],
                           [list_box],
                           [edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)  # Add
    print(2, values)  # {'task': 'Add warm'}
    print(3, values['todos'])

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["task"].capitalize() + '\n'
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == "Edit":
        todo_to_edit = values["todos"][0]
        new_todo = values['task'].capitalize() + '\n'

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == 'Complete':
        todo_to_complete = values['todos'][0]
        todos = functions.get_todos()
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['task'].update(value='')

    elif event == 'todos':
        window['task'].update(value=values['todos'][0])

    elif event == sg.WIN_CLOSED or event == 'Exit':
        break


window.close()
