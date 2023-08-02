# class Car:
#     def __init__(self,model):
#         self.__model = model

#     model = property(lambda self: self.__model)

# bmw = Car('BMW')
# print(bmw.model)



# class Circle:
#     def __init__(self,radius):
#         self.__radius = radius


#     @property
#     def radius(self):
#         print('getter')
#         return self.__radius
#     @radius.setter
#     def radius(self,new_radius):
#         print('setter')
#         if not isinstance(new_radius,(int,float)):
#             raise ValueError('Invalid radius')
#         self.__radius = new_radius

#     @radius.deleter
#     def radius(self):
#         print('deleter')
#         del self.__radius

# circle = Circle(10)
# circle.radius = 9
# print(circle.radius)
# del circle.radius
# print(circle.radius)


#     def get_radius(self):
#         print('getter')
#         return self.__radius
    
#     def set_radius(self, new_radius):
#         print('setter')
#         if not isinstance(new_radius,(int,float)):
#             raise ValueError('Invalid radius')
#         self.__radius = new_radius

#     radius = property(get_radius, set_radius)

# circle = Circle(10)
# print(circle.radius)


"""
1.Создайте класс PrivateProject. Внутри этого класса есть приватные атрибуты класса: github_link и developers.
В github_link хранится ссылка на проект (любая), а в developers хранится список с юзернеймами, 
у которых есть доступ к этой ссылке (атрибуту github_link).
Создайте объект класса PrivateProject, при создании необходимо передать в качестве аргумента username.
Далее, попытайтесь через созданный объект класса получить атрибут github_link. 
При этом, если данный username есть в списке developers, ему открыт доступ к ссылке.
В противном случае выводится сообщение: Forbidden. Список developers должен быть скрыт.
"""





# class PrivateProject:

#     def __init__(self,username):
#         self.username = username

#     __github_link = 'ссылка на проект'
#     __developers = ['nurs','jeckie chan','baby','moto moto']

#     @property
#     def link(self):
#         if self.username in self.__developers:
#             return self.__github_link
#         else:
#             raise ValueError('Forbidden')
        
# a = PrivateProject('nurs')
# print(a.link)






"""
2.Создайте класс User. В этом классе есть защищенный метод _create_user, который принимает email и password. 
Этот метод вызывается в публичных методах create_user и create_superuser. 
Оба метода отличаются друг от друга тем, что в методе create_user атрибут is_superuser имеет значение False, 
а в методе create_superuser - True.
Также в классе есть метод admin_login, который принимает password.
Создайте два объекта от класса User. К первому объекту примените метод create_superuser, а ко второму - create_user. 
Далее у обоих объектов вызовите метод admin_login, передав правильные пароли.
У первого объекта должно выдаваться сообщение Successfully logged in, а у второго - Forbidden, 
так как поле is_superuser у второго объекта имеет значение False. Также если даже is_superuser у первого объекта True, 
ему не удасться залогиниться, 
если он передал неправильный пароль password в метод admin_login и ему выдается сообщение: Invalid password.
"""



# class User:
#     def _create_user(self,email,password):
#         self.email = email
#         self.__password = password

#     def create_user(self,email,password):
#         self.is_superuser = False
#         self._create_user(email,password)


#     def create_superuser(self,email,password):
#         self.is_superuser = True
#         self._create_user(email,password)

#     def admin_login(self,password):
#         if self.is_superuser == True:
#             if password != self.__password:
#                 raise Exception('Invalid password')
#             print('Successfully logged in')
#         else:
#             print('Forbidden')

# user1 = User()
# user1.create_user('nurs@gmail.com','1234')
# user2 = User()
# user2.create_superuser('nursultan@gmail.com','12345678')
# user2.admin_login('1234')
# user2.admin_login('12345678')






"""============================= task ============================="""



# task 1

# class A:
#     def public(self):
#         return 'Public method'

#     def _protected(self):
#         return 'Protected method'

#     def __private(self):
#         return 'Private method'

# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())


# task 3

# class Car:
#     def __init__(self):
#         self.__speed = 0

#     def set_speed(self, new):
#         self.__speed = new

#     def show_speed(self):
#         return self.__speed
    
# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed()) 




# task 4
# class Car:
#     def __init__(self):
#         self.__speed = 0

#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self, new):
#         self.__speed = new

    
# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed) 



# task 5
# class Person: 
#     name = "John" 
#     _phone_number = "+996 557 55 17 57" 
#     __card_number = "9999 9999 9999 9999" 
#     @property 
#     def number(self): 
#         return self.__card_number 
    
# john = Person() 
# print(john.name) 
# print(john._phone_number) 
# print(john.number)


# task 6
# class Person: 
#     def __init__(self, name, phone_number, card_number) -> None: 
#         self.name = name 
#         self._phone_number = phone_number 
#         self.__card_number = card_number 
        
#     @property 
#     def number(self): 
#         return self.__card_number 
    
# john = Person("John", "+996 557 55 17 57", "9999 9999 9999 9999") 
# print(john.name) 
# print(john._phone_number) 
# print(john.number)





# task 7
# class Person: 
#     name = "John" 
#     _phone_number = "+996 557 55 17 57" 
#     __card_number = "9999 9999 9999 9999" 
    
#     def get_number(self): 
#         return self.__card_number 
    
#     def set_number(self): 
#         self.__card_number = None 
#         return self.__card_number 
    
# john = Person() 
# john.name = None 
# john._phone_number = None 
# print(john.name) 
# print(john._phone_number) 
# print(john.set_number())


# task8

class Person:
    def __init__(self, name, phone_number, card_number):
        self.name = self.__validate_name(name)
        self._phone_number = phone_number
        self.__card_number = card_number

    def __validate_name(self,name):
        if len(name) < 2:
            return 'John'
        return name.title()
    
    def get_card_number(self): 
        return self.__card_number
    
sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
print(sam.name)
print(sam._phone_number)
print(sam.get_card_number())

class Person:
    def __init__(self, name, phone_number, card_number):
        self.name = self.__validate_name(name)
        self._phone_number = phone_number
        self.__card_number = card_number

    def __validate_name(self, name):
        if len(name) <  2:
            return "John"
        else:
            return name.title()

    def get_card_number(self):
        return self.__card_number
    
sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
print(sam.name)
print(sam._phone_number)
print(sam.get_card_number())

