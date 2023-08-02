'''Циклы'''
# повторяющийся блок кода

# for -> проходится по итерируемому объекту
# list -> [1, 2, 4]; str -> 'hello world'; set -> {'hello', 'test', 'makers' }; dict -> {1: 'a', 2: 'b'}; tuple -> (1, 4, 7, 8) 

# while -> работает пока условие верно

# while <логическое выражение>:
#     тело

'''Бесконечный цикл'''
# a = 0
# while True:
#     # a = a +1 
#     a += 1
#     print(f'hello {a}')

'''цикл, который никогда не заработает'''
# while False:
#     print('hello')


# a = 0
# while a < 10:
#     # a = a +1 
#     a += 1
#     print(f'hello {a}')

# a = 11
# while a > 0:
#     print(a)
#     a -= 1


# a = 0
# while a != 100:
#     a += 1
#     print(a)

# list_ = ' '
# print(bool(list_))

'''найти сумму цифер целого числа'''
# number = int(input('Enter number: '))
# 12345 -> 15
# 1 + 2 + 3 + 4 + 5 = 15

# sum_ = 0
# for i in str(number):
#     sum_ += int(i)

# print(sum_)

# sum_ = 0
# l = 0

# while l < len(str(number)):
#     # print(str(number)[l])
#     sum_ += int(str(number)[l])
#     l += 1
    

# print(sum_)

# '4134567432'
# '4' -> 4
# for i in 12345665432:
#     print(i)


'''бесконечный цикл for'''
# list_ = [1, 2]
# for i in list_:
#     list_.append(i)
#     print(i)

# string = 'hello'
# print(id(string))

# for i in string:
#     print(i)
#     string = string + 'hello' # меняется ссылка на объект
# print(id(string))



'''break, continue, pass, else'''

# break 
# a = 0 
# while a != 10:
#     a += 1
#     if a == 5:
#         break
#     print(a)


# for i in range(11):
#     if i == 4:
#         break
#     print(i)

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         print(str('this is 3'))
#         continue
#         print('h')
#     print(i)


# a =[ 1,2,3,4, 'hello',9, False]
# sum_ = 0
# for i in a:
#     if type(i) not in (int, float):
#         continue
#     sum_ += i
# print(sum_)
    
# if 4 == 00:
#     pass
# for i in range(1,11):
#     pass


"""
# num = int(input('enter number: '))
# max_number = 0
# while num > 0:
#     if num % 10 > max_number:
#         max_number = num % 10
#     num = num // 10
# print(max_number)
"""
    






