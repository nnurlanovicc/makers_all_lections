
#виды комментов
'''
1.многострочные
'''
"""многострочные"""
#2.

'''
обзор типов данных
типы дынных в Питоне
'''

# 1. NoneType ->
# 2. Boolen (bool()) -> True/False
# 3. Числовые типы данных:
    # a. integer (int()) -> 1 2 3 ... целые числа 
    # b. float() -> 1.6 5.99 числа с плавающей точкой
    # c. complex(3, 5) -> 3 + 5j
# 4. string (str()) -> "hello" 'makers' """ """" ''' ''' ... строки
# 5. list () -> [1, 2, 2, None, True, 'Hello', [1, 2, 3,], {1: 'a'}] списки
# 6. tuple() -> (1, 2, 3, None, False) кортеж
# 7. set() -> {1, 2, 3, 4, 5} множество
# 8. dict() -> {1: 'one', 2: 'two'} словарь
# 9. frozenset() -> замароженное множество


'''Изминяемые (Mutable)'''
# set ()
# dict () 
# list() 


'''========== переменные========='''
# ссылка для ячейки памяти в котой хранится объект. Предназначена для хранения данных 

# hello_world = 'snake case'
# helloworld = 'camel case' 

# num = 10 
# num_2 = 11
# name = 'Nurs'
# age = 32
# is_user = True 

# print () -> функция для вывода данных в терминал 

# print(hello_world)
# print(helloworld)

# num3 = num + num_2 
# print(num3)

# input () -> функция ввода данных с терминала 
# name = input('enter your name : ')


3 
'3'
# type() -> вводит тип данных
# print(type(3)) 
# print('3' + '3') 

# int() -> для перевода в тип данных  целые числа

# number1 = int(input('Введите число'))
# # print(int(number1))
# print(type(number1))


# a = 1
# b = 2

# id () -> выводит номер ячейки в памяти 

# list_ =[1, 2, 3, 4]
# print(list_)
# print(id(list_))
# list_.append(5)
# print(list_)
# print(id(list) 


'''===========операция над числами============='''



#+

# number1 = 10 
# number2 = 88
# print(number1 + number2)




# _ 
# number_1 = 77 
# number_2 = 9
# print(number_1 - number_2)


# * -> Умножение

# print(number_1 * number_2) 
# number3 = number_1 * number_2 
# print(number3)


# / -> Деление

# division_result = number1 / number2
# print(division_result)


# % -> Для получения остатка от деления 

# a = 89
# b = 9
# print(a % b )
# print(a / b)
# c = 8 * 9
# print(c)
# print(a - c)

# print(00 * 0)

# // -> Целочисленное деление 


# a = 89
# b = 9
# print(a // b)



# ** ->  Возведение в степень 
# print(10 ** 2)
# print(5 ** 3)



# || -> Модуль числа |-9| из отрицательного сделает положительный 
# print(abs(-9)) 
# print(abs(10))


# pow -> 1. возВедение в степень
    #    2. Возвращает остаток деления 

# 1. 
# print(pow(5, 4))
# 2. 
# print(pow(5, 3, 9))




# divmode Принимает два числа и возвращает  два числа-> первое число - результат целочисленного деления, второе -> остаток от деления 

# print(divmod(9, 4 ))
# divmod(15, 5)  # (3, 0)





# round ()
# print(round(559/5))
# print(round(777/8, 3)) # Второй элемент указывает сколько чисел после запятой оставить 




# import math 

# print(dir(math))
# math.sqrt

# from math import sqrt 


# sqrt -> Для нахождения квадратного корня 


# print(math.sqrt(100))
# math.sqrt(36) 