# 4- Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

from typing import Optional

def give_int(input_string: str,
            min_num: Optional[int] = None,
            max_num: Optional[int] = None)-> int:
    '''
        Выпытывает число
    Args:
        input_string - предложение ввода
        min_num - минимальное число диапозона
        max_num - максимальное число диапозона
    Returns:
        int - число
    '''
    while True:
        try:
            num = int(input(input_string))
            if min_num and num<min_num:
                print(f'Введите больше {min_num}')
                continue 
            if max_num and num>max_num:
                print(f'Введите число меньше,чем {max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')

def int_to_be(N: int):
    '''
    Преобразует десятичное число в двоичное
    Args - int
    Result - string
    '''
    be_list = []
    while N != 0:
        be_list.insert(0, N%2)
        N = N//2
    
    return be_list

num = give_int('Введите число')
be_num = int_to_be(num)
print('Число ', num, 'в двоичной системе равно: ') 
print("".join(str(x) for x in be_num))

