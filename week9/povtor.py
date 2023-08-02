'''
Задание 7
Напишите класс Game, с помощью которого можно создать объекты-игры, у объектов должны быть атрибуты:

type_ - тип игры
name - название игры,
extensions соответсвующий пустому списку - [].
У класса должны быть методы:

get_description, который принимает строку и возвращает описание к игре в виде названия игры и переданной строки:
Minecraft это инди-игра в жанре песочницы с элементами выживания и открытым миром. 
Где Minecraft - это название игры, берется из атрибута name объекта.

get_extensions, который возвращает все подключенные расширения в виде строки разделенной пробелами, если же список extensions пуст, возвращайте сообщение:
Нет подключенных расширений   


Также напишите миксин ExtensionMixin, чтобы к игре можно было подключать расширения.

У миксина должно быть два метода:

add_extension, принимающий строку-название и добавляющий ее в список игры, также должен возвратить сообщение:

Добавлено новое расширение Multiverse-Core для игры Minecraft. 

где Multiverse-Core это строка - название расширения

remove_extension, удаляющий расширение по названию, и возращающий строку в формате:
Multiverse-Core был отключен от Minecraft. 
Если же такого расширения нет в списке должна возвращаться строка:

Такого расширения нет в списке.
'''

# class ExtensionMixin:

#     def add_extension(self, title):
#         self.extensions.append(title)
#         return f'Добавлено новое расширение {title} для игры {self.name}'
    
#     def remove_extension(self, title):
#         if title in self.extensions:
#             self.extensions.remove(title)
#             return f'{title} был отключен от {self.name}'
        
#         return 'Такого расширения нет в списке.'
    

# class Game(ExtensionMixin):
#     def __init__(self, type_, name):
#         self.type_ = type_
#         self.name = name
#         self.extensions = []

#     def get_description(self, description):
#         return f'{self.name} это {description}'
    
#     def get_extensions(self):
#         if self.extensions:
#             return ' '.join(self.extensions)
#         return 'Нет подключенных расширений'
    


'''
Задание 8
Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:

В начале, проверьте, что пароль состоит из минимум 8 символов, но меньше 15, если условие не соблюдено, должны выйти ошибка с текстом:
Password should be longer than 8, and less than 15
Вторая проверка должна проверять что пароль содержит цифры, и в случае отсутствия цифр, выводить ошибку с текстом:
Password should contain numbers too
Третья проверка, проверяет содержит ли пароль буквы и в случае не совпадения, выводит ошибку с текстом:
Password should contain letters as well
В конце проверьте, содержит ли пароль хотя бы один из символов: '@', '#', '&', '$', '%', '!', '~', '*', если условие не выполнено выводите ошибку с текстом:
Your password should have some symbols
если одно из условий не выполнено, выводите соответствующее исключение, если же все условия выполнены метод validate должен возвращать строку:

Ваш пароль сохранен.
Также переопределите метод __str__, чтобы при попытке распечатать сам пароль, вам выдавалась строка из звездочек количество которых равно длине пароля.

К примеру, если пароль joe@123456, при попытке распечатать пароль, в терминал должно выводиться: **********

пишите код для проверки пароля в указанном порядке
'''

class Password:
    def __init__(self, password):
        self.password = password

    def validate(self):
        if not 15 > len(self.password) > 8:
            raise Exception('Password should be longer than 8, and less than 15')
        
        nums_contain = False
        letters_contain = False
        specials_contain = False

        specials = ('@', '#', '&', '$', '%', '!', '~', '*')

        for symbol in self.password:
            if symbol.isdigit():
                nums_contain = True
            if symbol.isalpha():
                letters_contain = True
            if symbol in specials:
                specials_contain = True
        
        if not nums_contain:
            raise Exception('Password should contain numbers too')
        if not letters_contain:
            raise Exception('Password should contain letters as well')
        if not specials_contain:
            raise Exception('Your password should have some symbols')
        
        return 'Ваш пароль сохранен.'
    
    def __str__(self):
        return len(self.password) * '*'