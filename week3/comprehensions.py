# sintaxis
# result for element in itereble object 
# result for element in itereble object if filter



"""============================list comprehension=========================================="""

# list_ = [i for i in 'hello']
# print(list_)


# list_1 = list((i for i in 'hello'))
# print(list_1)



# import time
# import datetime
# start_time = time.time()

# list1 = []
# for i in range(1,1000001):
#     list1.append(i)
# print(time.time() - start_time)

# start_time = time.time()
# list_num = [number for number in range(1,1000001)]
# print(time.time() - start_time)



# list_ = [i for i in range(1,11) if i % 2 == 0]
# print(list_)


# print(['hello' for i in range(10)])


# print([input() for i in range(10)])



# sintaxis

# [element if uslovie else element2 for i in itereble object ]

# a = ['chetnoe' if i % 2 == 0 else 'nechetnoe' for i in range(1,11)]
# print(a)

# a = [
#     'chetnoe'
#     if i % 2 == 0 
#     else 'nechetnoe'
#     for i in range(1,11)
#     ]
# print(a)

"""         ============== set comprehension ================       """

# list_ = [1,2,3,45,6,5,4,3,3,45,6,54,3,'nurs', 'azi', 'hello','makers']
# set_1 = {i for i in list_}
# print(set_1)


# list_ = [1,2,3,45,6,5,4,3,3,45,6,54,3,'nurs', 'azi', 'hello','makers']
# set_1 = {i for i in list_ if type(i) == str}
# print(set_1)


# list_ = [1,2,3,45,6,5,4,3,3,45,6,54,3,'nurs', 'azi', 'hello','makers']
# set_1 = {i + 'best' for i in list_ if type(i) == str}
# print(set_1)



# list_ = [1,2,3,45,6,5,4,3,3,45,6,54,3,'nurs', 'azi', 'hello','makers']
# set_1 = {i + 'best' if type(i) == str else i + 1 for i in list_ }
# print(set_1)


"""               =============== dict comprehension ================               """
# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# dict_1 = {}
# for k,v in dict_.items():
#     dict_1.update({v: k})
# print(dict_1)

# dict_1 = {v: k for k,v in dict_.items()}
# print(dict_1)

# dict_ = {}
# for i in range(1,11):
#     dict_.update({i: i ** 2})
# print(dict_)

# dict1 = {i:i ** 2 for i in range(1,11)}
# # print(dict1)



# list_ = [1,2,3,2,3,4,5,7,8,9,4,5,7]
# dict_1 = {i: list_.count(i) for i in list_}
# print(dict_1)


# dict_ = {'a': 1, 'b': 2, 'c': 3,'d': 4}


# dict_abc = {k: ('chetnoe' if v % 2 == 0 else 'nechetnoe') for k,v in dict_.items()}
# print(dict_abc)


# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# dict1 = {
#     list1[index]: list2[index] for index in range(len(list1))
#     }
# print(dict1)

# dict1 = {
#     list1[index]: ''.join(list2)
#     for index in range(len(list1))
#     }
# print(dict1)

# dict1 = {
#     list1[index]: '+'.join(list2)
#     for index in range(len(list1))
#     }
# print(dict1)


"""                          ================ vlojennoe comprehensions ====================                         """

# dct = {
#     i:
#     [j for j in range(i + 1)] 
#     for i in range(1,6)
#     }
# print(dct)

# list1 = [
#     ['hello world' for i in range(2)] 
#     for i in range(3)
#     ]
# print(list1)


# employees = {
#     'id1': {
#         'first name': 'Александр',
#         'last name' : 'Иванов',
#         'age': 30,
#         'job':'программист'
#             },
#     'id2': {
#         'first name': 'Ольга',
#         'last name' : 'Петрова',
#         'age': 35,
#         'job':'ML-engineer'
#             }
# }

# dct = {key: value for key, value in employees.items()}
# print(dct)


# dct = {
#     key: {k:v for k,v in value.items()} 
#     for key, value in 
#     employees.items()
#     }
# print(dct)



# dct = {
#     key: {k: float(v) 
#     if k == 'age' else v 
#     for k,v in value.items()
#     } 
#     for key, value in 
#     employees.items()
#     }
# print(dct)

# for info in employees.values():
#     for k ,v in info.items():
#         if k == 'age':
#             info[k] = float(v)


# print(employees)



# list_ = [bool(i) if i % 2 == 0 else bool(0) for i in range(1,11) ]
# print(list_)



# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ['shorter' if len(i) <= 4 else 'longer' for i in list_name]
# print(new_list)


# dict_ = {i: i * i for i in range(1,11)}
# print(dict_)

















#task 10
# n = int(input('enter the number from 1 to 10: '))
# dict_ = {k: k * k  for k in range(1,501) if k % n == 0 }

