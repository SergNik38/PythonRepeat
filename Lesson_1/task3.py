from random import randint


def random_generator(a, b, n):
    result = {}
    for i in range(1, n + 1):
        val = randint(a, b)
        key = f'elem_{i}'
        result[key] = val
    return result


a = int(input('Введите нижний диапазон: '))
b = int(input('Введите верхний диапазон: '))
n = int(input('Введите количество чисел: '))

print(random_generator(a, b, n))
