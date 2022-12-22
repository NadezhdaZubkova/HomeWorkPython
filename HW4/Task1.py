# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

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

def prime_factors(N : int):
    '''
    Give prime factors of number
    Args - int
    Returns - list
    '''
    pf = []
    for i in range(2,N):
        if N % i ==0:
            pf.append(i)
            N//=i
    return pf

num = give_int('Введите число:' , 1)
print(f'Простые множители числа {num} : {prime_factors(num)}')