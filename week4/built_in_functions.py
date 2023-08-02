"""
всроенные функции
"""









"""======================  lambda  ==========================="""

# lambda параметры: что функция возвращвет

# def add_nums(x,y):
#     return x + y
# print(add_nums(3,4))

# print((lambda x,y: x + y) (3,40))

# lambda_func = lambda x,y: x + y
# print(lambda_func(45,6))



# a = lambda a,b,c: (a,b,c)

# print(a(3,4,5))


# dict_ = {1: 'a', 2: 'b', 3: 'c'}

# dict_case = lambda x: x.keys()
# print(dict_case(dict_))


# ls = [1,2,3,4,5,6,7,8]
# print((lambda ls: ls[-1])(ls))


# num = lambda x: x ** 2
# print(num(8))

# str_ = lambda x: len(x)
# print(str_('nurs'))


"""============================ map ==========================="""

# map(func,iterable) -> она приминяет функцию для каждого элемента итерируемого обьекта

# list_ = ['1','2','3']
# print(map(int, list_))
# for i in map(int, list_):
#     print(type(i))

# print(list(map(int,list_)))




# nums = input('enter two number with space: ')
# a,b = map(int, nums.split())


# list_ = ['1','2','3']
# list_n = []
# for i in list_:
#     list_n.append(int(i))



# list_ = [1,2,3,4,5,56,45,]
# list_s = list(map(lambda x: x ** 2, list_))
# print(list_s)



# def square(a):
#     return a ** 2
# list_ = [1,2,3,4,5,56,45,]
# list_s = list(map(square, list_))
# print(list_s)



"""====================== filter ======================"""

# filter(func, iterable) -> фильтрует элэменты итерируемого объукта, основываясь на результат func -> true


# def filter_nums(number: int) -> bool:
#     if number % 2 ==0:
#         return True
#     return False
# list_ = [2,3,4,5,3,5,6,5,345,43,2,45,43,23,54,64,]
# result = list(filter(filter_nums, list_))
# print(result)



# list_ = [2,3,4,5,3,5,6,5,345,43,2,45,43,23,54,64,]
# lam_func = lambda x: x % 2 ==0
# result = list(filter(lam_func, list_))
# print(result)



# list_ = ["Тима", "Макс", "Эртай", "Алина", "Эркайым", "Алекс"]
# vowels = "АЕОУИЭЮЯ"
# def startswith_vowels(name):
#     # # vowels = "АЕОУИЭЮЯ"
#     # # print(tuple(vowels))
#     return name.upper().startswith(tuple(vowels))
# # # print(startswith_vowels('алекс'))



# result = list(filter(startswith_vowels, list_))
# print(result)



# res = list(filter(lambda name: name.upper().startswith(tuple(vowels)),list_))
# print(res)



"""========================= filter на цикле ========================="""
# list1 = []
# for name in list_:
#     if startswith_vowels(name):
#         list1.append(name)
# print(list1)









"""======================= reduce =============================="""

"""
reduce(func,iterable) -> нужно импортировать с functools -> возвращает какой то результат
заменили на sum, min, max
"""






# from functools import reduce


# list_ = [3,4,5,6,2,3,5,7]
# result = reduce(lambda x,y: x + y, list_)
# print(result)


# resul = list_[0]
# for y in list_[1:]:
#     resul = (lambda x,y: x * y)(resul, y) 
# print(resul)




"""================= enumerate ================"""
"""
enumerate(iterable,[start]) -> номерует элемменты последовательности (по дефолту с 0)
"""

# list_ = ['hello', 'nurs', 'azi', 'world', 'pythub']
# print(list(enumerate(list_)))


# for i in enumerate(list_):
#     print(i)

# for index,element in enumerate(list_):
#     print(f'index ->{index} | element ->{element}')






"""====================== zip ===================="""

"""
zip(iterable,iterable,[*iterables]) -> 
"""

# list_ = [1,2,3,4]
# list1 = [5,6,7,8,9,10]
# for i in zip(list_,list1):
#     print(i)





# dict1 = {1:2, 3:4, 5:6}
# def conver_to_str(value):
#     return str(value)

# res = list(map(conver_to_str,dict1.values()))
# print(res)
# new = dict(zip(dict1.keys(), res))
# print(new)


# list_ = [1,2,3,4]
# list1 = list(map(lambda x: 'чётное' if x % 2 == 0 else 'нечётное', list_))
# print(list1)

































































from functools import reduce











# task 1
# list_ = [1, 2, 3, 4]  
# result = reduce(lambda x,y: x + y,list_ )
# print(result)










# task 2
# list_ = [1, 5, -9, 6, -4] 
# new = all(i > 3 for i in list_)
# print(new)







# task 3
# list_ = [5, 8, 4, 6, 7]
# result = any(i < 0 for i in list_)
# print(result)








# task 4
# list_ = [1, 2, 3, 4]  
# result = list(map(lambda x: x ** 2,list_))
# print(result)









# task 5
# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x: x % 2 == 0,list_))
# print(result)












# task 6
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x: len(x) > 7,list_))
# print(result)











# task 7
# list_ = [5, 6, 7, 8] 
# result = reduce(lambda x, y: x * y, list_)
# print(result)












# task 8
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = list(filter(lambda x: x % 2 == 0,list_))
# list3 = list(filter(lambda x: x % 2, list_))
# result = f'even: {len(list2)}, odd: {len(list3)}'
# print(result)











# task 9
# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x: True if x > 0 else False,list_))
# print(result)












# task 10
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = reduce(lambda name,name2: name if len(name) > len(name2) else name2,list_)
# print(result)












# task 11

# result = list(map(lambda x: 'Fizz' if x % 3 == 0 else 'Buzz', range(1,5)))
# print(result)












# task 12
# list_ = [1,2,3,4,2,3,5,6,8,5,3,23,4,6,6,85,55,34,6,67,75,5,52,341,21,3345,47,]
# print(reduce(lambda x,y: x if x > y else y,list_))














# task 13
# list_ = [1,2,3,4,2,3,5,6,8,5,3,23,4,6,6,85,55,34,6,67,75,5,52,341,21,3345,47,]
# print(reduce(lambda x,y: x if x < y else y,list_))











# task 14
# string = 'hello'
# print(tuple(enumerate(string)))







# task15
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# result = list(map(lambda x: abs(x),list_))
# print(result)










# task 16
# list_ = ['hello', 123]
# res = list(map(lambda x: type(x),list_))
# print(res)












# task 17
# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# res = list(map(lambda x: x + ' Python' if len(x) > 5 else x + ' JavaScript',names))
# print(res)















# task 18
# list_ = ['123hello@gmail.com', '123', 'hello']
# res = list(map(lambda x: x if x.endswith('@gmail.com') else 'Not valid email',list_))
# print(res)










# task 19
# string = 'hello'
# print(tuple(enumerate(string,1)))













# task 20
# list1 = ['M', 'A', 'K', 'E', 'R', 'S'] 
# list2 = [236, 54, 33, 21, 89, 1]
# res = list(zip(list1,list2))
# print(res)











# task 21
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# list1 = list(filter(lambda x: x > 0,list_))
# list2 = list(filter(lambda x: x <= 0,list_))
# list3 = list(zip(list1,list2))
# print(list3)














# task 22
# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24]
# res = list(map(lambda x: round(x ** 2,3),list_))
# print(res)




# task 23
# list_ = ['a', 'n', 'n', 'a']
# res = list(map(lambda x: 'YES' if list_[::-1] == list_ else 'NO', list_))
# print(res[0])




































