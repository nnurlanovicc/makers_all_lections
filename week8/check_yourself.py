"""
1) Создайте класс Auto в нем реализуйте метод ride который выводит сообщение 'Riding on a ground'.

Создайте класс Boat реализуйте метод swim, который выводит 'Floating on water'.

Создайте класс Amphibian который наследуется от класса Auto и Boat.

Создайте от него объект obj и вызовите все методы.

Ввод:

obj = Amphibian() 
obj.ride() 
obj.swim() 
Вывод:

Riding on a ground 
Floating on water 
"""


# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto,Boat):
#     pass

# obj = Amphibian() 
# obj.ride() 
# obj.swim() 













"""
2)Создайте класс ContactList, который должен наследоваться от встроенного класса list.

В вашем классе должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений.

Создайте экземпляр класса в переменной all_contacts и передайте список ваших контактов.

Примерный ввод:

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 
Метод search_by_name возвращает все строки содержащие подстроку "Olya":

['Ivan Olya', 'Olya Ivan'] 
"""




# class ContactList(list):

#     def __init__(self,list):
#         self.list = list

#     def  search_by_name(self,name):
#         names = []
#         self.name = name
#         for i in self.list:
#             if i == self.name:
#                 names.append(i)
#             else:
#                 for j in i.split():
#                     if j == self.name:
#                         names.append(i)
#         return names
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))




"""
3) Напишите класс Person, который будет хранить информацию о пользователе. 
У объекта будут следующие атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email).
При инициализации объекта, передавать аргументы классу не нужно, 
все его атрибуты по умолчанию будут равны None и также все они будут приватными.
Поэтому реализуйте для каждого атрибута методы доступа get и set не используя декораторы property и setter. 
У вас будут такие методы: get_name, set_name, get_last_name, set_last_name, get_age, set_age, get_email, set_email.
Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран.
Пример:

john = Person()
print(john.get_name()) # None
print(john.get_last_name()) # None
print(john.get_age()) # None
print(john.get_email()) # None
john.set_name('John')
john.set_last_name('Snow')
john.set_age(30)
john.set_email('johnsnow@gmail.com')
print(john.get_name()) # John
print(john.get_last_name()) # Snow
print(john.get_age()) # 30
print(john.get_email()) # johnsnow@gmail.com
"""

# class Person:
#     __name = None
#     __last_name = None
#     __age = None
#     __email = None
#     def set_name(self,name):
#         self.__name = name
#         return self.__name
#     def set_last_name(self,last_name):
#         self.__last_name = last_name
#         return self.__last_name
#     def set_age(self,age):
#         self.__age = age
#         return self.__age
#     def set_email(self,email):
#         self.__email = email
#         return self.__email
    

#     def get_name(self):
#         return self.__name
#     def get_last_name(self):
#         return self.__last_name
#     def get_age(self):
#         return self.__age
#     def get_email(self):
#         return self.__email

# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com

















"""
4)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. Затем определите метод set_speed, 
который будет устанавливать значение скорости и метод show_speed, с помощью которого Вы будете получать значение скорости.
"""


# class Car:

#     def __init__(self,):
#         self.__speed = None

#     def set_speed(self,speed):
#         self.__speed = speed

#     def show_speed(self):
#         return self.__speed
    
# car = Car()
# car.set_speed(200)
# print(car.show_speed())





"""
5)Перепишите класс Car из предыдущего задания.
Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, 
для того чтобы можно было работать с данным классом следующим образом:

car = Car()
car.speed = 120
print(car.speed)
"""


# class Car:

#     def __init__(self,):
#         self.__speed = None

#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self,speed):
#         self.__speed = speed

# car = Car()
# car.speed = 120
# print(car.speed)
