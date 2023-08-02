


# def func(a):
#     a = 0
#     print('function')
# print(a) -> NameError: name 'a' is not defined




"""
1. builtins() -> print, input, len
"""
"""
2. global -> 
"""
"""
3. enclosed -> (не локальное , замкнутое ) находится между двумя пространствами
"""
"""
4. local -> 
"""

# name = 'nurs'

# def test():
#     hello = 'hello'

# print(globals())
# globals() -> возвращает все глобальные переменные


# print(dir(__builtins__)) -> Возвращает все встроенные имена

# x = 100
# y = 0
# z = 99
# x = 34

# globals()['x'] = 45
# print(globals())
# print(z is globals()['z'])


"""
локальные -> переменные в функциях
"""

# def func(test):
#     a = 10
#     b = 0
#     print(test)
#     print(z)
#     print(locals())

# func(6)

# locals() -> Возвращает все локальные имена, когда применяем на глобальном уровне, Возвращает все глобальные имена



# print(locals().items())
# print(locals().values())

# def func1():
#     a = 0
#     b = 9
#     print(a,b)

# func1()




# a = 8
# b = 7
# def func1():
#     print(a,b)

# func1()


# a = 8
# b= 7
# def func1():
#     a = 0
#     b = 9
#     print(a,b)

# func1()
# print(a,b)



"""
Enclosed -> возникает в том случае когда внутри функции объявляется еще функция (при вложенности функции)
"""

# def outer_func():
#     outer = 'не локальное переменное'
#     print(outer)
#     def inner_func():
#         inner = 'локальное переменное'
#         print(inner)
#         print(locals())
#     inner_func()
#     print(locals())


# outer_func()





"""
local -> enclosed -> global -> builtins
"""

# import this 
"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


# x = 10

# def func():
#     global x 
#     x += 20
#     print(x)

# func()
# print(x)


# y = 23

# def func0():
#     global y 
#     y = 20
#     print(y)

# func0()
# print(y)


# def func1():
#     global n
#     n = 34
#     print(n) 

# func1()



# z = [1,2,3,4]

# def func1():
#     z[0] = 0
#     print(z)

# func1()
# print(z)



# count = 0

# def counter():
#     global count
#     count += 1
#     return count

# # counter()
# # counter()
# # counter()
# # counter()

# name = input()
# age = input()
# print({'id': counter(), 'name': name, 'age': age})

# name = input()
# age = input()
# print({'id': counter(), 'name': name, 'age': age})

# name = input()
# age = input()
# print({'id': counter(), 'name': name, 'age': age})


# count = 0

# def counter():
#     # global count
#     try:
#         print(count)
#         count += 1
#     except:
#         print('k')


# counter()
# counter()
# counter()
# counter()

# a = 0

# def outer():
#     global a
#     a = 8
#     def inner():
#         global a
#         a = 10
#         print('inner a = ',a)
#     inner()
#     print('outer a =', a)

# outer()
# print('global a = ', a)




# def outer():
#     a = 8
#     def inner():
#         nonlocal a 
#         a = 10
#         print('inner a = ',a)
#     inner()
#     print('outer a =', a)

# outer()





# from time import sleep
# def counter(number):
#     count = 0
#     def add():
#         nonlocal count
#         count += 1
#         print(count)
#         sleep(1)
#     for i in range(number):
#         add()

# counter(10)





# from time import sleep
# def counter(number):
#     count = number
#     def add():
#         nonlocal count
#         count -= 1
#         print(count)
#         sleep(1)
#     for i in range(number):
#         add()

# counter(10)



# def countdown(num):
    
#     def inner_dec(func):
#         count = num + 1
#         def wrapper(*args,**kwargs):
#             nonlocal count
#             count -= 1
#             print(count)
#             sleep(1)
#         for i in range(num):
#             wrapper()
#         func()      
#         return wrapper
#     return inner_dec

# @countdown(5)
# def func():
#     print('hello')
















































# task 1
# def foo():
    
#     var = 'переменная foo'
#     print('переменная в foo:  переменная foo')
#     def bar():
#         global var
#         var = 'переменная bar'
        
 
#     bar()
# foo()
# print('переменная в foo: ', var)


# task 2
# x = 'Я глобальная переменная!'

# def my_func():
    
#     global x
#     print(x)
#     x = 'Я могу изменяться'
    

# my_func()
# print(x)
# print(globals())


# task 3
# num = 3

# def mul():
#     global num
#     num =  num ** 2
#     return num

# mul()
# mul()
# mul()
# print(num)



# task 4
# balance = 0

# def get_salary(amount):
#     global balance
#     balance += amount



# def pay_bills(amount: int, log_name: str):
#     global balance
#     balance -= amount
#     print(f"Вы заплатили {amount} сом за {log_name}")


# # pay_bills(300,'internet')

# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')


# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# task 5
# result = 0


# def pow_first(x,y):
#     global result
#     result = x ** y



# def pow_second(z):
#     global result
#     result = result % z

# pow_first(2, 3)
# pow_second(3)
# print(result)


# task 6
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}


# def control(dict_: dict):
#     for key,value in dict_.items():
#         if value >=17:
#             print(f'{key}, Вы можете войти в клуб')
#         else:
#             print(f'{key}, извините, Вы не проходите по age-control')

# control(a)


# task 7
# a =  ['pipi', 'papa', 'mama']
# b = []
# def vr(list_:list):
#     for i in list_:
#         b.append(i.capitalize())
#     print(b)

    
# vr(a)

# task 8
# def count_symbols(str_: str):
#     a = []
#     b = []
#     c = []
#     gl = ['а','у','э','о','ы','и','е','я','ё','ю']
#     sgl = ['й','ц','к','н','г','ш','щ','з','х','ф','в','п','р','л','д','ж','ч','с','м','т','б']
#     for i in str_.lower():
#         if i in gl:
#             a.append(i)   
#             # print(f'Количество гласных: {i.count(i)}')
#         elif i in sgl:
#             b.append(i)
#             # print(f'согласных: {i.count(i)}')
#         else:
#             c.append(i)
#             # print(f'остальных символов: {i.count(i)}')
#     return (f'Количество гласных: {len(a)}, согласных: {len(b)}, остальных символов: {len(c)}')    
# print(count_symbols('Мурат супер!'))




# task 9
# a = []

# def asdf(list_: list):
#     for i in range(0,11):
#         list_.append(i)
#     return list_

# print(asdf(a))



# task 10
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]

# def lower_7():
#     b = []
#     for i in a:
#         if i < 7:
#             b.append(i)
#     return b

# print(lower_7())




# a = [1,2,5,7,8]
# def lower_7():
#     b = []
#     for i in a:
#         if i < 7:
#             b.append(i)
#     return b
# print(lower_7())






# a = [6,8,3,7,20]

# ac = [1,2,5,7,8]
# def lower_7():
#     b = []
#     for i in a:
#         if i < 7:
#             b.append(i)
#     return b
# print(lower_7())


