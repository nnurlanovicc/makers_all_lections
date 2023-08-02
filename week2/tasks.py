# name_of_list = ['Helloworld!'] 
# if len(name_of_list) / 2 == 0:

# b = name_of_list
# new_list = b + a
# print(list(new_list))

# task of lists 3
# name_of_list = ['Helloworld!']
# new_list = name_of_list[0]
# i = len(new_list)
# if i%2==0:
#     new_list = name_of_list[0][i//2:] + name_of_list[0][:i//2]
# else: new_list = name_of_list[0][i//2+1:] + name_of_list[0][:i//2+1]
# print(list(new_list))
# print(type(i))
#========================================================================================


# task of lists 4
# list_ = ['world', 'hello']
# a = str(list_[1])
# b = str(list_[0])
# new_list = [a , b] 
# print(new_list)
#========================================================================================


# task of lists 5
# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# suitcase.pop()
# suitcase.insert(0, 'панама')
# print(suitcase)
#========================================================================================



# task of lists 6
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = []
# for i in nums:
#     if i < 5:
#        res.append(i)
# print(res)
#========================================================================================


# task of lists 7
# a = input()
# list_ = list(a.split(','))
# tuple_ = tuple(a.split(','))
# print(list_)
# print(tuple_)
#========================================================================================



# task of lists 8
# list_ = [1,2,3,4,5]
# new_list = []
# for i in list_:
#     new_list.append(str(i))
# print(new_list)
#========================================================================================


# task of lists 9
# list_ = [1,2,3,4,5]
# new_list = []
# for i in list_:
#     if i % 2 != 0:
#         new_list.append('нечетное')
#     else:
#         new_list.append('четное')

# print(new_list)
#========================================================================================


#lists 10
# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10] 
# list3 = list(list1) + list(list2)
# print(sum(list3))
#========================================================================================


# lists 13
# a = input()
# list_ = []
# for i in a.split(','):
#     list_.append(i)
# list_.sort()
# print(list_)
#========================================================================================


# list 14
# list_ = [1,1,3]
# if list_[0] == list_[1] or list_[0] == list_[2] or list_[1] == list_[2]:
#     print('yes')
# else:
#     print('ERROR')
 #========================================================================================
   

# list 15
# list_ = [] 
# for x in range(54, 9184): 
#      if x % 5 == 0: list_.append(x) 
#      print(list_)
#========================================================================================



# list 16
# list_ = [20, 10, 20, 1, 100] 
# min_number = list_[0] 
# for i in range(len(list_)): 
#      if list_[i] < min_number: 
#           min_number=list_[i] 
          
# print(min_number)
#========================================================================================


# list 17
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')] 
# cleared_tuples = [c for c in tuples if c] 
# print(cleared_tuples)
#========================================================================================


# list 18
# list_ = [] 
# name1 = input("Введите имя и фамилию: ") 
# name2 = input("Введите имя и фамилию: ") 
# name3 = input("Введите имя и фамилию: ") 
# name4 = input("Введите имя и фамилию: ") 
# name5 = input("Введите имя и фамилию: ") 
# list_.append(name1) 
# list_.append(name2) 
# list_.append(name3)
# list_.append(name4) 
# list_.append(name5) 
# target = " " 
# surnames = [] 
# for x in list_: 
#      t = x.find(target) 
#      v = x.rfind(target) 
#      if x.count(target) > 1: 
#           surnames.append(x[v+1:])
#      else: surnames.append(x[t+1:]) 
#      print(sorted(surnames))
#========================================================================================


# task 19
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
# number = 8 
# if list_ == number: 
#      print('Oshjeh') 
# else: 
#      print(list_.count(number))
#========================================================================================


# task 20
# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12] 
# count = 0 
# a = '' 
# for i in list_: 
#      if type (i) == int: 
#           count = i + count 
#      elif type(i) == str: 
#           a = i 
#           if a.isdigit(): 
#                count = count + int(i) 

# print(count)
#========================================================================================


# task 21
# str_list = ['abc', 'xyz', 'aba', '1221'] 
# index = [] 
# for x in str_list: 
#      if x[0] == x[-1]: 
#           index.append(str_list.index(x)) 
          
# print(index)
#========================================================================================


# task 22
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = []
# min_list = []
# for i in lists:
#     if len(i) < 2:
#        print(min_list.append(i))
#     elif len(i) > 2:
#        print(max_list.append(i))
        
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]] 
# lengths = [] 
# for i in lists: 
#      lengths.append(len(i)) 

