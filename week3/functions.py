'''Ввведение в функции'''

'''Аннотации -> помогают сделать код информативным и избавиться от некоторых проблем динамической типизации, никак не влияет на работу кода'''

# num: int = 10 # предупредить какой тип данных нужно передавать, присваивать
# num = 'hello'
# print(num)

'''========== Функции =========='''
# Функция -> именованный блок кода (есть имя), которыйвыполняет одну задачу
# Может принимать в себя аргументы и возвращать результат
# вызывается многократно, по имени.


# def -> ключевое слово для объявления функции (указывает питону, что мы хотим создать функцию)

'''Синтаксис'''
# def <название_функции>(параметры):
#     <тело функции>


# def my_len(obj):
#     count = 0
#     for i in obj:
#         count += 1
#     print(count)
#     return count


# my_len([1, 2, 3, 4, 5])
# a = my_len([1, 2, 3, 4, 5])
# print(a)

# func = my_len
# print(func([1, 2, 3, 4, 5]))
# print(func)
# a = print
# a('hello')
# b = 10
# b()
# print(type(my_len))


# def sum_(num1: int, num2: int):
#     res = num1 + num2
#     print(res)
#     return res

# a = sum_(2, 3)
# print(a)
# # sum_(4, 'he')
# print(sum_(1, 2))

# sum_(sum_(2, 3), sum_(1, 2))
# a = sum_(1, 2) #без return None (3)
# b = sum_(9, 8) # без return None (17)
# c = sum_(9, 45) # без return None (54)

'''return -> используется для возвращения результата, который можно сохранить в переменной и где-то использовать, после return функция завершает свою работу, если в функции не прописан return -> функция возвращает None'''

# str_ = 'hello'
# print(str_.replace('h', 'hello')) # helloello

# list_ = [1, 2, 3, 4]
# print(list_.append([7, 8, 9]))
# print(list_)


'''======= Параметры и аргументы ======'''

# Параметры -> локальные переменные внутри функи, значения параметрам задаются при вызове фукции
# Аргументы -> значения, которые мы задаем параметрам

# def a(параметр):
#     pass

# a(аргумент)

''' ====== Виды параметров ======'''

# 1. обязательные (a, b, list_) -> определяют, какие аргументы нужно передать
# 2. не обязательные 
# 2.1 с дефолтом (имеет значение по умолчанию)
# 2.2 args -> принимает (все) неименованные аргументы, которые не относятся к обязательным (tuple)
# 2.3 kwargs -> принимает (все) именованные аргументы (dict)
# a=17

# def func(a = 0, *args, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs)

# func(3, 4, 4, n = 0, m = 7)


'''========= Виды аргументов ========='''
# 1. позиционные -> по позиции (a, b, c) -> (1,2,3) a = 1 b = 2 c = 3 
# 2. именнованные (по названию) 

# 2.
# def test(a, b, c):
#     print(a, b, c)

# test(1, b = 4, c = 2)

# 1.
# def test(a: int, b: int, c: list, n=4):
#     print(a, b, c)

# test()


# Pаспаковка
# list_ = [*range(1, 11)]
# print(list_)

# dict1 = {'a':1, 'b': 2, 'c': 3}
# dict2 = {*dict1}
# dict2 = {**dict1}
# print(dict2)

# def print(a):
#     return a

# print(2)
# print('hello')

# # sum 

# def sum_numbers(number1, number2, *args, **kwargs):
#     print(args, kwargs)
#     print(kwargs.values())
#     return number1 + number2 + sum(args) + sum(kwargs.values())

# print(sum_numbers(1, 7))
# print(sum_numbers(1, 7, 99, 8, 5, n = 9, k = 87, o = 0))


# while True:
# def add_(a,b):
#     return a + b
# def sub_(a,b):
#     return a - b
# def mult_(a,b):
#     return a * b
# def div_(a,b):
#     return a / b
   
# def calc(num1, num2, a):
#         if a == '+':
#             return add_(num1,num2)
#         elif a == '-':
#             return sub_(num1,num2)
#         elif a == '*':
#             return mult_(num1,num2)
#         elif a == '/':
#             return div_(num1,num2)
        
             
# print(calc(12,23,'*'))

















    #     num1 = int(input('enter the first number: '))
    #     num2 = int(input('enter the second number: '))
        
    #     dictionary = {'+': add(num1, num2),
    #                 '-': substract(num1, num2),
    #                 '*': multiply(num1, num2),
    #                 '/': division(num1, num2)}
        
    #     some_result = dictionary[action]
    #     return result(some_result)

    # action = input('select action + - * / ' + '\n: ')
    # print(calculator(action))


# def ice_cream(name,size,*args):
    