# print(dict_)


#task 11
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3} 
# dict_ = {k:list(range(v+1))[1:] for k,v in a.items()} 
# print(dict_)

# task 12
# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k:'even' if v % 2 == 0 else 'odd' for k,v in dict_.items()}
# print(a)


# task 13
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending' 
# list1 = list(string_.split()) 
# print(list1)
# list_ = [i for i in list1 if i.isdigit()] 
# print(list_)


# task 14
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 'Nik': {'history': 84, 'math': 85, 'literature': 87}} 
# new_dict={x:max(y,key=lambda x:y.get(x)) for x,y in dict_.items()} 
# print(new_dict)

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 'Nik': {'history': 84, 'math': 85, 'literature': 87}} 
# new_dict = {k:i for k,v in dict_.items() for i,j in v.items() if j == max(v.values()) } 
# print(new_dict)


# # task 15
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k:i for k,v in my_dict.items() for j,i in v.items() }
# print(dict_)


# task 16
# list_ = [i for i in range(1,26) if i % 2 == 0]
# print(list_)

# task 17
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# in_list = [i if i >= 0 else 1 for i in list_  ]
# print(in_list)


# task 18
# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = [i for i in list1 if type(i) is str]
# print(list2)

# task 8
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ['shorter' if len(i) <= 4 else 'longer' for i in list_name]
# print(new_list)

# # task 19
# list_ = [0, 3, 9, 7, 5, 2, 18, 4]
# list1 = [i for i in list_ if i > 5 ]
# print(list1)

# # task 20
# list_ = [False, True, False, True, False, True, False, True, False, True] 
# list1 = [1 if i == True else 0 for i in list_]
# print(list1)

# # task 21
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = [len(i) for i in list_name]
# print(new_list)

# # task 22
# a = [i for i in range(1,1001,125) if i % 2 == 0 ]
# print(a)

# task 23
# list1 = [44,54,64,74,104]
# list2 = [i + 6 for i in list1]
# print(list2)

# # task 24
# list1 = [2, 4, 6, 8, 10, 12, 14]
# list2 = [i for i in list1 if i ** 2 > 50]
# print(list2)

# task 25
# string = "happy birthday!"
# list_ = [i for i in string if i.isalpha()]
# print(list_)

# # task 26
# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list_1 = {}
# ls = []
# for k,v in dict_.items():
#     list_1.update(v)

# for k2,v2 in list_1.items():
#     ls.append(v2)
# print(ls)


# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}} 
# list1 = [v2 for k1,v1 in dict_.items() for k2,v2 in v1.items()] 
# print(list1)





# task 27
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# dict_ = {i: len(i)**2 for i in list_name if len(i) > 4 }
# print(dict_)


# task 28
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, 
#         "Miivan": 1600, "Vann": 2400, "Semi": 13600, 
#         "Bicycle": 7, "Motorcycle": 110}

# list1 = [k.upper() for k,v in dict_.items() if v > 200 and v < 5000]
# print(list1)


# task 29

# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, 
#         "Miivan": 1600, "Vann": 2400, "Semi": 13600, 
#         "Bicycle": 7, "Motorcycle": 110}

# dict2 = {k.replace('i',''):k.count('i') for k,v in dict1.items()}
# print(dict2)



# task 30
# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = [i for i in list1 if bool(i) != False]
# print(list2)


# task 31
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# readers = [i[0] for i in SPL_Patrons if i[1] > 100]
# print(readers)


# task 32
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

# saved_amount = [round(i[-1] * 11.95,2) for i in SPL_Patrons]
# print(saved_amount)




# task 33
# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]

# list1 = [ [i[0] ,i[1] * 42]  for i in prairie_pirates  if i[-1] == True ]
# print(list1)


# task 34
# dkt = {}
# dict_ = {
#     'Sasha': {'likes': 23,'comments': 2,'rating': 4},
#     'Aliya': {'likes': 34,'comments': 5,'rating': 5},
#     'Dasha': {'likes': 15,'comments': 3,'rating': 2},
#     'Luna': {'likes': 12,'comments': 2,'rating': 1},
#     'Rena': {'likes': 26,'comments': 7,'rating': 2}
# }

# list1 = [i['likes'] for i in dict_.values() if i['rating'] > 3]
# print(sum(list1))



# task 35
# dict_ = {
#     'Dasha': {'likes': 15,'comments': [
#                                         {'id': 1, 'text': 'some text'},
#                                         {'id': 2, 'text': 'some text'},
#                                                                         ],
#                                             'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# pizdets=[i['id'] for key,value in dict_.items() for i in value['comments'] if len(dict_[key]['comments'])>3] 
# print(pizdets)












