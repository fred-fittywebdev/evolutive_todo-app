from modules.functions import get_todos, write_todos
# from modules import functions
import time

now = time.strftime("%d %b %Y %H:%M")
print(now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'  # With the slice we retrieve only the words after 'add', so the todo only

        todos = get_todos()

        todos.append(todo.capitalize())

        write_todos(todos)
    elif user_action.startswith('show'):

        todos = get_todos()

        # we do a list comprehension to remove potentials multiples \n
        # new_todos = [todo.strip("\n") for todo in todos]

        for index, todo in enumerate(todos):
            row = f"{index + 1}-{todo.strip()}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            todo_number = int(user_action[5:])
            todo_number = todo_number - 1

            todos = get_todos()

            edited_todo = input('Enter a new todo: ').capitalize()
            todos[todo_number] = edited_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid. Please type the number of the todo")
            continue  # Allow us to run another cycle of the loop

    elif user_action.startswith('complete'):
        try:
            todo_number = int(user_action[9:])

            todos = get_todos()

            index = todo_number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo: {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue  # Allow us to run another cycle of the loop

    elif user_action.startswith('exit'):
        break

    else:
        print("command is not valid, try again.")


print("Bye, see you soon")
