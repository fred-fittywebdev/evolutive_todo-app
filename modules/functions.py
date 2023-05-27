FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of
     to-do items.
     """
    with open(filepath, 'r') as todo_file_local:
        todos_local = todo_file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in the text file """
    with open(filepath, 'w') as todo_file:
        todo_file.writelines(todos_arg)