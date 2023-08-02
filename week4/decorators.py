"""============ декораторы ==================="""



# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# print(outer(9))

# inner_func = outer(9)
# print(inner_func(8))
# a = print
# a('nurs')
# print(a)


"""
функция высщего порядка -> это функция которая может принимать в качество аргумента другую функцию 
и\или возвращвть функцию как результат
"""

# def test_func(func):
#     def inner_test_func():
#         func()
#     return inner_test_func

# def hello(func):
#     <telo>
#     pass




"""
декорфторы -  функция высшего порядка (в качестве арг принимает функцию и возвр функцию),
которая оборачивает другую функцию для расширения ее функционала при этом не изминяя ее код
"""


# from typing import Callable

# def test_decor(func: Callable) -> None:
#     func()
#     print('hello')

# def a():
#     print('привет')
    
# test_decor(a)


# def benchmark(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         func(args,kwargs)
#         stop = time.time()
#         print(f'время работы функции {func.__name__} {stop - start}')
#     return wrapper


# @benchmark
# def loop(a,d):
#     i = 0
#     while i < 1000000:
#         # print(i)
#         i += 1
    

# loop(2,3)



# @benchmark
# def test_for_loop(d,f):
#     for i in range(1000000):
#         pass
#         # print(i)
# test_for_loop(1,2)




# @benchmark
# def inp_str(w,e):
#     str_ = input('enter string: ')
#     return str_

# inp_str(5,6)




"""
============================== синтакси ========================
"""
# def decorator(func):
#     def wrapper():
#         print('функция обёртка!')
#         print(f'оборачиваем функцию {func.__name__}')
#         func()
#         print('выходим из обёртки')
#     return wrapper


# # @decorator
# def say_hi():
#     print('hiiiiiiii')


# # say_hi()

# say_hi = decorator(say_hi)
# say_hi()



"""
как работает @ под капотом 



@ -> синтаксический сахар, позволяет нам явно указать какой декоратор принимается для функции


под капотом вызывает функцию decorator и результат выполнения этой функции сохраняет в переменной 
с точно таким же названием как и обернутая функция
say_hi = decorator(say_hi)
say_hi()
"""





# def uppercase_decorator(func):
#     def wrapper():
#         func_ = func()
#         upper_str = func_.upper()
#         return upper_str
#     return wrapper


# @uppercase_decorator
# def inp_str():
#     str_ = input('enter string: ')
#     return str_

# print(inp_str())





# def smart(func):
#     def wrapper(x,y):
#         print('=======')
#         if y == 0:
#             return
#         return func(x,y)
#     return wrapper


# @smart
# def division(x,y):
#     return x / y

# print(division(3, 0))
# print(division(9, 3))







# def decorator(num):
#     def inner_dec(func):
#         def wrapper(*args,**kwargs):
#             for i in range(num):
#                 func(*args,**kwargs)
#         return wrapper
#     return inner_dec


# @decorator(7)
# def test(a):
#     print(f'============{a}\n++++++++++++')

# test(2)


        
# def strong(func):
#     def wrapper():
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper():
#         return '<div>' + func() + ' зима близко' + '</div>'
#     return wrapper


# @strong
# @div
# def get():
#     return 'Jhon Snow'
# print(get())


# def repeat(num):
#     def inner_dec(func):
#         def wrapper(*args,**kwargs):
#             for i in range(num):
#                 func(*args,*kwargs)
#         return wrapper
#     return inner_dec

# @repeat(5)
# def function(name):
#     print(f'{name}')

# function('nurs')


# def decorator(dec_arg): 
#     def wrapper(func): 
#         def wrapper2(func_arg): 
#             if dec_arg == 'start': 
#                 func(func_arg) 
#             else: 
#                 print('функция не запущена') 
#         return wrapper2 
#     return wrapper 

# @decorator('start') 
# def func(word): 
#    print(word)

# func('Hello!') 











































# task 1
# def call_function(func):
#     def wrapper():
#         print(f'Вызываю функцию {func.__name__}')
#         func()
#         print(f'Вызов функции {func.__name__} прошёл успешно')
#     return wrapper


