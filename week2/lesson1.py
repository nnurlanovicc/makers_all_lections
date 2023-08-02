# print(type(4>3))

# print('makers' > 'bootcamp')

# ord()

# print(ord('b'))

# # chr()
# print(chr(98))

# a = True
# b = False
# print(int(a))
# print(int(b))


# print(bool(3.5))
# print(bool(-200))
# print(bool(0))
# print(bool(' '))
# print(bool(""))

# ====False: 0, '', "", {}, [], set(), frozenset(), None, False========
 

# ===========================


# >  <  >=  =<  ==  1= 

# a = 10
# b = 7
# print(a + b > 15)      => True
# print(a < 20 -b)       => True
# print(a <= b + 3)      => True
# print(a != b)          => True 
# print(a == b)          => False

# c = a == b             => False 
# print(c)
# print(int(c))          => 0
# print(str(c))          => False

#=============================
        #and , or

# a = 15
# b = 25
# print(a >= 15 and b < 30)  => True
# print(a > 15 and b < 30)   => False

# print(a == 15 or b > 30)   => True
# print(a == 15 or b > 30)   => True
# print(a != 15 or b >30)    => False

#=============================

# not 

# x = 20
# print(not x > 10)          => False
# print(not x == 10)         => True

#=============================

# a = True 
# b = False 
# print(not a)               => False
# print(not b)               => True

#=============================

# if, elif, else
"""
if condition is True:
    some code 1
elif some condition is True:
    some code 3
else:
    some cod 2
"""


# a = 20 
# if a > 20:
#     print('a is greater than 20')          => no
# if a >= 20:
#     print('a equalse or greater than 20')  => ok


# a = 20
# if a > 20:
#     print('a is greater than 20')     => no
# elif a == 20:
#     print('a is equals 20')           => ok
# else:
#     print('a is less than 20')        => no

#===============================================================


# a = input('Enter the number: ')
# if int(a) > 20:
#     print('a is greater than 20')
#     if int(a) > 30:
#         print('a is greater than 30')
#         if int(a) > 40:
#             print('a is greater than 40')
#         else:
#             print('a is less than 40')
#     else:
#         print('a is less than 30')
# else:
#     print('a is less than 20')


#===============================================================


# a = input('Enter the number: ')
# if int(a) > 20:
#     print('a is greater than 20')
# elif int(a) > 30:
#     print('a is greater than 30')
# elif int(a) > 40:
#      print('a is greater than 40')
# else:
#     print('a is less than 20')


#==============================================================

# a = 10
# b = 5
# c = 20

# if a > b and b > c:
#     print('NURS')        => no
# else:
#     print('nurs')        => ok

#====================================
# a = 1
# b = 2
# c = 3

# if not (a < b and b > c):
#     print('NURS')        => ok
# else:
#     print('nurs')        => no

#===================================

# list_ = [11, 56, 98, 34]

# if not 20 in list_ and 11 in list_:
#     print('yes')
# else:
#     print('not')

#====================================

# Тернарный оператор 

"""
expression_true if condition else expression_false

"""

# a = True
# print(a if True else False)


# a = 'MAKERS'
# b = 10 
# print(a if b > 0 else 'makers')


"""
(expression_false, expression_true)[condition]
"""
# a = 10
# print(("negative","positive")[a >= 0])
# print(("negative","positive")[a == 0])

#===========================================

# NoneType

# print(type(None))

# null_variable = None
# not_nul_variable = 'NURS'

# if null_variable is None:
#     print('This is None')
# else:
#     print('This is not None')


# print(id(null_variable))
# print(id(None))

# if not null_variable is None:
#     print('This is None')
# else:
#     print('This is not None')


# if null_variable:
#     print('This is None')
# else:
#     print('This is not None')


# if not null_variable:
#     print('This is None')
# else:
#     print('This is not None')






"""Операторы идентификации """
   # 1. in => проверяет наличие элемента 
   # 2. сравнения
       # == -> по значению
       # is -> по ячейки памяти  
   # 3. is not -> отрицательное сравнение ячеек памяти 


# if 'u' in 'nurs':
#     print('yessssss')





#===================================================

# a = int(input("Enter the number: "))
# if a > 0 or a < 0:
#     print('Ok')
# else:
#     print('this is 0')

#==================================================

# number = int(input('Enter the number: '))
# if number > 0:
#     print(f'{number} is positive')
# elif number < 0:
#     print(f'{number} is negative')
# else:
#     print(f'{number} is zero')

#==================================================

"""Тернарные операторы"""
# условие в одну строку if elif else


# num = 4 
# result = 'Hello ' if num == 4 else 'World'
# print(result)

#===================================================


"""Моржовые операторы """
# Позволяет нам как и присваивать значение, так и возвращать его в одном выражении 
# print(hello :='Hello')
# print(hello = 'hello') TypeError: 'hello' is an invalid keyword argument for print()

#===================================================

# number = int(input('enter the number: '))
# if number %2 == 0:
#     print(f'{number} is even number')
# else:
#     print(f'{number} is odd number')

# a = 'even number' if number % 2 == 0 else 'odd number'

# a = 'odd number' if number % 2 else 'even number'

#===================================================

"""=================FizzBuzz=============="""

# number = int(input('Enter the number: '))
# if number % 15 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print(number)

#===================================================


# print('Your number is:', num := int(input("Enter your number: ")),'\n' + ('FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num))


#===================================================


# task 1

# password = input('enter your password: ')

# if password.isdigit() and len(password) >= 8:
#     print('your password save')

# if not password.isdigit():
#     print('Ваш пароль должен хранить только числа')

# if not len(password) >= 8:
#     print('Ваш пароль должен содержать не менее 8 символов')


# task 2


# point = input('sfgda: ').split(', ')
# math = int(point[0])
# inglish = int(point[1])
# litr = int(point[-1])

# average = (math + inglish + litr) /3
# if average > 69:
#     print(f'dvsdfv {average}')
# else:
#     print('sddsf')


# task 3

# import random

# play = ['kamen', 'nojnitsy', 'bumaga']
# my = input('your: ')
# com = random.choice(play)

# if my == 'nojnitsy' and com == 'bumaga':
#     print('you win')
# elif my == 'nojnitsy' and com =='kamen':
#     print('you lose')
# elif my == 

# print(my)
# print(com)

# task 22
# n = int(input('enter the number below 100: '))
# if n > 100:
#     print('incorrect number')
# elif (n > 10 and n < 20) or (n % 10 >= 5) or (n % 10 == 0):
#     print(f'На лугу пасется {n} коров')
# elif n % 10 == 1:
#     print(f'На лугу пасется {n} корова')
# elif n % 10 in range(2, 5):
#     print(f'На лугу пасется {n} коровы')




# TASK 24
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 and y1 != y2:
#     print('YES')
# elif y1 == y2 and x1 != x2:
#     print('YES')
# else:
#     print('NO')


# TASK 25
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1-x2) == abs(y1-y2):
#     print('YES')
# else:
#     print('NO')










