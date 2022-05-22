
n = int(input('Введите число: '))

for i in range(1, n + 1):
    for x in range(1, 11):
        print(f'{i}x{x} = {i * x}')
    print('-----')

