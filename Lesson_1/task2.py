import os
from pprint import pprint
path = input('Введите путь до директории: ')


def print_directory_contents(path):
    content = os.listdir(path)
    for el in content:
        if not os.path.isfile(os.path.join(path, el)):
            print_directory_contents(os.path.join(path, el))
    pprint(content)


print_directory_contents(path)
