"""
Основеые принципы ООП: Наследование



Основные принципы :
1. Наследие
2. Полиморфизм
3. Инкапсуляция


Остальные принципы:
1. Ассоциация
    1.Агреегация
    2.Композиция
2. Абстракция






Наследие это принцип ООП, в котором мы можем унаследовать, 
переопределить и исползовать методы и атрибуты родительского класса в дочернем классе.
Создаем новый класс на основе уже существующего.


"""

'''=============== Синтаксис для наследования ==============='''
# class Родительский_класс:
    # методы и атрибуты род кл

# class Дочерний_класс(Родительский_класс):
    # методы и атрибуты доч кл




# class A:
#     def func1(self,a):
#         print(self,a)

#     def __str__(self):
#         return 'это объект класса A'




# class B(A):
#     def __str__(self):
#         return 'это объект класса B'

# b = B()
# b.func1(12)

# a = A()
# a.func1(3)




# class A:
#     def func(self):
#         print('я метод в классе А')

# class C:
#     '''
#     наследовали все методы и атрибуты класса А
#     и полностью переопределили метод func
#     '''
#     def func(self):
#         print('я метод в классе C')


# class D(A):
#     pass

# d = D()
# d.func()  #я метод в классе А







'''
MRO -> method resolution order
порядок поиска атрибутов
'''



# class A:
#     x = 'x in A'
#     y = 'y in A'

# class B(A):
#     x = 'x in B'

# a = A()
# b = B()

# print(B.mro())          #[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# print(B.__mro__)        #(<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

# print(b.x)
# print(b.y)
# print(a.x)
# print(a.y)






# o = object()       класс от которого наследуются все классы python
# print(dir(o))






'''
=========================== виды наследование ===========================:
1. одиночное
2. иерархическое ->             когда у одного родительского класса много дочерних классов
3. многоуровневое наследие ->   когда дочерний класс наследууется от класса у которого есть родители
4. множественное ->             когда дочерний класс наследует от нескольких род. классов
5. гибридное ->                 когда используются несколько видов неследования
'''




# class Person:
#     def __init__(self,name,age,last_name):
#         self.name = name
#         self.age = age
#         self.last_name = last_name
    

#     def display_info(self):
#         print(f"Name: {self.name}\nLast name: {self.last_name}\nAge: {self.age}")


# class Employee(Person):
#     def work(self):
#         print(f"{self.name} works")


# class Students(Person):
    # def __init__(self, name: str, age: int, last_name: str, class_: int, faculty: str):   # 1. cпособ
    #     self.name = name
    #     self.age = age
    #     self.last_name = last_name
    #     self.class_ = class_
    #     self.faculty = faculty
    # def __init__(self, name: str, age: int, last_name: str, class_: int, faculty: str):   # 2. способ
    #     Person.__init__(self,name,age,last_name)
    #     self.class_ = class_
    #     self.faculty = faculty
#     def __init__(self, name: str, age: int, last_name: str, class_: int, faculty: str):     # 3ю способ
#         super().__init__(name,age,last_name)
#         self.class_ = class_
#         self.faculty = faculty



#     def display_info(self):
#         print(f"Name: {self.name}\nLast name: {self.last_name}\nAge: {self.age}\nClass: {self.class_}\nFaculty: {self.faculty}")    

# worker = Employee('Nurs',23,'Kalilov')
# worker.display_info()


# student = Students('Peter',23,'Parker',4,'IT')
# student.display_info()




# class A:

#     def __init__(self,range):
#         self.range = range
#     def my_range(self):
#         list_ = [i for i in range(self.range)]
#         print(list_)

# num = int(input('enter the number'))
# a = A(num)
# a.my_range()






# class A:
#     def my_range(self, start, end, step):
#         i = start
#         while i < end:
#             yield i
#             i += step

# element = A()
# ls = element.my_range(1, 10, 2)
# for i in ls:
#     print(i)








# class A:
#     def my_range(self, start, end, step):
#         while start < end:
#             yield start
#             start += step
        
# element = A()
# ls = element.my_range(1, 10, 2)
# for i in ls:
#     print(i)



# class A:
#     def my_range(self, start, end, s=1):
#         return list(range(start, end, s))
    
