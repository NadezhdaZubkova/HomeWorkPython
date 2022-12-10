# 1 - Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11


# number= abs(float(input("Введите число: ")))
# while number!=int(number):
#     number*=10
# sum =0
# while number!=0:
#     sum+=number%10
#     number//=10
# print(int(sum))




# 2 - Напишите программу, которая принимает на вход число N
#  и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)


# N= int(input("Введите число: "))
# set_multyply=[]
# element=1
# for i in range(1,N+1):
#     set_multyply.append(element*i)
#     element=element*i

# print('Факториалы чисел от 1 до ', N , ': ', set_multyply)





# 3 - Дан массив размера N. После каждого отрицательного элемента 
# массива вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]


# import random

# N = int(input('Введите размер массива: '))
# list_of_numbers = []
# for i in range(N):
#     list_of_numbers.append(random.randint(-100, 100))

# print(list_of_numbers)

# for i in list_of_numbers:
#     if i<0:
#         list_of_numbers.insert(list_of_numbers.index(i)+1, 0)
# print(list_of_numbers)





# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. 
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, 
# остальные получили по две монеты. Далее человек, на котором остановился счет, 
# отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. 
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге.
#  Составьте алгоритм, который проводит эту игру. Если хотите делать паузы, 
# то импортируйте библиотеку time и используйте оттуда функцию sleep. 
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.
import random


num_people= int(input('Введите колличество игроков: '))
people_list= list(range(1,num_people+1))
start_count=0
coins=0  
# определяем индекс выбывшего игрока и количество монет
while len(people_list)!=1:
    dropped = random.randint(1, num_people*3) #чсло от ведущего
    print('\n Текущий круг людей',people_list)
    print('\n Число от ведущего',dropped)

    if dropped<=len(people_list):
        if (start_count + dropped-1)<len(people_list):
            out=start_count + dropped-1
        else: out=((start_count + dropped-1)%len(people_list))-1  # там ли -1?
        coins+= (2*len(people_list)) - dropped #суммарное количество монет за раунд

    else :
        if (start_count + dropped% len(people_list)-1)<len(people_list):
            out=(start_count + dropped % len(people_list))-1
        else: out=((start_count + dropped%len(people_list) -1)%len(people_list)) -1
       
        coins+=(2*len(people_list)) - dropped % len(people_list) - 1 #суммарное количество монет за раунд

    print('\n Выбывает человек под номером',people_list[out])
    if out+1<len(people_list):
        start_count=people_list[out+1]
    else: start_count=0
    people_list.remove(people_list[out])

print('Победил игрок: ', people_list, 'Выйгрыш составил', coins, 'монет')


