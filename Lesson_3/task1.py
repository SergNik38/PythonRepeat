import os


def get_file_name():
    file_path = input('Введите имя файла: ')
    full_file_name = os.path.basename(file_path)
    print(f'Имя файла с расширением: {full_file_name}')
    file_name = full_file_name.split('.')[0]
    print(f'Имя файла без расширения: {file_name}')


if __name__ == '__main__':
    get_file_name()
