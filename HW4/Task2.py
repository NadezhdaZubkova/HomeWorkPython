# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

sequence_of_numbers = [1,1,6,4,1,5,6,2,5,1,7,4,1]
def nonrepeating_son (sequence: list):
    '''
     Outputs a list of non-repeating elements of the original sequence
     Args: list
     Return: list

    '''
    nonrepeat=[]
    for i in sequence:
        if i not in nonrepeat:
            nonrepeat.append(i)
    return nonrepeat

print('Исходная последовательность: ', sequence_of_numbers)
print(f'Неповторяющаяся последовательность: {nonrepeating_son(sequence_of_numbers)}')
