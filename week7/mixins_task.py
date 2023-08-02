# 1
"""
Создайте программу по следующему описанию. Создайте
родительские классы: Smartphone и Watch. От этих классов
создайте дочерний класс Smartwatch. В родительских классах
должны быть методы: в Smartphone - метод call, который должен
звонить на определенный номер, и в Watch - метод see_time, который выдает вам реальное время на данный момент.
Создайте объект от класса SmartWatch и вызовите оба метода.
Также в обоих родительских классах должен быть реализован
метод where_to_wear, который говорит вам, где нужно носить
данный гаджет. В классе Smartphone он выдает вам строку “You
can keep me anywhere”, а в классе Watch - строку “You should
wear me on your hand”. Данный метод наследуется и в дочернем
классе, и должен выдавать вам строку “You should wear me on
your hand”. Вызовите и этот метод у объекта класса Smartwatch.
"""




# class Smartphone:
#     def call(self,number: str):
#         print(f"calling: {number}")

#     def where_to_wear(self):
#         print('You can keep me anywhere')


# import datetime
# class Watch:
#     def see_time(self):
#         time = datetime.datetime.now()
#         print(f"it is {time.time()} o'clock")

#     def where_to_wear(self):
#         print('You should wear me on your hand')
    

# class Smartwatch(Watch,Smartphone):
#     pass

# obj = Smartwatch()
# obj.call('0708144474')
# obj.see_time()
# obj.where_to_wear()













"""
Создайте программу по следующему описанию. Есть классы:
Instagram, TikTok. Когда вы создаете объекты от этих классов, то
вам необходимо указать в аргументах username и пароль, таким
образом вы регистрируетесь в каждой из соцсети. Далее в
классе Instagram есть метод post_post, который будет принимать
в качестве аргументов название поста, username и пароль
вашего пользователя. Если пароль и пользователь указаны
верно, то вам выдается сообщение: “Successfully created”.
Аналогично с классом TikTok: метод post_video, принимает
название видео, username и пароль, при верном вводе выдается
сообщение “Successfully created”. При создании поста или же
видео, у вашего юзера должно увеличиться количество постов в
одной из соцсети в зависимости от того, где вы его
опубликовали. Создайте миксин, который будет проверять верны
ли пароль и username пользователя при попытке создания поста
или видео.
"""







# class Check:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password

#     def check_user(self,username,password):
#         if self.username == username and self.password == password:
#             return True
#         else:
#             return False

        

# class Instagram(Check):

#     count_post = 0

#     def post_post(self,username,password):
#         if self.check_user(username,password) is True:
#             self.count_post += 1
#             print('Successfully created')
#         else:
#             print('не стоит температурить бэйбии')

# user_inst = Instagram('nurs','1234')
# user_inst.post_post('nurs','1234')
# print(user_inst.count_post)



# class TikTok(Check):

#     count_video = 0

#     def post_video(self,username,password):
#         if self.check_user(username,password) is True:
#             self.count_video += 1
#             print('Successfully created')
#         else:
#             print('не стоит температурить бэйбии')

# user_tt = TikTok('Azi','5678')
# user_tt.post_video('Azi','5678')
# print(user_tt.count_video)










"""========================== task on platform =========================="""

# 3
# import datetime
# class Clock:
#     def current_time(self):
#         time = datetime.datetime.today().strftime("%H:%M:%S")
#         print(time)
    
# class Alarm:

#     def on(self):
#         print('Будильник включен')

#     def off(self):
#             print('Будильник выключен')


# class AlarmClock(Clock,Alarm):

#     def alarm_on(self):
#         return Alarm.on(self)
    
# clock = AlarmClock()
# clock.current_time()
# # clock.on()
# # clock.off()
# clock.alarm_on()







# 4
# from abc import ABC,abstractmethod 
# class Coder:
    
#     count_code_time = 0
    


#     def get_info(self):
#         pass

#     def coding(self):
#         pass

# class Backend(Coder):
#     def __init__(self, experience,languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend
#         # self.name = name
    
#     def coding(self,coding_time: int):
#         self.count_code_time += coding_time

#     def get_info(self):
#         print(f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование")

        


# class Frontend(Coder):
#     def __init__(self, experience,languages_frontend):
#         self.experience = experience
#         self.languages_frontend = languages_frontend
#         # self.name = name

#     def coding(self,coding_time: int):
#         self.count_code_time += coding_time   

#     def get_info(self):
#         print(f"{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование")

    

# class Fullstack(Backend,Frontend):
#     def __init__(self, experience, languages_backend,languages_frontend):
#         self.experience = experience
#         self.languages_backend = languages_backend
#         self.languages_frontend = languages_frontend
#         # self.name = name

#     def coding(self,coding_time: int):
#         self.count_code_time += coding_time  

#     def get_info(self):
#         print(f"{self.languages_backend} and {self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование ")

# a = Backend('Junior','Python')
# b = Frontend('Middle','Javascript')
# c = Fullstack('Senior','Python','JS')

# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 

