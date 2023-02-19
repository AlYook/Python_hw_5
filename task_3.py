"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""

def reverse(num, end_null, reversed=0):

    if num == 0:
        if end_null:
            reversed = '0' + str(reversed)

        print(f'Перевернутое число: {reversed}')
        return
    
    else:
        reverse(num // 10, end_null, reversed * 10 + num % 10)


num = input('Введите число, которое требуется перевернуть:' )

if num[-1] == '0':
    end_null = True
else:
    end_null = False

reverse(int(num), end_null)