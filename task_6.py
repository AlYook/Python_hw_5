"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def guess_number(hidden, count=0):
    num = int(input('Введите число: '))

    count += 1

    if count > 10:
        print('Увы, у вас не получилось угадать. Загаданное число было {hidden}')
        return

    if num < hidden:
        print(f'Указанное вами число меньше загаданного. У вас осталось {10 - count} попыток')
        guess_number(hidden, count)
    
    elif num > hidden:
        print(f'Указанное вами число больше загаданного. У вас осталось {10 - count} попыток')
        guess_number(hidden, count)

    elif num == hidden:
        print(f'Вы угадали !')
        return


hidden = random.randint(0, 100)

guess_number(hidden)