# a = A()
# result = a.my_range(1, 11)
# print(result)  

# result = a.my_range(10, 0, -1)
# print(result)




"""
==========================================множественное наследование
"""

# isinstance() -> проверяет является ли объект экземрляром класса 
# issubclass() -> проверяет является ли класс подклассом второго аргумента

# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass



# a = A()
# b = B()
# c = C()
# print(issubclass(C,A))
# print(issubclass(B,A))
# print(issubclass(B,C))

# print(isinstance(a,object))
# print(isinstance(c,A))

# class User:
#     def __init__(self,username,age,city,password):
#         self.username = username
#         self.age = age
#         self.city = city
#         self.password = password

#     def get_profile_info(self):
#         print(f"имя ползователя: {self.username}\nвозраст: {self.age}\nгород проживания: {self.city} ")

#     def greet_user(self):
#         print(f"добро пожаловать {self.username}")

#     def __str__(self) -> str:
#         return self.username


# class Admin(User):
#     def __init__(self, username, age, city, password):
#         super().__init__(username, age, city, password)
#         self.privileges = []

#     def __str__(self):
#         return self.username
    
#     def set_privileges(self,priv):
#         self.privileges.append(priv)

#     def show_privileges(self):
#         return self.privileges

# admin = Admin('Nurs',23,'Bishkek',12345678)
# # print(admin)
# admin.set_privileges('delete posts')
# admin.set_privileges('delete users')
# print(admin.show_privileges())
# admin.get_profile_info()
# admin.greet_user()
# user = User('Azi',18,'Bishkek',123456789)
# user.get_profile_info()
# user.greet_user()
# # print(user)





# class Lion:
#     color = 'black'

# class Lioness:
#     color = 'brown'

# class Child(Lion,Lioness):
#     pass

# obj = Child()
# print(obj.color)
# print(Child.__mro__)




"""
============================= проблемы множественного наследования


1. проблема ромба -> решена с помощью mro
2. проблема перекрестного наследования -> не решена


"""


# ====================1
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass
# print(D.__mro__)




# class X:
#     pass
# class Y:
#     pass
# class Z:
#     pass
# class A(X,Y):
#     pass
# class B(Y,Z):
#     pass
# class M(B,A,Z):
#     pass

# print(M.__mro__)






#=======================2

# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
# class D(B,A):
#     pass
# class M(C,D):
#     pass
# m = M()
# не решеная проблема скрещенного наследования




"""
Миксины -> классы которые используются для наследования но от них не создаются объекты
используются для добавления одних и тех же методов в разные классы

работа с Mixin 
1. принято давать имена заканчивающиеся на Mixin GreatMixin GetListMixin ....
2. он не предназначен для создания функционала другого класса
3. нужны для расширения функционала другог класса 
"""


# class MoveMixin:
#     def move(self):
#         print(f'я {self} и я двигаюсь')

# class StopMixin:
#     def stop(self):
#         print('я стою')


# class Car(MoveMixin,StopMixin):
#     def __str__(self) -> str:
#         return 'машина'


# class Person(MoveMixin,StopMixin):
#     def __str__(self) -> str:
#         return 'человек'




# car = Car()
# car.move()
# car.stop()

# person = Person()
# person.move()
# person.stop()

# objs = [Car(), Car(), Person()]

# for i in objs:
#     i.move()











# class CreateMixin:
#     def create(self,todo,key):
#         if key in self.todos:
#             return 'задача под таким номером уже есть'
#         else:
#             self.todos[key] = todo
#             return self.todos
        

# class DeleteMixin:
#     def delete(self,key):
#         deleted = self.todos.pop(key)
#         return deleted



# class UpdateMixin:
#     def update(self,key,new_value):
#         if key in self.todos.keys():
#             self.todos[key] = new_value
#             return self.todos
#         else:
#             return f'{key} нет в задачах'
        

# class ReadMixin:
#     def read(self):
#         return sorted(self.todos.items())


# class Note(CreateMixin,DeleteMixin,UpdateMixin,ReadMixin):
#     todos ={}

