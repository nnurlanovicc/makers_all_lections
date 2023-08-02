"""======================  SET()  =============================="""




"==make a set=="
# set_a = set()
# print(type(set_a))

# set_b = {1,2,3, [1,2,3]}
# print(set_b) => TypeError: unhashable type: 'list'

# set_c = set({1: 'a', 2: 'b', 3: 'c'})
# print(set_c)

# set_d = set([1,2,3,4,5,3,2,4,1,3,4,5])
# print(set_d)

# set_e = set('nurssssssss')
# print(set_e)

# set_a = {1,2,3,(1,2,['hello'])}
# print(set_a) => TypeError: unhashable type: 'list'


"""============================ methods ============================="""
# print(dir(set))
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
#   '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__',
#     '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', 
#     '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', 
#     '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 
#     'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 
#     'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

#===== set.add(element)
# set_a = {1,2,3}
# set_a.add('hello')
# print(set_a)
# a = 4
# set_a.add(a)
# print(set_a)

# set_a = {1,2,3}
# for i in range(101):
#     set_a.add(i)
# print(set_a)

#========= set.update(seq)

# set_a = {1,2,3,4,5,6,7, 'world', 'hello', 'test'}
# set_a.update(['makers'])
# print(set_a)
# set_a.update('nurs')
# print(set_a)

#========= set.clear()
# set_a = {1,2,3,4,5,6,7, 'world', 'hello', 'test'}
# set_a.clear()
# print(set_a)

#========= set.pop()

# set_a = {1,2,3,4,5,6,7, 'world', 'hello', 'test'}
# print(set_a.pop())
# print(set_a)

# set_b = {'nurs', 'azi', 'love', 'i'}
# print(set_b.pop())
# print(set_b)

# set_c = {'world', 'hello', 3, 4, 'test'}
# print(set_c)
# print(set_c.pop())
# print(set_c)
# print(set_c.pop())
# print(set_c)
# print(set_c.pop())
# print(set_c)

#========== set.difference(other_set)
# set_a = {1,2,3,4,5, 'nurs', 'azi', 'love'}
# set_b = {4,5,6,7,8, ' azi', 'love'}
# print(set_a.difference(set_b))
# print(set_b.difference(set_a))
# print(set_b-set_a)
# print(set_a-set_b)

#=========== set.symmetric_difference(other_set)
# set_a = {1,2,3,4,5, 'nurs', 'azi', }
# set_b = {4,5,6,7,8, ' azi', 'love'}
# print(set_a.symmetric_difference(set_b))
# print(set_b^set_a)

#=============== set.intersection(other_set)
# set_a = {1,2,3,4,5, 'nurs', 'azi', }
# set_b = {4,5,6,7,8, ' azi', 'love'}
# print(set_a.intersection(set_b))
# print(set_a & set_b)

#============== set.union(other_set)
# set_a = {1,2,3,4,5, 'nurs', 'azi', }
# set_b = {4,5,6,7,8, ' azi', 'love'}
# print(set_a.union(set_b))
# print(set_a | set_b)

# set_a = {1,2,3,4,5, 'nurs', 'azi', }
# set_b = {4,5,6,7,8, ' azi', 'love'}
# list_ = [8,9,0, 't']
# print(set_a.union(list_))

"""
set.difference_update()
set.intersection_update()
set.symmetric_difference_update()
set.isdisjoint()
set.issupperset()
set.issubset()
"""
#========================================================
# num = int(input(':'))
# summ_ = 0
# for i in str(num):
#     summ_ += int(i)
# print(summ_)
#========================================================
# sum_ = 0
# l = 0
# while l < len(str(num)):
#     # print(str(num)[l])
#     sum_ += int(str(num)[l])
#     l += 1
# print(sum_)
#========================================================
# num = [1,2,3]
# num2 = 1
# for i in num:
#     # print(i)
#     num.append(num2)

#     print(i)
#========================================================










