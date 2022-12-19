# 1- Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

N = int(input('Введите размер массива: '))

def creature_random_list(Num):
    '''
    Создает ранодомный список заданного размера
    Args- размер списка
    Reterns- список
    '''
    random_list = []
    for i in range(Num):
        random_list.append(random.randint(-100, 100))
    return random_list


def sum_odd_index(Any_list):
    ''' 
    Считает сумму элементов с нечетными индексами
    Args - список чисел
    Reterns - сумма чисел
    '''
    Summa= 0
    for i in range(1, len(Any_list), 2):
        Summa+= Any_list[i]
    return Summa

Some_list = creature_random_list(N)
result = sum_odd_index(Some_list)
print(Some_list)
print(result)
