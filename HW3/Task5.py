# 5-Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

from typing import Optional # как-то можно обойтись без этой строкт?

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

def fibonachi_neg_pos(num:int):
    '''
    Выводит список чисел Фибоначчи с положительными b отрицательными индексами
    Args: int
    return: list
    '''
    np_fibo= [0]
    fib1=0
    fib2=1
    neg=1
    for i in range(1, num+1):
        fib1,fib2=fib2, fib1+fib2
        np_fibo.append(fib1)
        np_fibo.insert(0, neg*fib1)
        neg*=-1
    return np_fibo

 

number = give_int('Введите число ')
print(fibonachi_neg_pos(number))


