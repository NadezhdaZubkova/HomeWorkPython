
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



def creature_random_list(Listlen: int):
    '''
    Создаетранодомный список заданного размера
    Args- размер списка
    Reterns- список
    '''
    random_list = []
    for i in range(Listlen):
        random_list.append(random.randint(-100, 100))
    return random_list