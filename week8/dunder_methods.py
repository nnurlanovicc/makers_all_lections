"""Магические методы в Python (dunder -> double underscore)"""

# Супер методы
# Служебные методы

# Методы, у которых 2 нижних подчеркивания в начале и в конце. 
# Мы их не вызываем напрямую, вызываются определенными операторами и функциями


# str, init

# __new__ -> Конструктор класса, отвечает за создание объекта
# __init__ -> инициализатор, задает созданному объекту атрибуты
# __del__ -> деструктор отвечает за удаление объекта (срабатывает когда мы заканчиваем работу с объектом)



# class Point:

#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         print('init')

#     def __del__(self):
#         print('удаление экземпляра' + str(self))


# a = Point(2,6)
# b = Point(3,6)
# print(a,b)



# class Point:

#     def __new__(cls,*args,**kwargs):
#         print('вызов метода __new__ для класса ' + str(cls))
#         return super().__new__(cls)

#     def __init__(self,x,y):
#         self.x = x
#         self.y = y


# a =Point(5,6)
# print(a)




# class Word(str):

#     def __new__(cls,*args):
#         string = args[0].replace(' ','')
#         return str.__new__(cls,string)
    
# word1 = Word('dsgarega reg rg js5ry ')
# print(word1)






# class User:
#     def __new__(cls, name, age):
#         if age > 18:
#             return super().__new__(cls)
#         raise Exception('Вы слишком молоды')
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __del__(self):
#         print('bye')

#     # def __str__(self):
#     #     return self.name
    
#     def __repr__(self):
#         return self.name

# user1 = User('nurs',23)
# print(user1)

# import datetime

# print(repr(datetime.date.today()))
# print(datetime.date.today())


# c = repr(datetime.date.today())
# print(eval(c))



'''
__str__ -> для удобного чтения 
__repr__ -> ссылку на объект в памяти

если не определен __str__ то str() использует __repr__
'''




# class MyNumber(int):

#     def __init__(self,value):
#         self.value = value

#     def __add__(self,other: int):
#         return f"это сложение и результат равен: {self.value + other}"
    
#     def __sub__(self, other: int):
#         return f"это выяитание и результат равен: {self.value - other}"
    
#     def __mul__(self,other: int):
#         return f"это умножение и результат равен: {self.value * other}"
    
#     def __truediv__(self,other: int):
#         return f"это деление и результат равен: {self.value / other}"
    
#     def __floordiv__(self,other: int):
#         return f"это целочисленное деление и результат равен: {self.value // other}"

#     def __mod__(self,other: int):
#         return f"это остаток от деления и результат равен: {self.value % other}"

#     def __pow__(self,other: int):
#         return f"это возведение в степень и результат равен: {self.value ** other}"


# obj_int = MyNumber(7)
# print(obj_int + 8)
# print(obj_int - 6)
# print(obj_int * 2)
# print(obj_int / 7)
# print(obj_int // 2)
# print(obj_int % 3)
# print(obj_int ** 2)



'''
==    __eq__(self,other) (equal)
!=    __ne__(self,other) (not equal)
>     __qt__(self,other) (greater than)
<     __lt__(self,other) (less than)
>=    __ge__...          
<=    __le__...


__invert__(self)             -> переварачивает итерируемый объект (~)
__hash__(self)               -> хеширует данные
__getattribute__(self, item) -> автоматически вызывается при считывании атрибута через экземпляр класса (получение свойства объекта) 
__getattr__                  -> вызывается автоматически каждый раз когда идет обращение к несуществующему атрибуту объекта 
__setattr__                  -> вызывается автоматически когда идет присвоение какому-нибудь атрибуту определенного значения
__delattr__                  -> вызывается когда удаляется атрибут из экземпляра 
__getitem__                  -> когда мы обращаемся в квадратных скобках (по индексу, по ключу, делаем срезы)
__setitem__                  -> когда создаем пару ключ и значение или изменяем
__delitem__                  -> когда удаляем
'''

# class Base:

#     def __init__(self, string: str):
#         self.string = string

#     def __invert__(self):
#         print('__invert__')
#         return self.string[::-1]
    
#     def __str__(self):
#         return self.string
    
# inv = Base('nursultan')
# print(~inv)




# string = 'hello'
# print(string.lower)
# print(string.__getattribute__('lower'))





# from typing import Any


# class Point:

#     def __init__(self,v,b):
#         self.v = v
#         self.b = b

#     def __getattribute__(self, item: str):
#         print('getattribute')
#         # return super().__getattribute__(item)
        
