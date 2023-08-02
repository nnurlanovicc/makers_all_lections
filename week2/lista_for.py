








# list_ = [1,2,3,4,5,6,7,8,9,[True],'hello',{1, 'one'},(1,2,3,)]
# print(list_[0])

# nurs = list('i love you')
# print(nurs)

# nurs = list(range(12))
# print(nurs)

# range(start, end, step)

#===========================================================
# ========list.append(element) -> end list
# nurs = [1, 1, 1, 2, 3, "I", "love", "you", "Azi", ]
# nurs.append('Azi')
# print(nurs)


#========= list.extend([interable])
# nurs.extend('more')
# print(nurs)

#========= list.insert(index, element)
# nurs.insert(1, 'more')
# print(nurs)

#======== list.index(element, [start, end])
# print(nurs.index(1))

#======== print(dir(nurs))

# ========= list.clear()
# nurs.clear()
# print(nurs)

#==========list.count(element)
# print(nurs.count(1))

#==========list.pop([index])
# print(nurs.pop(0))
# print(nurs)

# ==========list.remove(element)
# print(nurs.remove(1))
# print(nurs)

# ==========list.reverse 
# nurs.reverse()
# print(nurs)

# ==========list.sort()
# nurs2 = [4,5,6,3,2,7,8,9]
# nurs2.sort()
# nurs2.sort(reverse=True)
# print(nurs2)
# nurs3 = ['a','i','n','a','z', 'i','k']
# nurs3.sort()
# print(nurs3)

# nurs4 = ['n','n','u','r','l','a','n','o','v','i','c','c', 1,2,3,]
# nurs4.sort()
# print(nurs4)

# ============list.copy()
# nurs5 = nurs4.copy()
# nurs4.pop()
# print(nurs5)

"""========================FOR==========================="""

# for i in nurs4:
    # print(i)


# for i in nurs2:
#     print(i ** 2)


# for i in range(11):
#     # print(i)
#     if i % 2:
#         print(i,'Четное')
#     else:
#         print(i,'Нечетное') 

# for i in range(1,5):
#     print('-')
#     print(i)
#     for b in range(2):
#         print(b)

# for i in range(1,5):
#     print('-')
#     print(i)
#     for b in range(i):
#         print(b)


# for i in list_:
#     print(i)
#     if type(i) != int:
#         list_.remove(i)
#     print(list_)


# list_ = [1, 'hello', 2, 3, 4, 5, 'test', 'world']
# list_index = []
# for i in list_:
#     # print(i)
#     if type(i) != int:
#         index_ = list_.index(i)
#         list_index.append(index_)

# print(list_index)
# print(list_)

# for i in list_index:
#     list_.remove(i)

# print(list_)



# list_ = [1, 'hello', 2, 3, 4, 5, 'test', 'world']

# for i in list_.copy():
#     if type(i) == str:
#         list_.remove(i)

# print(list_)


# list_index = []
# for i in list_:
#     if type(i) != int:
#         list_index.append(i)
# print(list_index)

# for i in list_index:
#     list_.remove(i)
# print(list_)

# guests = []
# list_lenght = int(input('enter number of guests: '))
# for i in range(list_lenght):
#     guest = input('enter guest name: ')
#     guests.append(guest)
# print(guests)
"""=========================TUPLE=========================="""
# Литералы -> (,)
# a = 1,2,3
# a = (8,)
# print(type(a))

# print(dir(tuple))

#============= tuple.count(element)

# ============ tuple.index(element)















