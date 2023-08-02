"""
основные принципы ООП: Инкапсуляция

это принцип ооп у которого есть две трактовки: 
1. Объединение всех свойств и методов в единую капсулу или класс
2. Сокрытие данных -> ограничение доступа к методам и атрибутам 


"""


# 1) инкапсуляция как связь 

# class Phone:
#     number = '+996708144474'

#     def print_number(self):
#         print(f"Мой номер: {self.number}")

# nokia = Phone()
# nokia.print_number()


'''связали поведение объекта с его данными'''


# class Phone:
#     def __init__(self,number):
#         self.number = number

#     def print_number(self):
#         print(f"Мой номер: {self.number}")

# nokia = Phone('+996708144474')
# nokia.print_number()



# 2) Bнкапсуляция как сокрытие данных (управление доступом)

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

# pt = Point(4,5)
# print(pt.x,pt.y)
# pt.x = 2
# pt.y = 'idi naxuy jeckie chan'
# print(pt.x,pt.y)



"""
модификаторы доступа:
1. public -> публичный (без нижнего подчеркивания) -> данные доступны всем 
2. _protected -> защищенный (с одним нижним подчеркиванием в начале) -> данные доступны как внутри класса, так и удочерних
3. __private -> приватный (с двумя подчеркиваниями) -> данные доступны только внутри класса которому они принадлежат 
"""


# 2
# class Point:
#     def __init__(self,x,y):
#         self._x = x
#         self._y = y

# pt = Point(4,5)
# print(pt._x,pt._y)
# pt._x = 2
# pt._y = 'idi naxuy jeckie chan'
# print(pt._x,pt._y)


# 3
# class Point:
#     def __init__(self,x,y):
#         self.__x = x
#         self.__y = y

#     def set_coord(self,new_x,new_y):
#         if type(new_x) in (int,float) and type(new_y) in (int, float):
#             self.__x = new_x
#             self.__y = new_y
#         else:
#             raise ValueError('координаты должны быть числа')
        
#     def get_coords(self):
#         return self.__x, self.__y
    

# pt = Point(4,5)
# pt.set_coord(6,8)
# print(pt.get_coords())
# print(pt._x,pt._y)
# pt.__x = 2
# pt.__y = 'idi naxuy jeckie chan'
# print(pt._Point__x,pt._Point__y)


"""
getter, setter -> методы через которые предпологается работа с приватными и защищенными атрибутами и методами

setter -> метод для задания (установки) нового значения атрибутам (в нем реализовываутся доп-я проверка присваиваемых значений)
getter -> метод для получения защищенных и приватных атрибутов
"""
 


# class Person:
#     def init(self, name, age):
#         self.name = name
#         self.__age = age
    
#     def set_coord(self, name, new_age):
#         if type(new_age) == (int):
#             self.__age = new_age
#             self.name = name
#         else:
#             raise ValueError('Координаты должны быть числами')
    
#     def get_coords(self):
#         return self.name, self.__age

# asd = Person('Alice', 29)
# print(asd.get_coords())
# asd.set_coord("Alice", 30)
# print(asd.get_coords())


# class Person:
#     def init(self, name, age):
#         self.name = name
#         self.__age = age
'''
    prooerty -> делает из метода атрибут (позволяет обращаться к методу как к атрибуту)
    передоставляемый атрибут применятется для вызова декораторов getter, setter

'''
#     @property 
#     def property_age(self):
#         return self.__age
    
#     @property_age.setter
#     def age(self, new_age):
#         if type(new_age) != (int):
#             raise ValueError('Возраст должен быть числом')
#         if new_age < self.__age:
#             raise ValueError('Вы не могли помолодеть')
#         if 0 < new_age < 110:
#             self.__age = new_age
#         else:
#             print('Invalid age')

    
#     @property_age.getter
#     def age(self):
#         return self.__age
# a = Person('Kate', 43)
# a.age = 23
# print(a.property_age)



# class Russia:
#     __name = 'Russian Federation'
#     __population = 0

#     @property
#     def population(self):
#         return self.__population
    
#     @population.setter
#     def population(self,new_population):
#         if not isinstance(new_population,(int,float)) or not new_population > 0:
#             raise ValueError('invalid value')
#         self.__population = new_population

# rus = Russia()
# rus.population = 23425325476
# print(rus.population)


















"""=========================== task of classroom ================================="""
"""
1). Создайте класс ContactList, который должен наследоваться от встроенного класса list.

В вашем классе должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений.

Создайте экземпляр класса в переменной all_contacts и передайте список ваших контактов.

Примерный ввод:

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
print(all_contacts.search_by_name('Olya'))
Метод search_by_name возвращает все строки содержащие подстроку "Olya":
"""


class ContactList(list):
    def init(self,list):
        self.list = list
    def  search_by_name(self,name):
        names = []
        self.name = name
        for i in self.list:
            if i == self.name:
                names.append(i)
            else:
                for j in i.split():
                    if j == self.name:
                        names.append(i)
        return names
all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan','nurs ivan'])
print(all_contacts.search_by_name('nurs'))



"""
2). Напишите класс Person, который будет хранить информацию о пользователе. У объекта будут следующие атрибуты экземпляра класса: 
имя(name), фамилия(last_name), возраст(age), почта (email).
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


class Person:
    __name = None
    __last_name = None
    __age = None
    __email = None
    def set_name(self,name):
        self.__name = name
        return self.__name
    def set_last_name(self,last_name):
        self.__last_name = last_name
        return self.__last_name
    def set_age(self,age):
        self.__age = age
        return self.__age
    def set_email(self,email):
        self.__email = email
        return self.__email
    

    def get_name(self):
        return self.__name
    def get_last_name(self):
        return self.__last_name
    def get_age(self):
        return self.__age
    def get_email(self):
        return self.__email
    
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
























