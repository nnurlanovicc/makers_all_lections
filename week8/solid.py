'''
===========================================SRP============================
===============================как не стоить делать
'''

# class ExportCSV:

#     def __init__(self,data):
#         self.data = self.prepare(data)

#     def prepare(self,data):
#         result = ''
#         for item in data:
#             new_line = ','.join(
#                 [
#                 item['name'],
#                 item['surname'],
#                 item['profession']
#                 ]
#             )
#             result += f"{new_line}\n"
#         return result

#     def write_file(self,filename):
#         with open(filename,'w') as file:
#             file.write(self.data)

# data = [
#     {
#         'name': 'sam',
#         'surname': 'brown',
#         'profession': 'detective'
#     },
#     {   'name': 'john',
#         'surname': 'black',
#         'profession': 'doctor'

#     }
# ]

# exporter = ExportCSV(data)
# exporter.write_file('data.csv')




'''
соблюдение SRP
====================================как стоит делать:
'''

class FormatData:
    def __init__(self,data):
        self.data = data

    def prepare(self):
        result = ''
        for item in self.data:
            new_line = ','.join(
                [
                item['name'],
                item['surname'],
                item['profession']
                ]
            )
            result += f"{new_line}\n"
        return result  



class ExportCSV:

    def __init__(self,filename):
        self.filename = filename

    def write(self,data):
        with open(self.filename,'w') as file:
            file.write(data)

data = [
    {
        'name': 'sam',
        'surname': 'brown',
        'profession': 'detective'
    },
    {   'name': 'john',
        'surname': 'black',
        'profession': 'doctor'

    }
]


# data_obj = FormatData(data)
# formated_data = data_obj.prepare()
# # print(formated_data)

# writer = ExportCSV('data.csv')
# writer.write(formated_data)






'''
OCP
не стоит так делать
'''
# import time
# class Logger:
#     def __init__(self):
#         self.format = '%Y-%m-%d  %H:%M:%S'

#     def log(self,message):
#         current_time = time.localtime()
#         print(time.strftime(self.format,current_time),message)



# l = Logger()
# l.log('Error')




'''
надо делать вот так вот, понятноооо
'''
# import time
# class Logger:
#     def __init__(self):
#         self.format = '%Y-%m-%d  %H:%M:%S'

#     def log(self,message):
#         current_time = time.localtime()
#         print(time.strftime(self.format,current_time),message)

# class CustomLogger(Logger):
#     def __init__(self):
#         self.format = '%Y-%m-%d'

# l = Logger()
# l.log('Error')
# cl = CustomLogger()
# cl.log('Error Error Error')



from enum import Enum

'''
так не стоит делать
'''
# class Product(Enum):
#     SHIRT = 1
#     PANT = 2 
#     TSHIRT = 3

# class DiscountCalculator:

#     def __init__(self,product_type,cost):
#         self.product_type = product_type
#         self.cost = cost

#     def get_discount_price(self):
#         if self.product_type == Product.SHIRT:
#             return self.cost - (self.cost * 0.10)
#         elif self.product_type == Product.PANT:
#             return self.cost - (self.cost * 0.15)
#         elif self.product_type == Product.PANT:
#             return self.cost - (self.cost * 0.25)
        


'''
вот так вооот крч
'''

# from abc import ABC, abstractmethod

# class DiscountCalculator(ABC):

#     @abstractmethod
#     def get_discount_price(self):
#         pass


# class DiscountCalcShirt(DiscountCalculator):
#     def __init__(self,cost):
#         self.cost = cost

#     def get_discount_price(self):
#         return self.cost - (self.cost * 0.10)


# class DiscountCalcTshirt(DiscountCalculator):
#     def __init__(self,cost):
#         self.cost = cost

#     def get_discount_price(self):
#         return self.cost - (self.cost * 0.25)
    
# class DiscountCalcPant(DiscountCalculator):
#     def __init__(self,cost):
#         self.cost = cost

#     def get_discount_price(self):
#         return self.cost - (self.cost * 0.15)






'''
LSP
так не стоит 
'''

# class Animal:
#     def __init__(self,attrs):
#         self.attributes = attrs

#     def eat(self):
#         print('Ate some food')


# class Cat(Animal):
#     def eat(self,amount=100):
#         if amount > 300:
#             print('too much')
#         else:
#             print('ate some cat food')

# class Dog(Animal):
#     def eat(self):
#         print('eat some dog food')


# cat1 = Cat({'name': 'Mur', 'age': 3})
# dog1 = Dog({'name': 'rex', 'age': 4})
# cat2 = Cat(('barsik',2))


# animals = [cat1,cat2,dog1]
# for animal in animals:
#     print(animal.attributes['age'])
    




''''
djn nfr rhx
'''
# class Animal:
#     def __init__(self,name,age):
#         self.attributes = {'name': name, 'age': age}

#     def eat(self,_amount=0):
#         print('eat')

# class Cat(Animal):
#     def __init__(self,name,age):
#         super().__init__(name,age)

#     def eat(self,amount=100):
#         if amount > 300:
#             print('too much')
#         else:
#             print('ate some cat food')

# class Dog(Animal):
#     def __init__(self,name,age):
#         super().__init__(name,age)   
    
#     def eat(self,_amount=0):
#         print('dogs food')

# cat = Cat('mur',4)
# dog = Dog('bars',6)

# animals = [cat,dog]
# for animal in animals:
#     print(animal.attributes['age'])





'''

не так
'''

# class Creature:
#     def __init__(self,name):
#         self.name = name

#     def swim(self):
#         pass

#     def walk(self):
#         pass

#     def fly(self):
#         pass

#     def talk(self):
#         pass

# class Human(Creature):
#     def swim(self):
#         print('i can swim')

#     def walk(self):
#         print('i can walk')

#     def talk(self):
#         print('i can talk')

# class Fish(Creature):
#     def swim(self):
#         print('i can swim')

#     def fly(self):
#         print('i can fly')

# fish = Fish('')
# fish.talk()

# human = Human('jackie')
# human.fly()




'''
ISP
так
'''

# class Creature:
#     def __init__(self,name):
#         self.name = name


# class Swimmer:
#     def swim(self):
#         pass


# class Walker:
#     def walk(self):
#         pass
#     def run(self):
#         pass


# class Talker:
#     def talk(self):
#         pass
#     def skrim(self):
#         pass



# class Human(Creature,Walker,Swimmer,Talker):
#   ...




# DIP

# class TerminalWriter:
#     def write(self, msg):
#         print(msg)


# class FileWriter:
#     def write(self, msg):
#         with open('log.txt', 'w') as file:
#             file.write(msg)

# import time

# class Logger:
#     def __init__(self):
#         self.prefix = time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())
    
#     def log_str(self, message):
#         TerminalWriter().write(message)

#     def log_file(self, message):
#         FileWriter().write(message)

# logger = Logger()
# logger.log_file('hello')
# logger.log_str('test')






from abc import ABC, abstractmethod

class Writer(ABC):
    
    @abstractmethod
    def write(self, msg):
        pass

class DataBaseWriter(Writer):
    def writdde(self, msg):
        db = ...
  
class TerminalWriter(Writer):
    def write(self, msg):
        print(msg)


class FileWriter(Writer):
    def write(self, msg):
        with open('log.txt', 'w') as file:
            file.write(msg)

import time

class Logger:
    def __init__(self):
        self.format = '%Y-%m-%d:%H:%M:%S'

    def log(self, message, class_):
        prefix = time.strftime(self.format, time.localtime())
        class_().write(message)


logger = Logger()
logger.log('Error', FileWriter)
logger.log('Error', TerminalWriter)