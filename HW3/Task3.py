# 3-Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
from typing import Optional
import random

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

def creature_random_list(List_len: int, N: int):
    '''
    Создает ранодомный список заданного размера
    Args- размер списка, количество знаков после запятой
    Reterns- список
    '''
    random_list = []
    for i in range(List_len):
        random_list.append(round(random.uniform(-5,5), N))
    return random_list

def max_min_diff(some_list: list, N: int):
    '''
    Дает разницу между максимальным и минимальным значениями дробной части элементов 
    Args: список элементов, количество знаков после запятой
    Returns: число
    '''
    max_fract = 0.0
    min_fract= 1.0
    for i in range(len(some_list)):
        fract_part = round(some_list[i]%1, N)
        if fract_part>= max_fract:
            max_fract=fract_part
        if fract_part<=min_fract:
                min_fract=fract_part
    print("Max = ", max_fract)
    print('Min = ', min_fract)
    difference = round(max_fract-min_fract, N)
    return difference



size = give_int('Введите размер списка ',1)
number_of_decimal_places =give_int('Введите количество знаков после запятой ',1)
numbers = creature_random_list(size,number_of_decimal_places)
print(numbers)
print(f'Difference = {max_min_diff(numbers, number_of_decimal_places)}')
