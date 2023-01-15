FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Check the file with the todos and returns
    it as a list.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ Write a to-do items list in the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)


def complete_all(filepath=FILEPATH):
    with open(filepath, "w") as local_file:
        local_file.writelines([])
        print("List was cleaned!")
