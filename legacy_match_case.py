# Ask the user to enter a todo

while True:
    print("Type add, show, edit, complete or exit: ")
    user_action = input("> ")
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            print("Enter a todo")
            todo = input("> ") + "\n"  # Allow break line to print todos in file text in a better way

            with open('todos.txt', 'r') as todo_file:  # Using the context manager with
                todos = todo_file.readlines()

            todos.append(todo.capitalize())

            with open('todos.txt', 'w') as todo_file:
                todo_file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as todo_file:
                todos = todo_file.readlines()

            # we do a list comprehension to remove potentials multiples \n
            # new_todos = [todo.strip("\n") for todo in todos]

            for index, todo in enumerate(todos):
                row = f"{index + 1}-{todo.strip()}"
                print(row)

        case 'edit':
            todo_number = int(input("Enter the number of todo to edit: "))
            todo_number = todo_number - 1

            with open('todos.txt', 'r') as todo_file:
                todos = todo_file.readlines()

            edited_todo = input('Enter a new todo: ').capitalize()
            todos[todo_number] = edited_todo + '\n'

            with open('todos.txt', 'w') as todo_file:
                todo_file.writelines(todos)

        case 'complete':
            todo_number = int(input("Enter the number of todo to complete: "))

            with open('todos.txt', 'r') as todo_file:
                todos = todo_file.readlines()

            index = todo_number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as todo_file:
                todo_file.writelines(todos)

            message = f"Todo: {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break
        case _:  # Here on the fly python will take this case if the value entered is not one of the three first cases.
            print("Hey, you entered an unknown command ! Please try again.. ")
print("Bye, see you soon")





