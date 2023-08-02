""" ========== ввведение в ООП =============="""



"""
ООП -> парадигма программирования, в которой все основывается на двух понятиях: Класс и объект

ПАРАДИГМА -> набор правил, идей, понятий, которые определяют стиль написаний кода




Класс -> это чертёж, описание того, какими свойсвами и повидением будет обладать объект


# свойства -> обычные переменные 
# поведение -> обычные функции (их называют методами)


объект -> это тоже самое что и экземпляр класса и инстанция
объект = экземпляр класса = инстанция -> это экземпляр класса с собственным состоянием этих свойств.
 Каждый объект является экземпляром определенного класса
"""







"""=========================== синтаксис ==========================="""


'''
class <Название>: -> объявили класс
    string = '' -> создали переменную класса (атрибут класса)

    def some_method(self): -> создали метод
        (функция которая определена внутри класса)
        pass
        self -> ссылка на объект
'''


# class A: 
#     string = 'Нурс'
#     def __str__(self):
#         return self.string
    



# class Person:
#     legs = 2
#     arms = 2

#     def __init__(self, name, age):
#         """
#         отвечает за инициализацию  объекта 
#         вызывается когда мы создаем объект self -> ссылав на созданный объект
#         здесь определяются атрибуты объекта 
#         """
#         self.name = name
#         self.age = age
#         """
#         self.name = name -> создается новый атрибут у объекта
#         """

#     def add_age(self):
#         self.age += 1

# # print(dir(Person))
# sam = Person('sam',23)
# # print(dir(sam))
# sam.add_age()

# nurs = Person('nurs',24)
# nurs.add_age()

# print(sam.__dict__)
# print(nurs.__dict__)

"""
Атрибуты класса -> переменные внутри класса (атрибуты на уровне класса) -> изпользуются чтоб создать константу,
которая не предпологается быть измененной. к ним можно обращатся через класс и через объект



методы и атрибуты объекта (экземпляра класса)
это методы и атрибуты которые есть у объекта но возможно их нет у самого класса
атрибуты уровня объекта/инстанция класса/экземпляра класса -> определяются в методе __init__ 
(к атрибутам объекта нельзя обратится через класс) 



объекты класса -> объекты созданные по шаблону или чертежу класса 
"""


# class Nurs:
#     var1 = 'переменная класса'

#     def __init__(self):
#         self.var2 = 'переменная объекта'


# # print(Nurs.__dict__)
# a = Nurs()
# print(dir(a))





# class Salary:
#     nalog = 15
#     def __init__(self, zp, staj):
#         self.zp = zp
#         self.staj = staj

#     def sum_nalog(self):
#         sum = self.zp * self.staj * self.nalog / 100
#         print(sum)

# a = Salary(35000, 14)
# a.sum_nalog()

















































"""======================== tasks of platform ========================="""


# 1

# class Song:

#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year


#     def show_author(self):
#         return f"Автор этой песни {self.author}"
    

#     def show_title(self):
#         return f"Название этой песни {self.title}"
    

#     def show_year(self):
#         return f"Эта песня вышла в  {self.year} году"
    

# song = Song('Happy','Pharrell Williams', '2013')

# print(song.show_title())
# print(song.show_author())
# print(song.show_year())








# 2
# class Circle:
#     color = 'Синий'
#     pi = 3.14

#     def __init__(self,radius):
#         self.radius = radius

    
#     def get_area(self):
#         area = self.pi * self.radius**2
#         return area
    

# circle = Circle(2) 
# circle.color = 'красный'
# print(circle.color)
# print(circle.get_area()) 





# 3

# class BankAccount:
#     balance = 0

#     def deposit(self,amount):
#         self.balance += amount
#         print(f"Ваш баланс: {self.balance} сом")

#     def withdraw(self,amount):
#         self.balance -= amount
#         print(f"Ваш баланс: {self.balance} сом")

# account = BankAccount()
# account.deposit(1000) 
# account.withdraw(500) 





# 4
# class Taxi:

#     def __init__(self,name: str,cost: int,cost_km: int):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km


#     def get_total_cost(self,km):
#         res = km * self.cost_km + self.cost
#         return f"Такси {self.name}, стоимость поездки: {res} сом"
    

# taxi1 = Taxi('Namba',90,20)
# taxi2 = Taxi('Yandex',70,25)
# taxi3 = Taxi('Jorgo',100,20)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))  





# 5
# class Phone:

#     def __init__(self,name: str,last_name: str,phone: str):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone


#     def get_info(self):
#         print(f"Контакт: {self.name} {self.last_name}, телефон: {self.phone}")


# contact = Phone('Jhon','Snow','+996777234567')
# contact.get_info()






# 6
# class Salary:
#     percent = 8

#     def __init__(self,salary: int,experience: int):
#         self.salary = salary
#         self.experience = experience


#     def count_percent(self):
#         sum = self.salary * self.experience * self.percent / 100
#         return sum

# obj = Salary(1000,10)
# print(obj.count_percent())






# 7
# import datetime

# class Nobel:
#     def __init__(self,category, year: int, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         res = datetime.datetime.now()
#         return f"выиграл {res.year - self.year} лет назад"
    
# winner1 = Nobel('Литуратура',1971,'Пабло Неруда')
# winner2 = Nobel('Литуратура',1994,'Кэндзабуро Оэ')
# print(winner1.get_year())
# print(winner2.get_year())






# 8
# class Password: 
#     def __init__(self, password): 
#         self.password = password 
    