#         if item == 'v':
#             raise ValueError('доступ запрещен')
#         return super().__getattribute__(item)
    
#     def __setattr__(self,item: str, value):
#         print('setattr')
#         # super().__setattr__(item,value)
        
#         if item == 'z':
#             raise AttributeError('не допустимая имя аттрибута')
#         super().__setattr__(item,value)

#     def __getattr__(self,item):
#         print('getattr')

#     def __delattr__(self, item: str):
#         print('delattr')
#         super().__delattr__(item)

# a = Point(3,4)
# # a.v
# # a.b
# # a.z = 4
# del a.v
# print(a.__dict__)




# string = 'hello'
# print(string[0])
# print(string.__getitem__(0))




# class A:
#     def __getitem__(self,index):
#         print('getitem')
#         print(index)

#     def __setitem__(self,index,value):
#         print('setitem')
#         print(index)
        

#     def __delitem__(self,index):
#         print('delitem')
#         print(index)
        

# a = A()
# a.list_ = [1,2,3,4]
# a.dict_ = {1:'h'}
# a[0]
# a[1] = 9
# del a[2]



















'''============================================== classroom tasks ==============================================================='''
"""
1) Создайте свой класс MyUser. В этом классе реализуйте следующие условия:
При инициализации объекта, необходимо передавать аргументы: name, last_name. Автоматически программа генерирует вам пароль password, 
который состоит только из гласных букв, входящих в состав атрибутов name и last_name
При вызове самого объекта, возвращаются только первые буквы имени и фамилии, остальные буквы скрыты символом *
При попытке получения пароля (при вызове атрибута password) должна выдаваться ошибка-сообщение: “Forbidden”
	Например:
	user = MyUser(“Makers”, “Bootcamp”)
	print(user)  ->    M***** B*******
	print(user.password)  ->  Exception: Forbidden
"""



# class MyUser:

#     def __init__(self,name, last_name):
#         self.name = name
#         self.last_name = last_name
#         all_vowels = ['a','e','i','o','u','y']
#         vowels = []
#         for i in str(name+last_name):
#             if i in all_vowels:
#                 vowels.append(i)
#         self.password = ''.join(vowels)

#     def __str__(self):
#         return f"{self.name[0] + len(self.name[1:]) * '*'} {self.last_name[0] + len(self.last_name[1:]) * '*'}"
    
#     def __getattribute__(self, item: str):
#         if item == 'password':
#             raise Exception('Forbidden')
#         return super().__getattribute__(item)

# user = MyUser('nursultan','kalilov')
# print(user)
# print(user.password)

"""
ПРИМЕР:
name = 'nurs'
last = 'kalilov'
all_vowels = ['a','e','i','o','u','y']
vowels = []
for i in str(name+last):
    if i in all_vowels:
        vowels.append(i)

password = ''.join(vowels)

print(password)
"""



















"""
2) Создайте класс MyTuple. Создайте объекты от этого класса, они должны быть кортежами, в которых элементы - числа. 
Далее сравните эти кортежи, но сравнение должно происходить по сумме чисел в кортежах. Например:
a = (1,2,3,4,5)  - сумма 15
b = (6,7,8)        - сумма 21
print(a == b) -> False
print(a > b) -> False
print(a < b) -> True
print(a != b) -> True

"""


# class MyTuple(tuple):

#     def __eq__(self, __value: object) -> bool:
#         if sum(self) == sum(__value):
#             return True
#         else:
#             return False
        
#     def __ne__(self,__value: object) -> bool:
#         if sum(self) != sum(__value):
#             return True
#         else:
#             return False
        
#     def __gt__(self,__value: object) -> bool:
#         if sum(self) > sum(__value):
#             return True
#         else:
#             return False
        
#     def __lt__(self,__value: object) -> bool:
#         if sum(self) < sum(__value):
#             return True
#         else:
#             return False
        
#     def __ge__(self,__value: object) -> bool:
#         if sum(self) >= sum(__value):
#             return True
#         else:
#             return False
        
#     def __le__(self,__value: object) -> bool:
#         if sum(self) <= sum(__value):
#             return True
#         else:
#             return False
        
# a = (1,2,3,4,5)  
# b = (6,7,8)      
# print(a == b)    # False
# print(a > b)     # False
# print(a < b)     # True
# print(a != b)    # True
# print(sum(a))    # сумма 15
# print(sum(b))    # сумма 21




