# task = Note()
# task.create('заснуть',1)
# task.create('просыпаться рано',2)
# task.create('умытся',3)
# task.create('позавтракать',4)
# task.create('еще поспать',5)
# task.update(3,'принять душ')
# task.delete(5)
# print(task.todos)
# print(task.read())














































"""=============================== task on classroom ==============================="""

# 1
# import random

# class Languages:
#     all_students = 0

# class Python(Languages):
#     pyhton_students = 0
#     def coding(self):
#         return "I am Python student. I am coding now."
    
#     def add_to_all_students(self):
#         Languages.all_students += 1
#         self.pyhton_students += 1




# class JavaScript(Languages):
#     java_students = 0
#     def coding(self):
#         return "I am JavaScript student. I am coding now."
    
#     def add_to_all_students(self):
#         Languages.all_students += 1
#         self.java_students += 1
    

# python_student = Python()
# java_student = JavaScript()

# python_student.add_to_all_students()
# java_student.add_to_all_students()

# print(python_student.pyhton_students)
# print(java_student.java_students)
# print(Languages.all_students)


# students = [python_student, java_student]
# random_student = random.choice(students)


# guess = input('какого студента я выбрал?\npy или js : ')


# if random_student == python_student:
#     python_student.coding()
# else:
#     java_student.coding()

# if guess.lower() == "py" and random_student == python_student:
#     print("Good job!")
#     print(random_student.coding())
# elif guess.lower() == "js" and random_student == java_student:
#     print("Good job!")
#     print(random_student.coding())
# else:
#     print("No bueno")







# 2
# from typing import Any
# from typing_extensions import SupportsIndex


# class MyList(list):
#     def insert(self, __object: Any, __index: SupportsIndex,) -> None:
#         return super().insert(__object,__index)
    






















"""=============================== tasks of platform ==============================="""

# 1
# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass
# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass
# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()





# 2
# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()







# 3
# class MyString(str):

#     def __init__(self,a: str):
#         self.a = a
    
#     def append(self,_str: str):
#         self._str = _str
#         self.a = self.a + self._str
#         return self.a
    
#     def pop(self):
#         last_one = self.a[-1]
#         self.a = self.a[:-1]
#         return last_one
#     def __str__(self) -> str:
#         return self.a
    
# example = MyString('String') 
# example.append('hello') 
# print(example) 
# print(example.pop()) 
# print(example)
 
        





# 4
# class MyDict(dict): 
#     def get(self,key,default = 'Are you kidding?'): 
#         return dict.get(self,key,default) 
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))








# 5
# class Person: 
#     def __init__(self,name, age): 
#         self.name = name 
#         self.age = age 
#     def display(self): 
#         print(f'name:{self.name}, \nage:{self.age}') 
# class Student(Person): 
#     def __init__(self, name, age, faculty): 
#         super().__init__(name, age) 
#         self.faculty = faculty 
#     def display_student(self): 
#         info = super().display() 
#         info = f'name:{self.name}, \nage:{self.age}, \nfaculty:{self.faculty}' 
#         print(info)
# obj_student = Student('Rick', 21, 'science')
# obj_student.display()
# obj_student.display_student()


# class Person: 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age 
#     def display(self): 
#         return f'name:{self.name}, age:{self.age}' 
# class Student(Person): 
#     def __init__(self, name, age, faculty): 
#         super().__init__(name, age) 
#         self.faculty = faculty 
#     def display_student(self): 
#         info = super().display() 
#         info += f', faculty:{self.faculty}' 
#         return info 
# obj_student = Student('Rick', 21, 'science') 
# print(obj_student.display()) 
# print(obj_student.display_student())














# 6
# class ContactList(list): 
#     def __init__(self, list_): 
#         self.list_ = list_ 
#     def search_by_name(self, name): 
#         a = [] 
#         for i in self.list_: 
#             if name in i: 
#                 a.append(i) 
#         return a 
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))












# 7
# import datetime
# class SmartPhones:
#     def __init__(self,name: str,color: str,memory: int,battery=0):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery
    
#     def __str__(self):
#         return f"{self.name} {self.memory}"
    

#     def charge(self,battery: int):
#         self.battery = battery
#         return self.battery

# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios): 
#         super().__init__(name, color, memory) 
#         self.ios = ios

