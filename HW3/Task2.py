# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
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

def creature_random_list(List_len: int):
    '''
    Создаетранодомный список заданного размера
    Args- размер списка
    Reterns- список
    '''
    random_list = []
    for i in range(List_len):
        random_list.append(random.randint(-10, 10))
    return random_list

def symmetry_multiplication(some_list):
    '''
    Gives multiplication of elements on opposite positions
    Args: List with elements
    retern: list with multiplication
    '''
    multiplacation = list()
    for i in range(len(some_list)//2 +len(some_list)%2):
        multiplacation.append(some_list[i]*some_list[-1-i])
    return multiplacation

size = give_int('Введите размер списка ',1)
numbers = creature_random_list(size)
print(numbers)
print(f'Результат произведения чисел на симметричных позициях:{symmetry_multiplication(numbers)}')