# print(f'max_list {lists[max(lengths)+1]}') 
# print(f'min_list {lists[min(lengths)-1]}')

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_ = max([i for i in lists], key=len) 
# min_ = None 
# if len(lists) > 1: 
#      min_ = min([i for i in lists],key=len) 
#      if max_ == min_: 
#           min_ = None 
# print(f'max_list {max_}') 
# print(f'min_list {min_}')
#========================================================================================

# task 23
"""# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list_1 = []
# for i in list_:
    
# print(list_1)"""

# step = 3 
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'] 
# list1 = [list_[i::step] 
#          for i in range(len(list_))][:step] 
# print(list1)
#========================================================================================

# task 24
# size = 3 
# m = [] 
# m1 = [] 
# for i in range(1,size+1): 
#      m.append(i) 
#      m1.append(m) 
# print(m1)
#========================================================================================

# task 25
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# b = str(input('enter the word: '))
# v = []
# for i in list_:
#     if b == i[0]:
#         v.append(i)
# print(v)
#======================================================================================== 

# task 26
# colors1 = ["red", "orange", "green", "blue", "white"] 
# colors2 = ["black", "yellow", "green", "blue"] 
# res1=[] 
# res2=[] 
# for i in colors1: 
#      if not i in colors2: 
#           res1.append(i) 
# for k in colors2: 
#      if not k in colors1: 
#           res2.append(k) 
                    
                    
# print(res1,res2)
#========================================================================================  

# task 27
# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]

# for i in list1:
#     if i in list2:
#           print('True')
#     else:
#           print('False')
# for j in list2:
#      if j in list1:
#           print('True')
#      else:
#           print('False')

# list1 = [1,2,3,4,5] 
# list2 = [5,6,7,8,9] 
# res = None 
# for i in list1: 
#      for j in list2: 
#           if i==j: 
#                res = True
#           break 
#      else: res = False 
# print(res)

# list1 = [1,2,3,4,5] 
# list2 = [5,6,7,8,9] 
# if set(list1)&set(list2): 
#      print(True) 
# else: print(False)
#========================================================================================  

# task 28
# from collections import Counter

# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 3
# res = []
# for i in list_:
#     if Counter(i) >= repeats:
#         res.append(i)
# print(res)
        
# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8] 
# repeats = 3 
# res = [] 
# for i in list_: 
#      if list_.count(i) >= repeats and i not in res: 
#           res.append(i) 
# print(res)
#========================================================================================  

# task 29
# from itertools import permutations 
# list_ = [1, 2, 3] 
# comb = permutations(list_) 
# for i in comb: 
#      print(i)
#========================================================================================  

# task 30
# K=3 
# list1=[] 
# listhelp=[] 
# for i in range(K): 
#      listhelp.append(0) 
# for v in range(K): 
#           list1.append(listhelp) 
# print(list1)
#========================================================================================  


# task 31
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# res = []
# for i in colors:
#     res.append(i[::-1])
# print(sorted(res, key=len))
#========================================================================================  

# task 32
# list_ = [1,2,3,4,5,6,7,8,9,0] 
# step = 2
# element = "A" 
# for x in list_: 
#      if step < len(list_): 
#           list_.insert(step, element) 
#           step = step + 4 
# print(list_)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# step = 2
# element = 'A'
# def insert_element(list_, step, element):
#      result = []
#      for i in range(len(list_)):
#           result.append(list_[i])
#           if (i + 1) % step == 0:
#                result.append(element)
#      return result

# result = insert_element(list_, step, element)
# print(result)
#========================================================================================  

# task 33
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# res = []
# res2 = []
# for i in lists:
#     res.append(i[0]+i[1]+i[2])

# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

# max_list = max(lists, key=lambda x: sum(x))
# print(max_list)
#========================================================================================

# task 34
# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeated = []
# for i in list_:
#     if list_.count(i) > 1:
#           repeated.append(i)
# print(repeated)
#========================================================================================

# task 35
# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] 
# chars_list = [] 
# chars_new = [] 
# merge_from = input('Type letter for start: ') 
# merge_to = input('Type letter for end: ') 
# for i in chars: 
#      if chars.index(i) >= chars.index(merge_from) and chars.index(i) <= chars.index(merge_to): 
#           chars_list.append(i) 
#      else: chars_new.append(i) 
# str_ = ''.join(chars_list) 
# chars_new.insert(chars.index(merge_from), str_) 
# print(chars_new)









































