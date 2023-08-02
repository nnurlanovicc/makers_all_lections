# string1 = "Makers"
# string2 = 'Bootcamp'
# print(string1,string2)


# string3 = 'Makers's Bootcamp'
# print(string3)


# string = "Makers's Bootcamp"
# print(string)

# sentence = " Jhon said: 'I can code' "
# print(sentence)


# nurs = 'hello\vnurs\vkak\vty'
# print(nurs)


# url = r'https://kaktus/\news\topics\read'
# print(url)

# languages = 'language:\n\t '
# description = 'Python : backend language\n\t  JavaScript: frontend language'
# print(languages, description)


# loop = 'for i in range(5):\n\t print(i)'
# print(loop)


# sentence = 'hello\v nurs\v and\v azi'
# print(sentence)
# # len()
# string = 'nursultan ainazik'
# print(len(string))


# nurs = 'Strings are ordered'
# print(nurs[0])
# print(nurs[1])
# print(nurs[-1])
# print(nurs[5])
"""
[x:y]
# """
# cvb = 'nursultan'
# #print(cvb[:4])
# bnm = cvb[:4]
# print(bnm)
# print(cvb[6:])
# print(cvb[4:])
# print(cvb[3:])
# asd = 'ainazik'
# print(asd[::-1])

# word = 'dream'
# word[0] = 'c'
# word = 'c' + word[1:]
# print(word)

# # find(string)
# nurs = 'nursultan_sultan_sul_tan'
# print(nurs.rfind('sultan'))

# index(string)

# print(nurs.rindex('sul'))

# replace(pattern, replace_pattern)
# print(nurs.replace('tan', 'san', 1))

# split(symbol) -> list
# print(nurs.split('_'))

# nurs = input('name: ').split('a')
# print(nurs)

# startswith(), endswith

# nur = 'I love Azi'
# print(nur.startswith('I'))
# print(nur.endswith('i'))


# # join(list)
# list_ = ['n', 'u', 'r', 's']
# print(','.join(list_))

# # capitalize()
# nurs = 'nursultan'
# print(nurs.capitalize())

# # count()
# nurs = 'nursultan sultan'
# print(nurs.count('tan'))

# lstrip() rstrip() strip()
# password = '    fut99bol'
# print(len(password))
# print(len(password.lstrip()))

# # partition(patter)
# nur = 'nurs azi is lovers'
# print(nur.partition('is'))

# swapecase
# zxc = 'Nurs Azi'
# print(zxc.swapcase())

# # zfill(width)
# zxc = 'nursultan'
# print(zxc.zfill(28))




# ljust(width, fillchar) rjust(width, fillchar)
# zxc = 'nursultan'
# print(zxc.ljust(34, '*'))

# # 1. % 
# name = input()
# last_name = input()
# age = int(input())
# some_variable = "Wellcome, %s %s,age %d" % (name, last_name, age)
# print(some_variable)


# zxc = input('enter your name: ')
# vbn = input('enter your last name: ')
# asd = input('enter your age: ')
# res = f'Hello,{zxc} {vbn} \nyour age is {asd}'
# print(res)


# task8
# x = int(input('x: '))
# y = int(input('y: '))
# res1 = x // y
# res2 = x % y
# if res2 == 0:
#     print('x делится на y')
#     print(f'Частное: {res1}')
# else:
#     print('x не делится на y')
#     print(f'Частное: {res1}')
#     print(f'Остаток: {res2}')

# # task 9
# year = int(input('year:'))
# if year % 4 == 0 and year % 100 != 0:
#     print('YES')
# else:
#     print('NO')

#==============================================================
# task21
# a = int(input('first: '))
# b = int(input('second: '))
# c = int(input('third: '))
# if a + b > c and a + c > b and b + c > a:
#     if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#         print('rectangular')
#     elif (a==b,a!=c) or (a!=b,b!=c,a!=c) or (a==b,b==c,a==c):
#         print('acute')
#     elif a**2>b**2+c**2 or b**2>a**2+c**2 or c**2>a**2+b**2:
#         print('obtuse')
#     else:
#         print('impossible')

#============================================================

# a = int(input())
# b = int(input())
# c = int(input())
# if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#     print('rectangular')
# elif (a==b,a!=c) or (a!=b,b!=c,a!=c) or (a==b,b==c,a==c):
#     print('acute')
# elif a**2>b**2+c**2 or b**2>a**2+c**2 or c**2>a**2+b**2:
#     print('obtuse')
# else:
#     print('impossible')

#============================================================


# a = float(input("Введите длину стороны a: "))
# b = float(input("Введите длину стороны b: "))
# c = float(input("Введите длину стороны c: "))

# if a + b > c and a + c > b and b + c > a:
#     # Неравенство треугольника выполняется
#     if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         print("rectangular")  # Прямоугольный треугольник
#     elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
#         print("obtuse")  # Тупоугольный треугольник
#     else:
#         print("acute")  # Остроугольный треугольник
# else:
#     print("impossible")  






