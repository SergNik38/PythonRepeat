import os
import random


def create_file(name):
    word = 'example'
    list_words = [word for i in range(100)]
    list_nums = [i for i in range(100)]
    new_list = list(zip(list_words, list_nums))

    if os.path.exists(f'{name}.txt'):
        print('File already exists')
        return
    with open(f'{name}.txt', 'w', encoding='utf-8') as f:
        for el in new_list:
            rand = random.random()
            if rand >= 0.5:
                f.write(f'{el[0]}{el[1]} \n')
            else:
                f.write(f'{el[1]}{el[0]} \n')
        f.close()


def show_file(name):
    if os.path.isfile(f'{name}.txt'):
        with open(f'{name}.txt', 'r', encoding='utf-8') as f:
            for el in f:
                print(el, end='')
            f.close()


def find_element(name, elem):
    mode = input('Поиск первого вхождения - 1 \nПоиск всех вхождений - 2\n')
    with open(f'{name}.txt', 'r', encoding='utf-8') as f:
        if mode == '1':
            for el in f:
                if el == f'{elem} \n':
                    print(el)
                    return
        if mode == '2':
            for el in f:
                if el == f'{elem} \n':
                    print(el)
        f.close()


def replace_elem(file, elem, new_name):
    with open(f'{file}.txt', 'r', encoding='utf-8') as f:
        for el in f:
            if el == f'{elem} \n':
                el = f'{new_name} \n'
                print(el)

        f.close()


if __name__ == '__main__':
    create_file('file')
    show_file('file')
    find_element('file', 'example7')
    replace_elem('file', 'example7', 'NEW_NAME')