# task dict 2
# a = {'x': 1, 'y': 2, 'z': 1}
# print(list(a.keys())[0])
#========================================================================================

# dict3
# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)
#========================================================================================

# dict 4
# a = {'a': 1, 'b': 2, 'c': 1}
# del a['a']
# del a['b']
# del a['c']
# print(a)
#========================================================================================


# a = {'a': 1, 'b': 2, 'c': 1}
# b = []
# for k,v in a.items():
#      b.append(k)
# print(b)
#========================================================================================

# dict 9
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = []
# for i in list(a.items()):
#     if type(i) == int:
#         if i % 2 == 0:
#             i = 2
#         else:
#             None
#     else:
#         None
#     b.append(i)
# print(b)
#========================================================================================
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for k, v in a.items():
#      if v%2==0:
#           b.setdefault(k, 2)
#      else:
#           b.setdefault(k,v)
# print(b)


# a = {'a': 1, 'b': 2, 'c': 3}
# for x,z in a.items():
#     print(x,z)
#========================================================================================

# dict 10
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k,v in list(a.items()):
#     if type(v) != str and type(v) != int:
#         del a[k]
# print(a)
#========================================================================================

# dict 11
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# c = {} 
# for k, v in a.items():
#      b = v / 5 
#      c.setdefault(k,b) 
# print(c)
#========================================================================================

# dict 12
# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in list(a.items()):
#     if v % 2 == 0:
#         del a[k]
# print(a)
#========================================================================================

# dict 13
# a = {'a': 1, 'b': 2, 'c': 3}
# b = {}
# for k,v in a.items():
#     b.setdefault(v,k) 
# print(b)
#========================================================================================

# dict 14
# a = {'a': 3, 'b': 2} 
# print(sum(a.values()))
#========================================================================================

# dict 15
# a1=dict(a=1, b=2, c=3) 
# a2=dict([('d', 4),('e', 5),('f', 6)]) 
# a3=dict([('a', 1)], b=2, c=3)
# print(a1, a2, a3)
#========================================================================================

# dict 16
# dict_ = {'x': 1, 'y': 2, 'z': 1}
# print(dict_.get('x'))
#========================================================================================

# dict 17
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# del dict_['a']
# print(dict_)
#========================================================================================

# dict 18
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# print(dict_.items())
#========================================================================================

# dict 19
# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(max(dict_.values()))
#========================================================================================

# dict 21
# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {}
# for k,v in dict1.items():
#      if v % 2 != 0:
#         dict2.setdefault(k, 1)
#      else:
#          dict2.setdefault(k,v)
# print(dict2)
#========================================================================================

# dict 22
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} 
# for k, v in list(dict_.items()): 
#      if v != None: 
#           dict_.pop(k) 
#           print(dict_)
#========================================================================================

# dict 24
# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {}
# for i in list_:
#     b = int(len(i))
#     dict_.setdefault(i,b)
# print(dict_)
#========================================================================================

# dict 25
# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5} 
# max_ = max(dict_.values()) 
# for k in dict_.keys(): 
#      if dict_[k] == max_: 
#           print(k)
#========================================================================================

# dict 26
# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {}
# for k,v in dict1.items():
#     dict2.setdefault(k, k ** 3):
#     print(dict2)

# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5} 
# dict2 = {k:v**3 for k,v in dict1.items()} 
# print(dict2)
#========================================================================================

# # dict 27
# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}  
# new_dict = {}
# for k, inner_dict in dict_.items():
#      for inner_key, v in inner_dict.items():
#           new_dict[k] = v
# print(new_dict)

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} 
# dict_ = {k:(v[v]) for k,v in dict_.items()}  
# print(dict_) 
# for k,v in list(dict_.items()): 
#      for v2 in v.values(): 
#           dict_[k] = v2 
# print(dict_)

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} 
# for k,v in list(dict_.items()): 
#      for v2 in v.values(): dict_[k] = v2 
# print(dict_)


# dict 28
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for key,value in dict1.items():
#     v = value.values()
#     nv = 1
#     for i in v:
#         nv *= i
#         dict2[key] = nv

#     # print(nv)
#     # dict2.update({key: nv})
    
# print(dict2)

  



# dict 29

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {}
# key = []
# value = []
# for i in list_:
#     if type(i) is str:
#         key.append(i)
#     if type(i) is int:
#         value.append(i)

# dict_ = dict(zip(key, value))
# print(dict_)
        


