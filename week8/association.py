'''
абстракция -> принцип ооп , в котором создается класс пустышка, где задаются названия атрибутов и методов ,
что бы не забыть их переопределить в дочерних классах
'''


from abc import ABC, abstractmethod, abstractproperty

# class Abstract(ABC):

#     def __init__(self,a) -> None:
#         self.a = a

#     def metod(self):
#         print('metod 1')

#     @abstractmethod
#     def metod2(self):
#         pass

#     @abstractproperty
#     def metod3(self):
#         pass



# class A(Abstract):
    
#     def metod2(self):
#         print('переопределили абстрактный метод')

# a =A()
# a.metod()
# a.metod2()




'''
Абстрактный класс - не предназначен для создания от него объектов. Он предоставляет общие атрибуты и методы для всех дочерних классов,
что бы уменьшить дублирование кода

Абстрактный метод - это метод обязательный для переопределения в дочернем классе (есть объявление, но нет реализации) 
для создания такого метода используется декоратор abstractmethod
'''



# class Abst(ABC):

#     @abstractmethod
#     def get_info(self):
#         pass

#     @abstractmethod
#     def set_info(self):
#         ...


# class IdenticateMixin:

#     def identicate(self,year):
#         if int(year) < 2015:
#             return 'This is not new car'
#         return 'This is a new car'
    

# class BaseAuto(IdenticateMixin,Abst):

#     def __init__(self, model, year, owner):
#         self.model = model 
#         self.year = year
#         self.owner = owner

#     def get_info(self):
#         return f" Model: {self.model}\nYear: {self.year}"
    
#     def set_info(self, owner):
#         self.__owner = owner

#     def get_owner(self):
#         return self.__owner
    

# auto = BaseAuto('mers',2012,'nurs')
# print(auto.identicate(auto.year))
# auto.set_info('azi')
# print(auto.get_owner())



# class Auto(BaseAuto):

#     def __init__(self, model, year, owner,brand,color):
#         super().__init__(model, year, owner)
#         self.brand = brand
#         self.color = color

#     def get_info(self):
#         return f" Model: {self.model}\nYear: {self.year}\nBrand: {self.brand}\nColor: {self.color}"
    
#     @property
#     def owner(self):
#         return self.__owner
    
#     @owner.setter
#     def owner(self,owner):
#         self._BaseAuto__owner = owner

#     @owner.getter
#     def owner(self):
#         return self._BaseAuto__owner
    
#     @owner.deleter
#     def owner(self):
#         self._BaseAuto__owner = 'Nobody'

# auto = Auto('dsf',2022, 'sdgv', 'sdvsd', 'htsd')
# print(auto.get_info())
# print(auto.owner)
# auto.owner = 'Nurs'
# del auto.owner
# print(auto.owner)





'''
Ассоциация - это принцип ооп , в котором два класса связаны друг с другом 

1. Композиция - сильная связь
2. Агрегация - слабая связь

Композиция:

A - компонент
|
|
|
v
B - составной
'''



# class Wheel:
#     pass

# class Engine:
#     pass

# class Freshener:
#     pass

# class Car:

#     def __init__(self,freshener):
#         self.engine = Engine()
#         self.wheels = [Wheel(),Wheel(),Wheel(),Wheel()]  # Композиция
#         self.freshener = freshener                       # Агрегация


# elochka = Freshener()

# car = Car(elochka)
# del car
# print(elochka)
# print(car.__dict__)





# class Salary:

#     def __init__(self,pay):
#         self.pay = pay

#     def getTotal(self):
#         return (self.pay * 12)
    
# class Employee:
#     def __init__(self,pay,bonus):
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)

#     def annualSalary(self):
#         return f"Total: {self.salary.getTotal() + self.bonus}"
    
# emp = Employee(10000,2000)
# print(emp.annualSalary())





# class Salary:

#     def __init__(self,pay):
#         self.pay = pay

#     def getTotal(self):
#         return (self.pay * 12)
    
# class Employee:
#     def __init__(self,salary, bonus):
#         self.salary = salary
#         self.bonus = bonus


#     def annualSalary(self):
#         return f"Total: {self.salary.getTotal() + self.bonus}"
    
# salary = Salary(10000)
# emp = Employee(salary,2000)
# print(emp.annualSalary())






# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self,color):
#         self.color = color
#         self.battery = Battery()

# class Nokia:
#     def __init__(self,battery, color = 'черный'):
#         self.color = color
#         self.battery = battery

