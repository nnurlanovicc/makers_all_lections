# try:
#     num = int(input('enter tne number: '))
#     num2 = int(input('enter tne number: '))
#     res = num / num2
# except ValueError:
#     print('this is not a number')
#     num = int(input('enter tne number: '))
#     num2 = int(input('enter tne number: ')) 
# except ZeroDivisionError:
#     print('number cannot be divided by zero')
# else:
#     print(f'{num}/{num2}={res}')
# finally:
#     print('idi na huy')

# try:
#     while True:
#         print('f')
# except KeyboardInterrupt:
#     print('ctrl + c')

# while True:
#     try:
#         num1 = int(input('enter the first number: '))
#         num2 = int(input('enter the second number: '))
#         res = int(num1 + num2) 
#     except ValueError:
#         print('this is not a number')
#         num1 = int(input('enter the number: '))
#         num2 = int(input('enter the second number: '))
#         res = int(num1 + num2) 

#     except ZeroDivisionError:
#         print('number cannot be divided by zero')
#         num1 = int(input('enter the number: '))
#         num2 = int(input('enter the second number: '))
#         res = int(num1 + num2) 
#     else:
#         print(f'{num1} + {num2} = {res}')
#     finally:
#           print('idi na huy')

"""===============  raise  ================"""


# try:
#     age = int(input('enter your age: '))
#     if age < 18:
#         raise ValueError('id na huy')
#     print('idi na huy cynok')
# except ValueError:
#     print('dalbayob pishi chislo: ')


# Aiana, [13 июня 2023 г., 12:18:54]:
'''
Ошибки -> проблемы с синтаксисом
1. SyntaxError: забыли двоеточие, скобку
2. IndentationError: неправильный отступ
3. TabError: неправильная табуляция
'''
# 2f = 8

# Исключения: (код написан правильно, но работает не так, как ожидалось)
# 1.  ArithmeticError 
#    ZeroDivisioError
# 2. ValueError 
# 3. NameError
# 4. TypeError
# 5. KeyError
# 6. IndexError
# 7. AttributeError
# 8. ImportError
# 9. BaseException (прородитель)

ZeroDivisionError # при делении на 0
# 8 / 0
# 4 // 0
# 3 % 0

ValueError # вызывается при распаковке, переводе одного типа данных в другой
# int('hello')
# a = 'asd'
# k, b = a

NameError # когда обращаемся к несуществующей переменной

# print(b)


TypeError # когда передаем в функцию, метод меньше или больше аргументов, чем требуется

# for i in 2345677:
#     print(i)
# [].append()
# [].append(1, 2, 3)
# '5' + 5

KeyError # при обращении к несуществующему ключу

# dict_ = {'a': 1}
# dict_['b']
# dict_.pop('b')

IndexError # при обращении к несуществующему индексу

# list_ = ['a', 'b', 'c']
# list_[4]
# list_.pop(3)


AttributeError # когда обращаемся к несуществцющему методу или атрибуту объекта

# a = 12341
# a.upper()
# b = [1, 2, 3]
# b.discard()

ImportError # неправильный импорт

# import math
# from math import pi2


# BaseException -> прородитель


'''===== try except ====='''
# чтобы код не прекращал свою работу

'''Синтаксис'''

# try:
#     тело try
#     # код, который может вызвать ошибку
# except:
#     тело except
#     # код, который сработает, если в try возникнет ошибка
# else:
#     тело else
#     # код, котрый отработает, если в блоке try не возникло ошибки
# finally:
#     тело finally
#     # код, который отработает в любом случае

# def division(num1, num2):
#     return num1/num2

# try:
#     num = int(input('Введите число: '))
#     num2 = int(input('Введите число: '))
#     res = num / num2
#     # res = division(num, num2)
# except (ValueError, ZeroDivisionError):
#     print('Вы ввели не число или на ноль делить нельзя')
    
#     num = int(input('Введите число: '))
#     num2 = int(input('Введите число: '))
#     res = num / num2
#     # res = division(num, num2)
#     print(res)

# # except ZeroDivisionError:
# #     print('На ноль делить нельзу')
# else:
#     print(f'{num} / {num2} = {res}')

# finally:
#     print('Пока')


# try:
#     while True:
#         print('f')
# except KeyboardInterrupt:
#     print('ctrl + c')