#     def __str__(self) -> str:
#         return '*' * len(self.password) 
    
    
#     def validate(self): 
#         if not len(self.password) > 8 and len(self.password) < 15: 
#             return f'Password should be longer than 8, and less than 15' 
#         elif not any(map(lambda i: i.isdigit(), self.password)): 
#             return f'Password should contain numbers too' 
#         elif not any(map(lambda i: i.isalpha(), self.password)): 
#             return f'Password should contain letters as well' 
#         elif not any(map(lambda i: i in ['@', '#', '&', '$', '%', '!', '~', '*'], self.password)): 
#             return f'Your password should have some symbols' 
#         return f'Ваш пароль сохранен.' 
    
    
# password = Password('nurs1001@#$%') 
# print(password.validate()) 
# print(password)



# class Password:
#     def __init__(self, password):
#         self.password = password

#     def validate(self):
#         if not 15 > len(self.password) > 8:
#             raise Exception('Password should be longer than 8, and less than 15')
        
#         nums_contain = False
#         letters_contain = False
#         specials_contain = False

#         specials = ('@', '#', '&', '$', '%', '!', '~', '*')

#         for symbol in self.password:
#             if symbol.isdigit():
#                 nums_contain = True
#             if symbol.isalpha():
#                 letters_contain = True
#             if symbol in specials:
#                 specials_contain = True
        
#         if not nums_contain:
#             raise Exception('Password should contain numbers too')
#         if not letters_contain:
#             raise Exception('Password should contain letters as well')
#         if not specials_contain:
#             raise Exception('Your password should have some symbols')
        
#         return 'Ваш пароль сохранен.'
    
#     def __str__(self):
#         return len(self.password) * '*'

# password = Password('hello3@')
# print(password)




# 9
# class Math:
#     def __init__(self,number):
#         self.number = number

#     def get_factorial(self):
#         factorial = 1 
#         a = self.number 
#         while a > 1: 
#             factorial *= a 
#             a -= 1 
#         print(factorial)

#     def get_sum(self):
#         x = sum([int(y) for y in str(self.number)]) 
#         print(x)

#     def get_mul_table(self): 
#         for x in range(0,11): 
#             print(f'{self.number} x {x} = {self.number * x}')


# num = Math(0)
# num.get_factorial()
# num.get_sum()
# num.get_mul_table()




# class Math:
#     def __init__(self,number):
#         self.number = number

#     def get_factorial(self):
#         factorial = 1 
#         a = self.number 
#         while a > 1: 
#             factorial *= a 
#             a -= 1 
#         return factorial

#     def get_sum(self):
#         x = sum([int(y) for y in str(self.number)]) 
#         return x

#     def get_mul_table(self): 
#         summ = '' 
#         for i in range(11): 
#             summ += f'{self.number}x{i+1}={self.number * (i+1)}' + '\n'
#         return summ


# num = Math(0)
# print(num.get_factorial())
# print(num.get_sum())
# print(num.get_mul_table())





# 10
# class ToDo: 
#     def __init__(self,string): 
#         self.todo = string 
#     instances = dict() 
        
        
#     def give_priority(self,priority): 
#         ToDo.instances[priority] = self.todo 
        
#     def list_of_tasks(self): 
#         return sorted(ToDo.instances.items()) 
    

# var1 = ToDo('делать домашку') 
# var1.give_priority(1) 
# # print(var1.list_of_tasks())
# var2=ToDo('выгулять собаку') 
# var2.give_priority(2) 
# # print(var2.list_of_tasks())
# var3=ToDo('сходить в кино') 
# var3.give_priority(3)
# print(var3.list_of_tasks())

















































"""================================ task of classroom =============================="""



class Sniper:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp

    def less_hp(self):
        self.hp-=20
global hp1
global hp2
name1=input('Введите имя первого снайпера: ')
hp1=int(input('Введите здоровье первого снайпера: '))
name2=input('Введите имя второго снайпера: ')
hp2=int(input('Введите здоровье второго снайпера: '))
sniper1=Sniper(name1,hp1)
sniper2=Sniper(name2,hp2)
while hp1>0 or hp2>0:
  step=int(input('Выберите какой снайпер атакует, 1 - первый , 2 - второй: '))
  if step==1:
    sniper2.less_hp()
    print(f'Атаковал 1 снайпер, у второго снайпера осталось {sniper2.hp} здоровья')
  elif step==2:
    sniper1.less_hp()
    print(f'Атаковал 2 снайпер, у первого снайпера осталось {sniper1.hp} здоровья')
  elif step!=1 or step!=2:
    print('Неправильно! выберите 1 или 2 ')
    pass
  if sniper2.hp<=0:
    print(f'Выиграл снайпер {sniper1.name}')
    break
  if sniper1.hp<=0:
    print(f'Выиграл снайпер {sniper2.name}')
    break




# class Hogwarts:
#     def __init__(self,courage, intelligence , justice , ambition) :
#         self.courage = courage
#         self.intelligence = intelligence
#         self.justice = justice
#         self.ambition = ambition
#     def sorting_hat(self):
     
#         attributes = {
#         'courage': self.courage,
#         'intelligence': self.intelligence,
#         'justice': self.justice,
#         'ambition': self.ambition
#         }
#         max_value = max(attributes.values())
#         result = [k for k,v in attributes.items() if v == max_value]
#         if 'courage' in result:
#             print(f'Преобладает courage -> Gryffindor')
#         elif 'intelligence' in result:
#             print(f'Преобладает intelligence -> Ravenclaw')
#         elif 'justice' in result:
#             print(f'Преобладает justice -> Hufflepuff')
#         elif 'ambition' in result:
#             print(f'Преобладает ambition -> Slytherin')


# person1 = Hogwarts(int(input('Введите значение Храбрости от 1 до 100:')),int((input('Введите значение Интелекта от 1 до 100: '))),int(input('Введите значение Cправедливости от 1 до 100:')),int(input('Введите значение Амбиции от 1 до 100:'))) 
# person1.sorting_hat()




