"""
1. Создайте класс Account и переопределите в нем методы __init__, __repr__, __str__ и __del__.
Объекты класса должны содержать атрибуты имени, баланса и города, где открыт счет.
Метод __init__ должен возвращать сообщение о создании счета, __repr__ только имя держателя счета
и баланс, а __str__ сообщение с приветствием и также информацией о держателе счета, 
балансе и филиале банка в котором зарегистрирован клиент, __del__ в свою очередь сообщение об удаление 
и слово "Пока!"
"""



# class Account:

#     def __init__(self,name,balance,city):
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print('счет открыт')

#     def __repr__(self):
#         return f"{self.name,self.balance}"

#     def __str__(self):
#         return f"салам алейкум {self.name} братан!\nу вас на балансе {self.balance} долларов\nвы зарегались в городе {self.city}"

#     def __del__(self):
#         print(f"Ваш аккаунт удален {self.name} братан. Так что Пока!" )

# obj = Account('Тима',500000,'Бишкек')
# print(obj)






















"""
2. Определите класс MyNumber который наследуется от класса int. 
У экземпляра класса должен быть обязательный атрибут value. 
Переопределите методы сложения, вычитания, умножения и деления для класса таким  образом чтобы 
при использовании операторов + - * / - результат возвращался с сообщением об использованном методе, 
например:print(num + 5)  -------> "Это сложение и Ваш результат равен 10"
"""


# class MyNumber(int):

#     def __init__(self,value):
#         self.value = value

#     def __add__(self,other: int):
#         return f"Это сложение и Ваш результат равен: {self.value + other}"
    
#     def __sub__(self, other: int):
#         return f"Это выяитание и Ваш результат равен: {self.value - other}"
    
#     def __mul__(self,other: int):
#         return f"Это умножение и Ваш результат равен: {self.value * other}"
    
#     def __truediv__(self,other: int):
#         return f"Это деление и Ваш результат равен: {self.value / other}"
    
# num = MyNumber(5)
# print(num + 5)




















"""
3. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
"""


# class MyList(list):
#     def __getitem__(self, index):
#         if isinstance(index, slice):
#             start, stop, step = index.indices(len(self))
#             return [super().__getitem__(i) for i in range(start, stop, step)]
#         else:
#             if index < 0:
#                 index = len(self) + index + 1
#             return super().__getitem__(index - 1)

#     def __setitem__(self, index, value):
#         if index < 0:
#             index = len(self) + index + 1
#         super().__setitem__(index - 1, value)

# # Пример использования:
# x = MyList([1, 2, 3, 4, 5])

# # Индексация начинается с 1:
# print(x[1])  # Вывод: 1
# print(x[3])  # Вывод: 3

# # Можно использовать отрицательные индексы:
# print(x[-1])  # Вывод: 5

# # Можно использовать срезы:
# print(x[2:5])  # Вывод: [2, 3, 4]

# # Также работает обычная индексация:
# x[2] = 10
# print(x)  # Вывод: [1, 10, 3, 4, 5]


















"""
4. Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: 
имя, фамилия, класс, и оценки по предметам в следующем виде: {'math': 100, 'history': 89, 'literature': 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
"""

# class Student:
#     def __init__(self, name, last_name, *args, **kwargs ):
#         self.name = name
#         self.last_name = last_name
#         self.args = args
#         self.kwargs = kwargs

#     def average_rating(self):
#         total = sum(self.kwargs.values())
#         subjects = len(self.kwargs.values())
#         return total / subjects if subjects > 0 else 0

#     def __lt__(self, other):
#         return self.average_rating() < other.average_rating()

# student1 = Student('Albert','Einstein','physic',{'math': 100, 'history': 89, 'literature': 88})
# student2 = Student('Nursultan','Kalilov','python',{'math': 85, 'history': 90, 'literature': 92})

# if student1 < student2:
#     print(f"{student1.name} {student1.last_name} умнее чем {student2.name} {student2.last_name}")
# else:
#     print(f"{student2.name} {student2.last_name} умнее чем {student1.name} {student1.last_name}")


    


"""
5. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' 
для сравнения объектов класса - строк по длине(len). 
Также в методе __new__ напишите условие для удаления
пробелов и пустых строк в созданных словах.
"""

# class Word(str):

#     def __gt__(self,__value: object) -> bool:
#         if len(self) > len(__value):
#             return True
#         else:
#             return False
        
#     def __lt__(self,__value: object) -> bool:
#         if len(self) < len(__value):
#             return True
#         else:
#             return False
        
#     def __ge__(self,__value: object) -> bool:
#         if len(self) >= len(__value):
#             return True
#         else:
#             return False
        
#     def __le__(self,__value: object) -> bool:
#         if len(self) <= len(__value):
#             return True
#         else:
#             return False