# dict_ = {key: key  2 for key in range(11)if key % 2 == 0}
# print(dict_)
# try:
#     dict_ = {key: key  2 for key in range(11)if key % 2 == 0}
#     # print(dict__)
#     value = dict_[100]
#     print(value)
# # except:
# #     pass
# except NameError:
#     print('Переменна dict__ не объявленна ')
# except KeyError:
#     print('такого ключа нет')
#     print(dict_)
#     key = int(input('Введите ключ: '))
#     print(dict_[key])

# from math import factorial as fact 
# fact()

# try:
#     i = int(input())
# except Exception as e:
#     print(e)

"""напишите программу, в которая будет принимать от пользователя два числа и складывать их"""

# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
# except ValueError:
#     # print('Вы ввели не число')
#     # num1 = 10
#     # num2 = 99
#     print(num1 + num2)
# else: 
#     print('ошибка не возникла')
# finally:
#     print(num1 + num2)

# count = 0
# while True:
    
#     try:
#         a = int(input('Введите число: '))
#         b = int(input('Введите число: '))
#         res = a + b
#     except ValueError:
#         a = int(input('Введите число: '))
#         b = int(input('Введите число: '))
#         res = a + b
    
#     count += 1
#     print(res, count)
#     if count == 3:
#         break


'''======   raise   ======'''
# Исскуственно вызывать ошибки
# try:
#     age = int(input('введите возраст: '))
#     if age < 18:
#         raise ValueError('Доступ закрыт')
#     print('чек')
# except ValueError:
#     print('вы ввели не число или вам нет 18')

# a = 1
# b = 2
# if a < b:
#     raise Exception('b должно быть меньше a')





# task 2
# b = 10
# c = 11
# try:
#     print(a)
# except NameError:
#     print('Такой переменной не существует!')

# task 3
# try:
#     num1 = int(input('jjn'))
#     num2 = int(input('k'))
#     res = num1 / num2 
# except (ValueError, ZeroDivisionError):
#     print('На ноль делить нельзя')
# else:
#     print(res)



# # task 5
# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try:
#     print(dict_['key3'])
# except KeyError:
#     print('Нет такого ключа!')


# # task 6
# list_ = [1, 4, 9, 16, 25, 36] 
# try:
#     print(list_[7])
# except:
#     print('Нет такого элемента!')

# # task 7
# try:
#     age = int(input(':'))
#     if age < 18:
#         raise ValueError('Доступ запрещён')
#     # elif age is float and age > 100:
#     #     print('Введён некорректный возраст')
#     # else:
#     #     print('Спасибо')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо') 
# finally:
#     print('До свидания!')



# task 8
# try:
#     num1 = int(input('jjn'))
#     num2 = int(input('k'))
#     res = num1 / num2 
# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка!')
# else:
#     print(res)


# # task 9

# cash = int(input(':'))
# if cash < 0:
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print(cash)
    

# # task 10
# list_ = [1, 2, 3]
# try:
#     list_.get(1)
# except AttributeError:
#     print(list_[0])

# task 11
# string = 'nurs'
# num = 23
# try:
#     print(string + num)
# except TypeError:
#     print('Unsupported option')




# task 12

# try: 
#     for x in range(10): 
#         list_.append(x)
# except NameError: print([0,1,2,3,4,5,6,7,8,9])



# task 13
# try:
#     list_ = [1, 2, 3, 4]
#     for i in range(0, len(list_) + 1):
#         print(list_[i])
# except IndexError:
#     pass



# task 14
# password = 'ainazik'
# if len(password) <6:
#     raise ValueError


# task 15

# warehouse = [
#         ['1', '2', '3'],
#         [1, 2],
#         [[1], [2], [3]],
#         [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
#     ]
# for i in warehouse: 
#     if len(warehouse)>10 or len(i)>3: 
#         raise ValueError()



# task 16
# def to_fahrenheit(k:int) -> float:
#     assert k >= 0 ,"Холоднее абсолютного нуля!"
#     result = (k - 273.15)* 9/5 + 32
#     return result


# print(to_fahrenheit(0))


# task 17
# try:
#     import lamabimgo 
# except ModuleNotFoundError:
#     print('Такого модуля нет')



# task 18
# def filter_comment(comment: str, banlist=[]) -> None:
#     for i in range(0,len(banlist)): 
#         if banlist[i] in comment.lower(): 
#             raise ValueError('Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст')


# print(filter_comment('Hello, world', ['hello']))



# task 19:










