# + 
# 4 + 4 
# 'str'  + string

# [1,2,3,5,6,] + ['r','a']


# class Cat:
#     def init(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"It's a cat. Cat's name is {self.name} ")

#     def make_sound(self):
#         print('meow','meow')

# class Dog:
#     def init(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"It's a dog. Dog's name is {self.name} ")


#     def make_sound(self):
#         print('gav','gav')

         

# cat = Cat('elice',age=1)
# dog = Dog('reks',age=4)
# for i in (cat, dog):
#     i.make_sound()
#     i.info()

# from math import pi
# class Shape:

#     def init(self,name):
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         print('Я фигура в двумерном пространстве')


#     def str(self):
#         return self.name
    
# class Square(Shape):
#     def init(self, length):
#         super().init('spuare')
#         self.length = length


#     def area(self):
#         print(self.length, 2)

#     def fact(self):
#         print('У квадрата все стороны равны')

# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__('Circle')
#         self.radius = radius


#     def ara(self):
#         print(pi * self.radius, 2)

# square = Square()
# circle = Circle(3)

# circle.area()
# square.area()
# circle.fact()
# square.fact()

# for i in [Square(5), Square(9), Circle(8), Circle(5)]:
#     print(i)
#     i.area()
#     i.fact()








'''====================================== task ========================================'''

# task 1

# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 


# lst = [a,b,c]
# for i in lst:
#     print(len(i))



# task 2

# class Cat:
#     def voice(self):
#         print('Мяу')


# class Dog:
#     def voice(self):
#         print('Гав')

# barsik = Cat()
# rex = Dog()

# def to_pet(animal):
#     return animal.voice()

# to_pet(barsik) 
# to_pet(rex) 





# task 3


# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}"

# class Employee(Person):
#     def __init__(self, name, last_name,work,status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status

#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}"

# class Student(Person):
#     def __init__(self,name,last_name,university,course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course

#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе"

# person = Person('Иван', 'Петров')
# employee = Employee('Иван', 'Петров','Рога и копыта','директор')
# student = Student('Иван', 'Петров','КГТУ',3)


# def get_human_info(a):
#     print(a.get_info())

# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person) 








# task 4

# from abc import ABC,abstractmethod
# from math import pi

# class Shape(ABC):

#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return 0.5 * self.base * self.height

# class Square(Shape):
#     def __init__(self,length):
#         self.lenght = length

#     def get_area(self):
#         return self.lenght ** 2

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def get_area(self):
#         return pi * self.radius ** 2
        
# triangle = Triangle(5,5)
# square = Square(5)
# circle = Circle(10)


# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area()) 





# task 5

# class OS:
#     def __init__(self,version):
#         self.version = version

#     def copy(self):
#         pass

# class Windows(OS):

#     def copy(self,text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'
        
# class MacOS(OS):

#     def copy(self,text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'


# class Linux(OS):

#     def copy(self,text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'
    

# win = Windows(2.3)
# mac = MacOS(16)
# lin = Linux(3)


# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))









# task 6
# class Language: 
#     def __init__(self, level, type) -> None: 
#         self.lvl = level 
#         self.type = type 
        
# class Python(Language): 
#     def write_function(self, func_name, arg): 
#         return f"def {func_name}({arg}):" 
    
#     def create_variable(self, var_name, value): 
#         if isinstance(value, str): 
#             return f"{var_name} = '{value}'" 
#         else: 
#             return f"{var_name} = {value}" 
        
# class JavaScript(Language): 
#     def write_function(self, func_name, arg): 
#         return f"function {func_name}({arg}) {{ }};" 
    
#     def create_variable(self, var_name, value): 
#         if isinstance(value, str): 
#             return f"let {var_name} = '{value}';" 
#         else: 
#             return f"let {var_name} = {value};" 
        
# py = Python('Intermediate', 'Backend') 
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John')) 
# js = JavaScript('Advanced', 'Frontend') 
# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))

    



# task 7
# class Money:
#     def __init__(self,country,symbol):
#         self.country = country
#         self.symbol = symbol

# class Dollar(Money):
#     rate = 84.80

#     def exchange(self,count):
#         amount = self.rate * count
#         return f"{self.symbol} {count} равен {amount} сомам"
    
# class Euro(Money):
#     rate = 98.40

#     def exchange(self,count):
#         amount = self.rate * count
#         return f"{self.symbol} {count} равен {amount} сомам"
    
# d = Dollar('Amerika','$')
# e = Euro('europe','€')

# print(d.exchange(100))
# print(e.exchange(80))





# task 8

# class Planet: 
#     def __init__(self, orbit): 
#         self.orbit = orbit 
        
        
# class Mercury(Planet): 
#     def get_age(self, earth_age): 
#         return f"на Меркурии ваш возраст составляет {int(earth_age * 365 / self.orbit)} лет"
    
    
# class Venus(Planet): 
#     def get_age(self, earth_age): 
#         return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit * 365)} дней' 
    
    
# class Jupiter(Planet): 
#     def get_age(self, earth_age): 
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов' 
    
# mercury = Mercury(88) 
# venus = Venus(225) 
# jupiter = Jupiter(12) 
# print(venus.get_age(20)) 
# print(jupiter.get_age(20)) 
# print(mercury.get_age(20))