#     def send_imessage(self,message: str):
#         return f"sending {message} from {self.name} {self.memory}"
    

# class Samsung(SmartPhones):
#     def __init__(self,name,color,memory,android):
#         super().__init__(name,color,memory)
#         self.android = android
    

#     def show_time(self):
#         time = datetime.datetime.now()
#         return time.time()
    

# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 


# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 


# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time()) 








# 8
# class CustomError(Exception):
#     def __init__(self,message: str):
#         self.message = message


# capitals_error = CustomError("ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ")

# def check_letters(str_: str):
#     if str_.islower():
#         raise capitals_error
#     else:
#         return f"ВСЕ ОТЛИЧНО! {str_}"
    
# print(check_letters("HELLO")) 
# print(check_letters("hello")) 


















"""=============================== task replit ==================================="""

# 1
# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('floating on water')

# class Amphibian(Auto,Boat):
#     pass

# obj = Amphibian()
# obj.ride()
# obj.swim()




# 2
# class RadioMixin:
#     def play_music(self,music: str):
#         print(f"играет музыка {music}")


# class Auto(RadioMixin):
#     def ride(self):
#         print('Riding on a ground')  

# class Boat(RadioMixin):
#     def swim(self):
#         print('floating on water')


# class Amphibian(Auto,Boat):
#     pass

# obj = Amphibian()
# obj.ride()
# obj.swim()
# obj.play_music('Blinding lights')





# 3
# import datetime
# class Clock:
#     def seychas(self):
#         time = datetime.datetime.now()
#         print(time.time())
    
# class Alarm:
#     # def __init__(self):
#     #     self.is_on = False

#     def on(self):
#         # if not self.is_on:
#         #     self.is_on = True
#             print('Будильник включен.')
#         # else:
#             # print("Будильник уже включен.")

#     def off(self):
#         # if self.is_on:
#         #     self.is_on = False
#             print('Будильник выключен.')
#         # else:
#         #     print("Будильник уже выключен.")


# class AlarmClock(Clock,Alarm):

#     def set_alarm(self, alarm_time: str):
#         self.alarm_time = alarm_time
#         print(f"Будильник установлен на {alarm_time}.")
#         return Alarm.on(self)
    
# obj = AlarmClock()
# obj.seychas()
# obj.on()
# obj.off()
# obj.set_alarm('08:00')










# 4
# class Coder:
    
#     count_code_time = 0
    
#     def __init__(self,experience: int):
#         self.experience = experience

#     def get_info(self):
#         pass

#     def coding(self):
#         pass

# class Backend(Coder):
#     def __init__(self, experience: int,languages_backend,name):
#         self.experience = experience
#         self.languages_backend = languages_backend
#         self.name = name

#     def get_info(self):
#         print(f"имя кодера {self.name}, пишет на языке {self.languages_backend}, опыт работы {self.experience} года")

#     def coding(self,coding_time: int):
#         self.count_code_time += coding_time
        


# class Frontend(Coder):
#     def __init__(self, experience: int,languages_frontend,name):
#         self.experience = experience
#         self.languages_frontend = languages_frontend
#         self.name = name

#     def get_info(self):
#         print(f"имя кодера {self.name}, пишет на языке {self.languages_frontend}, опыт работы {self.experience} года")

#     def coding(self,coding_time: int):
#         self.count_code_time += coding_time   
    

# class FullStack(Backend,Frontend):
#     def __init__(self, experience: int, languages_backend,languages_frontend, name):
#         self.experience = experience
#         self.languages_backend = languages_backend
#         self.languages_frontend = languages_frontend
#         self.name = name

#     def get_info(self):
#         print(f"имя кодера {self.name}, пишет на языках {self.languages_backend} и {self.languages_frontend}, опыт работы {self.experience} лет")

# back = Backend(3,'python','Nurs')
# front = Frontend(2,'javascript','Azi')
# full = FullStack(6,'python','javascript','Jackie Chan')


# # back.get_info()
# # front.get_info()
# # full.get_info()

# # back.coding(5)
# # print(back.count_code_time)

# # front.coding(3)
# # print(front.count_code_time)

# # full.coding(8)
# # print(full.count_code_time)