#     return f'your ice cream {name}, {size}, with {args}'


# print(ice_cream('plumbir','big','nuts'))





# def generation_password(a,b):
#     import random 
#     random_list = random.sample(range(1,10), k=7)
#     random_list = [str(i) for i in random_list]
#     password = a + b + ''.join(random_list)
#     return password

# def get_info(name = input('enter your name: '),
#             last_name = input('enter your last name: ')):
#     password = generation_password(a = name,b = last_name)
#     return password

# print(get_info())























































































# task 1
# def add(a,b):
#     return a + b



# task 2
# def get_string_length(a):
#     return len(a)


# task 3
# def get_type(x,y): 
#     print(f'{type(x)}\n{type(y)}') 
# get_type(5,'s')







# task 4
# def divide(a,b):
#     return a / b 


# task 5
# dict_ = {'a': 1, 'b': 2, 'c':3}

# def dictionary(a):
#     for keys in a:
#         print(keys)



# # task 6
# num = 6
# def check(number):
#     if number % 2 == 0:
#         return("It is even number")
#     else:
#         return("It is odd number")

# print(check(num))


# def check_type(elem): 
#  if type(elem) == str: 
#      print('это строка') 
#  elif type(elem) == int: 
#      print('это число') 
#  else: 
#      print('что-то другое') 

# print(check_type(10)) 


# num = 6 
# def check(num): 
#     if num % 2 == 0: 
#         return("It is even number") 
#     else: 
#         return("It is odd number")


# task 7
# def is_palindrome(a):
#     if a.lower()[0::] == a.lower()[::-1]:
#         return(True) 
#     else:
#         return(False)

# print(is_palindrome('Mom'))


# task 8
# def max_num(a,b):
#     if a > b:
#         return(a)
#     else:
#         return(b)
# print(max_num(10, 12))


# task 9
# def multiply_list(a):
#     n = 1
#     for i in a:
#         n *= i
#     return(n)
# print(multiply_list([1, 2, 3, 4, 5, 6])) 



# task 10
# def  sum_digits():



# a = 105
# def sum_digits(num): 
#     return(sum([int(i) for i in str(num)])) 
# print(sum_digits(105))





# task 11
# def func11(a,b,c):
#     try:
#         res = (a + b) / c
#     except ZeroDivisionError:
#             res = a + b
#     return(res)




# task 12
# def func12(list_,a):
#     n = []
#     for i in list_:
#         if a == 'lower':
#             n.append(i.lower())
#         elif a == 'upper':
#             n.append(i.upper())
#     return(n)

# print(func12(["hEllo", "wORld"], "upper"))



# task 13
# def func13(str): 
#     return {x:str.count(x) for x in str} 

# print(func13("Hello"))


# task 14
# def add_(a,b):
#     return a + b
# def sub_(a,b):
#     return a - b
# def mult_(a,b):
#     return a * b
# def div_(a,b):
#     return a / b
   
# def calc(num1, num2, a):
#         if a == '+':
#             return add_(num1,num2)
#         elif a == '-':
#             return sub_(num1,num2)
#         elif a == '*':
#             return mult_(num1,num2)
#         elif a == '/':
#             return div_(num1,num2)
        
             
# print(calc(12,23,'*'))




# task 15
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]

# def func15(users): 
#     a=[] 
#     for i in users: 
#         if i['work'].startswith('IT'): 
#             a.append(f"{i['name']}, скидки в магазине компьютерной техники!\n") 
#             b = ''.join(i for i in a) 
#     return b 


# print(func15(users))



# task 16
# def func16(km: int or float,benza: int or float) -> int or float:
#     result = round(benza * 100 / km)
#     return f'На 100км было расходовано {result}л горючего' 

# print(func16(1200,233))




# task 17
# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]



# def func17(_list_):
#     for i in _list_:
#         res =  i['salary'] + i['overTime'] * 200
#         i['salary'] = res
#         i.pop('overTime')
#     return _list_

# print(func17(employees))


# task 18
# list1 = ['dff','dfgdg',1,2,3,4,'hello','nurs']
# def func18(list_):
#     list_int = []
#     list_str = []
#     for i in list_:
#         if type(i) == int:
#             list_int.append(i)
#         elif type(i) is str:
#             list_str.append(i)
#     return list_int, list_str

# print(func18(list1))


# task 19
# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]



# def func19(list_: list):
#     for x in list_:
#         list_.sort(key=lambda x: x['marks'], reverse=True)
#     return list_
# print(func19(students))





# task 20
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]



# def func20(list_: list, string: str):
#     list1 = []
#     for i in list_:
#         if string.lower() in i['title'].lower():
#             list1.append(i)
#     return list1    

# print(func20(products,'I'))