# @call_function
# def first():
#     print("hello world")
#     return "hello world"

# first()





"""
Вызываю функцию first
hello world 
Вызов функции first прошёл успешно 
"""














# task 2
# def func_start_time(func):
#     def wrapper():
#         import datetime
#         print(f'Функция запущена {datetime.datetime.now()}')
#         func()
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')
# func()













# task 3
# def make_bold(func):
#     def wrapper():
#         return '<b>' + func() + '</b>'
#     return wrapper


# def make_italic(func):
#     def wrapper():
#         return '<i>' + func() + '</i>'
#     return wrapper


# def make_underline(func):
#     def wrapper():
#         return '<u>' + func() + '</u>'
#     return wrapper
    
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())













# task 4
# import requests

# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         stop = time.time()
#         print(f'Время выполнения: {stop - start} секунд.')
#     return wrapper


# @benchmark 
# def fetch_webpage(): 
#     webpage = requests.get('https://google.com')

# fetch_webpage()

















# task 5
# users = {'nurs': 123,
#          'azi': 456,
#          'love': 789}

# def validate_password(func):
#     def wrapper(username,password):
#         if not username in users:
#             print('Username is not defined ')
#             return
#         elif users[username] != password:
#             print('Password is invalid ')
#             return
#         else:
#             return func(username,password)
#     return wrapper         

# @validate_password
# def login(username, password):
#     print(f'Welcome, {username}')

# login('nurs',123)




# users = {'Tim':'1234', 'Alex':'qwert', 'Sadyr':'654' } 
# def validate_password(func): 
#     def wrapper(username, password): 
#         if username not in users: 
#             print("Username is not defined") 
#             return 
#         elif users[username] != password: 
#             print("Password is invalid") 
#             return 
#         else: 
#             return func(username, password) 
#     return wrapper 
# @validate_password 
# def login(username, password): 
#     print(f'Welcome, {username}') 
# login('Tim','1234')






















# task 6

# def is_admin(func):
#     def wrapper(dict):
#         if dict['is_admin'] == True:
#             print(f'Доступ разрешен {dict["username"]}')
#             return func(dict)
#         else:
#             print(f'Доступ запрещен {dict["username"]}')
#             return func(dict)
#     return wrapper

# @is_admin
# def get_user(dict):
#     return dict
 
# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})


































# task 7


# def route(func):
#     def wrapper(path):
#         url = 'https://www.mywebsite.com/' + func(path)
#         return url
#     return wrapper

# @route
# def get_page(path):
#     return path
 
# print(get_page('about/'))
# print(get_page('products/'))




















# task 8
# def sort_names(func):
#     def wrapper(list):
#         sorted_list = sorted(list, key=lambda i: i[2])
#         return func(sorted_list)
#     return wrapper

# @sort_names
# def prefix_name(person: list) -> list:
#     list_ = []
#     for i in person:
#         if i[3] == 'M':
#             list_.append(f'Mr. {i[0] + " " + i[1]}')
#         elif i[3] == 'F':
#             list_.append(f'Ms. {i[0] + " " + i[1]}')
#     return list_


# print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
#       ('Carrie', 'Fisher', 35, 'F'),
#       ('Harrison', 'Ford', 38, 'M')]))





































# task 9
# def get_full_number(func):
#     def wrapper(list):
#         list1 = []
#         for i in list:
#             list1.append(f'+996 {i[1:4] + " " + i[4::]}')
#         return func(list1)
#     return wrapper

# @get_full_number
# def sort_phone_nums(list_):
#     sorted_list = sorted(list_)
#     str_ = '#'.join(sorted_list) 
#     print(str_)

# sort_phone_nums(['0777987456', '0555123456', '0770369852'])


































# task 10

# def type_check(correct_type):
#     def wrapper(func):
#         def wrapper2(func_arg):
#             if correct_type == type(func_arg):
#                 func(func_arg)
#             else:
#                 print('Неверный тип данных :(')
#         return wrapper2
#     return wrapper

# @type_check(int)
# def func1(num):
#     print(num*2)
 
# func1(2)
# func1({1: 'какой-то', 2: 'словарь'})

































