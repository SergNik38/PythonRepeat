num = input('Введите число: ')

try:
    int_num = int(num)
    print('Число целое')
except ValueError:
    print('Число дробное')
    int_num = int(num.split('.')[0])
    fract_num = int(num.split('.')[1][0])

    if int_num == fract_num:
        print(True)
    else:
        print(False)
