import os


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
            f.write(f'{el[0]}{el[1]} \n')
        f.close()


def show_file(name):
    if os.path.isfile(f'{name}.txt'):
        with open(f'{name}.txt', 'r', encoding='utf-8') as f:
            for el in f:
                print(el, end='')
            f.close()


if __name__ == '__main__':
    create_file('file')
    show_file('file')
