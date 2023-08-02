

# count = 0

# def counter():
#     global count
#     count += 1
#     return count


# name = input()
# age = input()
# print({'id': counter(), 'name': name, 'age': age})

# name = input()
# age = input()
# print({'id': counter(), 'name': name, 'age': age})

# name = input()
# age = input()
# print({'id': counter(), 'name': name, 'age': age})












































# database = [
#     {'username': 'RobStark', 'password': hash('1234test')},
#     {'username': 'JhonSnow', 'password': hash('19283746')},
#     {'username':'SansaStark', 'password': hash('87654321')}
# ]

# def in_database(username: str) -> bool:
#     for user in database:
#         if user['username'] == username:
#             return True
#     return False

# def get_user(username: str, password: str) -> dict:
#     if not in_database(username):
#         raise Exception('user is not found')
#     for user in database:
#         if user['username'] == username:
#             if user['password'] != hash(password):
#                 raise Exception('password is wrong')
#             else:
#                 return user

# def register(username: str, password: str, password_confirm: str) -> str:
#     if in_database(username):
#         raise Exception('name is not free')
#     if password != password_confirm:
#         raise Exception('passwords is not same')
#     new_user = {'username': username, 'password': hash(password)}
#     database.append(new_user)
#     return 'you signed up'


# def login(username: str, password: str) -> str:
#     get_user(username, password)
#     return 'you log in your account'


# def change_password(username, password):
#     user = get_user(username, password)
#     new_password = input('enter the new password: ')
#     index = database.index(user)
#     user_from_db = database[index]
#     user_from_db['password'] = hash(new_password)
#     return 'password updated'


# def delete_account(username: str, password: str):
#     user = get_user(username, password)
#     database.remove(user)
#     return 'account deleted'





# print(register('nurs','234565432','234565432'))
# print(login('nurs','234565432'))
# print(change_password('nurs','234565432'))
# print(delete_account('nurs','234565432'))

















































"""
- 🤖 ****Необходимо использовать эти технологии (stack):****
    - Back-End
        - [Python](https://www.python.org/)
- 🫀 **CRUD**
    
    Вам нужно реализовать функционал CRUD курса. 
    
    При создании курса Пользователь должен заполнить следующие поля:
    
    - Категория - ограничить выбор категории из следующих:
        - Веб-разработка
        - Разработка мобильных приложений
        - Разработка игр
    - Подкатегория - ограничить выбор подкатегории из следующих:
        - Python
        - JavaScript
        - Java
    - Заголовок курса (максимум 60 символов)
    - Описание к курсу (минимум 10 слов)
    - Уровень - ограничить выбор уровня из следующих:
        - начальный
        - средний
        - профессиональный
    - Цена курса  - все суммы конвертировать в сомы
        - валюта
        - сумма
- ⏳ **Deadline**
    
    На реализацию данного функционала вам дается 1 день.
    
- **😊 За вдохновением (Пример)**
    
    [Online Courses - Learn Anything, On Your Schedule | Udemy](https://www.udemy.com/)
"""




'''
Вам нужно реализовать функционал CRUD курса. 

При создании курса Пользователь должен заполнить следующие поля:

- Категория - ограничить выбор категории из следующих:
    - Веб-разработка
    - Разработка мобильных приложений
    - Разработка игр
- Подкатегория - ограничить выбор подкатегории из следующих:
    - Python
    - JavaScript
    - Java
- Заголовок курса (максимум 60 символов)
- Описание к курсу (минимум 10 слов)
- Уровень - ограничить выбор уровня из следующих:
    - начальный
    - средний
    - профессиональный
- Цена курса  - все суммы конвертировать в сомы
    - валюта
    - сумма
'''

# categories = [
#     'веб-разработка',
#     'разработка мобильных приложений',
#     'разработка игр'
# ]

# subcategories = [
#     'python',
#     'javaScript',
#     'java'
# ]

# levels = [
#     'начальный',
#     'средний',
#     'профессиональный'
# ]
# id = 0
# def get_id():
#     def inner():
#         global id
#         id += 1
#     inner()
#     return id


# db = {
#     get_id(): {
#         'category': 'веб-разработка',
#         'subcategory': 'python',
#         'level': 'начальный',
#         'tilte': 'Веб-разработка для начинающих',
#         'description': 'Эффективные модели и практики организации профориентационной и научно-исследовательской работы с детьми с применением современных технологий',
#         'price': {'currency': 'сом', 'sum': 5000}
#     }
# }

# def get_courses():
#     return db

# def get_course(id: int) -> dict:
#     course = db.get(id)
#     if course:
#         return course
#     else:
#         raise Exception('Такого курса нет')
    

# Create Read Update Delete
# def validate_date(data):
#     if data['id']


# def create_course():
#     new_course = {
#         get_id(): {
#             'category': input(f'Выберите категорию {categories}: '),
#             'subcategory': input(f'Выберите подкатегорию {subcategories}: '),
#             'level': input(f'Выберите уровень курса {levels}: '),
#             'title': input('Введите название курса: '),
#             'description': input('Введите описание курса: '),
#             'price': {'currency': input('Выберите валюту (cом/dollar): '), 'sum': float(input('Введите стоимость курса: '))}
#         }
#     }

    # print(new_course)
    # if new_course['id']['categoryh'] 


# create_course()