# battery = Battery()

# nokia = Nokia(battery,'dark blue')
# iphone = Iphone('red')


# del iphone
# del nokia
# print(battery)
# iphone.battery._power = 54
# iphone.battery.charge()
# print(iphone.battery._power)
# print(nokia.battery._power)








"""
1) Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, Telegram. 
При регистрации в WhatsApp и SnapChat необходимо передавать свой номер телефона, который должен быть int. 
При регистрации в Telegram необходимо передавать номер телефона и username. 
Во всех классах есть метод send, в WhatsApp он принимает только text и выдает строку “I am sending a text ...” 
и вместо … должен быть сам текст сообщения. В SnapChat send принимает image и text, при этом image должен быть булевым типом данных. 
Если image True, то выдается сообщение “I am sending a text … with some image ”, 
если  False - сообщение “I am sending a text … without image”. В Telegram метод send принимает voice message в виде строки 
и выдает сообщение “I am sending a voice message ...”. Создайте объекты от этих классов и вызовите метод send у всех объектов.
"""





# class WhatsApp:
#     def __init__(self,num: int,):
#         self.num = num

#     def send(self,text):
#         self.text = text
#         print(f"I am sending a text {self.text}")

# class SnapChat:
#     def __init__(self,num: int,):
#         self.num = num

#     def send(self,image: bool, text: str):
#         self.text = text
#         self.image = image
#         if self.image == True:
#             print(f"I am sending a text {self.text} with some image")
#         else:
#             print(f"I am sending a text {self.text} without image")
        

# class Telegram:
#     def __init__(self,num: int,username):
#         self.num = num
#         self.username = username

#     def send(self,voice: str):
#         self.voice = voice
#         print(f"I am sending a voice message {self.voice}")

# w = WhatsApp(996708144474)
# s = SnapChat(996708144474)
# t = Telegram(996708144474,'nurs')
# w.send('bla bla bla')
# s.send(True,'ne stoit tem........')
# t.send('пешеходдон кааач')










"""
2) Создайте два класса A и B. В обоих классах есть метод count. 
В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, 
а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и вызовите этот метод у каждого объекта.
"""

# class A:
#     def count(self, string: str):
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         count = 0
#         for i in string:
#             if i.lower() in vowels:
#                 count += 1
#         return count

# class B:
#     def count(self, string: str):
#         consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
#         count = 0
#         for i in string:
#             if i.lower() in consonants:
#                 count += 1
#         return count


# a = A()
# b = B()

# print(a.count('zharko'))
# print(b.count('zharko'))









# Task association
"""
1. Создайте абстрактный класс DaysAndDates с двумя методами: define_date и define_days. 
Создайте три дополнительных класса: Current, MonthStart и MonthEnd. 
В Current необходимо вывести текущую дату. 
В MonthStart вывести первый день текущего месяца и кол-во дней с первого дня до текущего дня. 
В MonthEnd вывести последний день текущего месяца и кол-во дней до конца месяца.
Даты выводить в формате: день/месяц/год, кол-во дней: в int.
К абстрактным методам добавить док-стринг с описанием методов.
"""

from abc import ABC, abstractmethod
import datetime

class DaysAndDates(ABC):
    day = datetime.datetime.now()
    month = datetime.datetime.now()
    year = datetime.datetime.now()
    # @abstractmethod
    def define_date(self):
        pass
    
    # @abstractmethod
    def define_days(self):
        pass

class Current(DaysAndDates):
    @abstractmethod
    def define_date(self) -> int:
        print(f"{DaysAndDates.day.day}/{DaysAndDates.month.month}/{DaysAndDates.year.year}")
        



class MonthStart(DaysAndDates):

    def define_date(self) -> int:
        print(f"{DaysAndDates.day.day}/{DaysAndDates.month.month}/{DaysAndDates.year.year}")

    def define_days(self): 
        print(f"первый день текущего месяца: 1/{DaysAndDates.month.month}/{DaysAndDates.year.year}\nкол-во дней с первого дня до текущего дня:{DaysAndDates.day.day - 1}")

class MonthEnd(DaysAndDates):

    def define_days(self): 
        print(f"последний день текущего месяца: 31/{DaysAndDates.month.month}/{DaysAndDates.year.year}\nкол-во дней до конца месяца: {31-DaysAndDates.day.day}")




a = Current()
a.define_date()



# date = datetime.datetime.now()
# print(date.day)
# print(date.month)
# print(date.year)




