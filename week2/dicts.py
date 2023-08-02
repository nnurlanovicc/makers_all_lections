"""================== словари ======================"""
# 


# dict = {}
# print(type(dict))

# nurs = dict(a = 'azi', b = 1)
# print(nurs)

# nurs = dict((['o','v'],['key', 'value']))
# print(nurs)

# nurs = dict(['as','df','fg'])
# print(nurs)

# k, v = [1,2]
# print(k,v)

# k, v = 'ac'
# print(k,v)





# {[]: 1} -> TypeError: unhashable type: 'list'

# a = {1: 'nurs', 1: 'azi'}
# print(a) #{1: 1}

# nurs = {
#     'name': 'nurs',
#     'last':  None,
#     'mail': True,
#     'info': [1,2,3,4],
# }

# print(nurs)
# a,b,c = (1,2,3)
# print(a, '=>', b, '=>', c)


# nurs['mail'] = 'test@gmail.com'

"""===========mothods==========="""
# print(dir(dict))


#============== dict.items()

# print(nurs.items())

# for key, value in nurs.items():
#     print(key, '--->', value )

# for key, val in nurs.items():
#     print(key, val)


# nurs = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five' }

# new_nurs = {}
# for key, value in nurs.items():
#     new_nurs.update({value: key})

# print(new_nurs)



#============== dict.value()
# for i in nurs.values():
    # print(i)


#============== dict.keys
# for i in nurs.keys():
#     print(i)

#============== dict.clear
# nurs.clear()
# print(nurs)

#============= del
# del nurs
# print(nurs)


# a,b,c = (1,2,3)
# print(a, '=>', b, '=>', c)

#============= dict.copy
# nurscopy = nurs.copy()
# print(nurscopy)

#============ dict.fromkeys(seq, [default]) default = None
# list_ = [ 'name','hello', ' keys']
# dict_ = dict.fromkeys(list_, 1)
# print(dict_)


# dct = dict.fromkeys('as')
# print(dct)

#==================== dict.get(key, [default]) => no error
            # dict[key] => error


# nurs = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five' }
# print(nurs.get(6)) => None

# print(nurs[6]) => KeyError:

#======================= dict.update(new_dict)
# nurs.update({6: 'six', 7: 'seven', 8: 'eight'})
# print(nurs)
# azi = {9: 'nine', 10: 'ten'}
# nurs.update(azi)
# print(nurs)



#=============== dict.setdefault(key, [default_value]) 
        # like get
        # make new

# nurs = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five' }
# print(nurs.setdefault(1)) => one
# print(nurs.setdefault(11, 'eleven'))
# print(nurs) =>  

#==================dict.pop(kye, [message])
# nurs = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five' }
# nurs.pop(1)
# print(nurs)
# print(nurs.pop(7, 'no such key'))



#===============dict.popitem()

# nurs = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five' }
# print(nurs.popitem()) => (5, 'five')
# print(nurs) => {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


# nurs = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five' }

# new_nurs = {}
# for key, value in nurs.items():
#     new_nurs.update({value: key})

# print(new_nurs)


# try: 
#     for x in range(10): 
#         list_.append(x)
# except NameError: print([0,1,2,3,4,5,6,7,8,9])








"""2) Даны два списка одинаковой длины. 
Необходимо создать из них словарь таким образом, чтобы элементы первого списка были ключами, 
а элементы второго — соответственно значениями нашего словаря

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
dict_ = {}
"""

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}
# for i in range(len(list1)):
#     dict_[list1[i]] = list2[i]
# print(dict_)