# dict 30
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_values = sorted(dict_.values()) 
# sorted_dict = {} 
# for i in sorted_values: 
#         for k in dict_.keys(): 
#                 if dict_[k] == i: 
#                         sorted_dict[k] = dict_[k] 
#                         break 
                
# print(sorted_dict)





# task 31

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} 
# sorted_values = sorted(dict_.values(), reverse = True) 
# sorted_dict = {} 
# for i in sorted_values: 
#         for k in dict_.keys(): 
#                 if dict_[k] == i: 
#                         sorted_dict[k] = dict_[k] 
#                         break 
# print(sorted_dict)


# task 32
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
# key = input() 
# if key in dict_: 
#         print("Key is present in the dictionary") 
# else: 
#         print("Key is not present in the dictionary")


# # task 33
# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4 = {}
# dict4.update(dict1)
# dict4.update(dict2)
# dict4.update(dict3)

# print(dict4)


# # task 34
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}
# for i in range(len (list1)): 
#         dict_[list1[i]] = list2[i] 
# print(dict_)


# # task 35
# dict_ = {'math': {'sum': sum},'vars': {'a': 5,'b': 20,'c': 50}}
# res = dict_.get('vars') 
# for k,v in dict_.items(): 
#         for j in v.values(): 
#                 if type(j) != int: 
#                         print(j(res.values()))





# # task 36
# d = {'a': 10, 'b': 9, 'c': 3} 

# result = d['a'] * d['b'] * d['c']  
# print(result)








# task 37
# string = "pythonist" 
# di = {}
# for i in list(string): 
#         di.setdefault(i, list(string).count(i)) 
# print(di)




















































# set 11
# a = {0,1,2} 
# b = {0,1,2,3,34,5,8,13} 
# if a.issubset(b): 
#      print ('Подмножество!')

# set 12
# a = {0,1,2,3,34,5,8,13} 
# b = {1,2,34} 
# if a.issuperset(b): 
#      print ('Надмножество!')

# # set 13
# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# if kail&robert and merri&robert:
#     print('kail merri')
# elif kail&robert and merri-robert:
#     print('kail')
# elif kail-robert and merri&robert:
#     print('merri')
# else:
#     print('no one')

# set 14
# tilek = {"Dodo","ImperiaPizza","FreshBox"}
# timur = {"OchakKebab","FreshBox"}
# alexander = {"FreshBox","KFC"}
# elina = {"Dodo","ImperiaPizza","FreshBox","OchakKebab","KFC"}
# restoran = tilek & timur & alexander & elina
# print(restoran)

# tilek = {'Dodo','ImperiaPizza','FreshBox'} 
# timur = {'OchakKebab','FreshBox'} 
# alexander = {'FreshBox', 'KFC'} 
# elina = {'Dodo','ImperiaPizza','FreshBox','OchakKebab','KFC'} 
# restoran = tilek.intersection(timur).intersection(alexander).intersection(elina) 
# print (restoran)

# task 15
# ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
# ingredients.add("помидор" )
# ingredients.discard("колбаса" )
# ingredients.remove("шпинат")
# ingredients.add("базилик")
# ingredients.discard("сыр чеддар" )
# ingredients.add("сыр моцарелла")
# print(ingredients)

# task 16
# a = [{},{},{}]
# inp1 = input()
# inp2 = int(input())
# if inp2 == 1 and inp2 < 4:
#      a[0] = {inp1}
#      a[1] = {'default value'}
#      a[2] = {'default value'} 
# elif inp2 == 2 and inp2 < 4:
#      a[0] = {'default value'}
#      a[1] = {inp1}
#      a[2] = {'default value'}  
# elif inp2 == 3 and inp2 < 4:
#      a[0] = {'default value'}  
#      a[1] = {'default value'}  
#      a[2] = {inp1}
# else:
#      a[0] = {'default value'}  
#      a[1] = {'default value'}   
#      a[2] = {'default value'}  
# print(a) 


# task 17
# set1 = {range(2,11,2)}
# set2 = {range(1,11,2)}

# if set1&set2:
#     print('Множества пересекаются!')
# else:
#     print('Множества не пересекаются!')

# set1 = {i*2 for i in range(5)} 
# set2 = {i*2+1 for i in range(5)} 
# if set1 & set2: 
#     print('Множества пересекаются!') 
# else: 
#     print('Множества не пересекаются!')















# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {k:v for k,v in my_dict.items }
# print(dict_)











