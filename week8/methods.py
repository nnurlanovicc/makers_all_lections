"""
Методы экземпляра, класса, статичские

1. методы экземпляра класса (instance methods)
2. методы класса (class methods)
3. статические методы (static methods)
"""


'''
1. Методы экземпляра класса - обычные методы, которые первым аргументом принимабт self (ссылка на объект)
они нужны для работы с атрибутами объекта 

'''


# class A:
#     def instance_method(self):
#         print('метод экземпляра')
#         print('первый аргумент', self)

# obj = A()
# obj.instance_method()
# A.instance_method(obj)





'''
2. методы класса - метод , который принимает первым аргументом ссылку на класс (cls). 
нужны для создания объектов или изменения атрибутов класса.
для создания нужно задекорировать его classmethod
'''

# class B:
#     @classmethod
#     def class_method(cls):
#         print('метод класса')
#         print('первый аргумент', cls)

# B.class_method()
# b = B()
# B.class_method()



# class Car:
#     color = 'red'

#     @classmethod
#     def change_color(cls,value):
#         cls.color = value

#     # def change_color(self,value):
#     #     self.color = value

# a = Car()
# b = Car()
# a.change_color('blue')
# print(a.color, b.color)




# class Pizza:

#     def __init__(self,radius,*ingredients):
#         self.radius = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(f"готовится пицца размером {self.radius} см")
#         print(f"ингридиенты: {self.ingredients}")

#     @classmethod
#     def four_cheeze(cls,r):
#         pizza = cls(r, 'моцарелла', 'чеддер', 'голландский','дор-блю')
#         return pizza


# pizza1 = Pizza(15,'пепе', 'сыр','перец','чеснок','ананас','оливки','соус')
# pizza1.cook()
# pizza_four_cheeze = Pizza.four_cheeze(23)
# pizza_four_cheeze.cook()



'''
3. статический метод - чтобы их создать изпользуется декоратор staticmethod
просто функции внутри класса , не принимают ссылку ни на объект ни на класс 
не взоимодействуют ни c клаcсом ни с объектом 
используются только внутри класса 
дополнительные функции которые производят какие то вычисления , переобразования типа данных итд итп 
'''


# class C:

#     @staticmethod
#     def pow_(z):
#         return z ** 2
    
# c = C()



# class Cylinder:
#     def __init__(self,diametr,hight):
#         self.diametr = diametr
#         self.hight = hight
#         self.area = self.get_area(diametr, hight)


#     @staticmethod
#     def get_area(d,h):
#         from math import pi
#         circle = pi * d**2/4
#         side = pi * d * h
#         area = circle * 2 + side
#         return round(area,2)


# cylinder = Cylinder(10,4)
# print(cylinder.area)






# class Home:

#     people = 0

#     def __init__(self,name,last_name, count_people):
#         self.name = name
#         self.last_name = last_name
#         self.count_people = count_people
#         Home.people += count_people

#     def info(self):
#         print(f"кавртира в этом доме принадлежит {self.name} {self.last_name}")

#     @classmethod
#     def f(cls):
#         print(cls.people)

#     @staticmethod
#     def about_home():
#         print('самый многоэтажный дом')

# a = Home('nurs','nurlan', 3)
# b = Home('frank','lost',5)
# a.f()    
# a.info()
# b.info()
# b.about_home()








# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. 
# Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность зарядить батарею.



# class Phone:

#     __power = 100

#     def __init__(self,imei,os):
#         self.__imei = imei
#         self.__os = os

#     def check(self,battery):
#         if self.__power <= battery:
#             raise Exception('телефон разряжен')

#     @property
#     def battery(self):
#         print(self.__power)

#     @property
#     def get_info(self):
#         self.check(1)
#         self.__power -= 0.5
#         print(f"OC: {self.__os}\nIMEI:{self.__imei}")


#     def listen(self):
#         self.check(5)
#         self.__power -= 5
#         print("играет трек")

#     def watch(self):
#         self.check(10)
#         self.__power -= 7
#         print("идет просмотр")


#     def charge(self,sec):
#         from datetime import datetime,timedelta
#         from time import sleep
#         now = datetime.now
#         end_time = (now() + timedelta(seconds=sec)).strftime('%M:%S')

#         while now().strftime('%M:%S') != end_time:
#             sleep(1)
#             if self.__power < 100:
#                 self.__power += 1
#             if self.__power == 100:
#                 print(f"телефон заряжен на {self.__power}%")
#                 break
#             print(f"идет зарядка, уровкеь заряда {self.__power}%")


# a = Phone('12435','ios')
# a.listen()
# a.watch()
# a.charge(10)




























