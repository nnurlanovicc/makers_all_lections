"""работа с файлами, модули и пакеты. JSON"""




"""=================работа с файлами==============="""
# open('path/file-name.txt','режим') -> функция которая позволяет открыть файл и работать с ним 


# file1 = open('test.txt')
# print(file1.read())
# file1 = open('test.txt','w')
# file1.write('hello')
# print(file1)



"""===================== режимы ===================="""

# 1. r (read) -> токрывает файл для чтения


# 2. w (write) -> открывает файл для записи, перезаписывает файл, если такого файла нет создает пустой файл


# 3. a (append) -> открывает файл для добавления, все новое добавляется в конец, если такого файла нет то он тоже создаст


# 4. x (exclusive) -> создает файл с уникальным именем, если в директории есть такой файл , то ошибка


# 5. t (text) -> открывает файл в текстовом виде ('rt') == r


# 6. b (binary) -> открывает файл в бинарном виде ('rb') == r    ('wb') == w


# 7. + -> открывает файл в режиме чтения и в режиме записи r+   w+


# file  = open('test.txt', 'r+')
# print(file.read())
# file.write('\nmakers')



# file = open('test.txt', 'r+')
# print(file.read())
# file.seek(0)
# print(file.read())
# file.seek(4)
# print(file.read())
# file.write('\nMakers')
# print(file.tell())
# file.close()


# file.seek(0) -> перемещает курсор в начало файлла
# file.close() -> закрывает файл 
# file.tell() -> возвращает индекс, где находится курсор



"""================== методы режима 'r' ====================="""
# 1. read(index) -> считывает весь файл, если указать считывает до index
# 2. readline(кол-во символов) -> считывает одну строку из файла
# 3. readlines(кол-во символов) ->  считывает построчно и сохраняет  их в виде списка

# file = open('test.txt')
# print(file.read(10))
# file.close()


# file = open('test.txt')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()



# file = open('test.txt')
# print(file.readlines())
# file.close()


"""=================== методы режима 'w' ========================"""
# 1. write('string') -> записывает string в файл 
# 2. writelines(list) -> 

# f = open('test.txt','w')
# f.write('приветб вас беспокоит компание Makers')
# f.write('приветб вас беспокоит компание Makers')
# f.close()


# f = open('test.txt','w')
# f.writelines(['hello world\n','nurs\n','makres\n'])
# f.close()


# ==========контекстный менеджер - открывает файл и при любом раскладе он будет его закрывать

# with open('test.txt','r') as file:
#     data = file.read()
#     print(data)






"""====================== JSON ====================="""
'''
JSON (JavaScript Objekt Notation) -> единый текстовый формат передачи данных между приложениями, 
компютерами и языками программирования
'''



# {
#     "id":1,
#     "email":"nurs@gmail.com",
#     "posts": null
# }

           #разница
#Python                 JSON

# None                   null
# dict                   object
# list                   Array
# str                    String
# int                    Number
# float                  Number
# True                   true
# False                  false

# import json
# print(dir(json))


'''
сериализация и  десериализация
'''

# ===========сериализация -> запись данных в JSON (перевод)

# dump() -> метод записывает объект Python в файл в формате JSON
# dumps() -> метод записывает объект Python в строку JSON 



# ========= десериализация -> чтение данных из json,    перевод 

# load(file) -> метод который считывает файл в формате json и переводит его в объект python
# loads(string) -> метод который считывает текст/строку в формате  json и переводит в объект python


# import json

# person = '{"name": "Sam", "age": 25,"is_working": false}'
# result = json.loads(person)
# print(result)
# print(type(person))
# print(type(result))

# with open('file.json','w+') as file:
#     person = '{"name": "Sam", "age": 25,"is_working": false}'
#     file.write(person)
#     file.seek(0)
#     data = json.load(file)
#     print(data.get('name'))


# data = {
#     'email': 'n@gmail.com',
#     'password': '123214345'
# }

# data_json = json.dumps(data)
# print(type(data_json))


# data = {
#     'email': 'n@gmail.com',
#     'password': '123214345'
# }

# with open('file.json','w+')as file:
#     json.dump(data, file)
#     file.seek(0)
#     print(type(file.read()))













"""=======================file tasks ==============================="""

# task 1
# with open('task1.txt', 'w+') as file:
#     file.writelines(['1', '\n2', '\n3', '\n4', '\n5', '\n6', '\n7', '\n8', '\n9', '\n10'])
#     for line in file.readline(11):
#         print(line)  


# with open('text.txt', 'r') as file:
#     for line in file.readlines(9):
#         print(line)  





# task 2
# with open('task2.txt') as file:
#     for i in file.readlines():
#         print(i)





# task 3
# with open('task3.txt','w+') as file:
#     file.write('0*1*2*3*4*5*6*7*8*9*',)
#     file.seek(0)
#     print(file.read())




# task 4
# with open('task4.txt') as f:
#     print(len(f.readlines(0)))







# task 5
# with open('task5.txt', 'r') as file: 
#     list_ = file.readlines() 
#     list_ = [i.replace('\n', '')for i in list_] 
#     list1 = [] 
#     for x in list_: 
#         x = int(x) 
#         list1.append(x) 
#         mini = min(list1) 
#         maxi = max(list1) 
# with open('task6.txt', 'w') as f: 
#     f.write(f'{mini}-{maxi}')











# task 6
# def read_last(lines, filename): 
#     with open(filename) as file: 
#         list_ = file.readlines() 
#     if lines < len(list_): 
#         i = 0 
#         reversed_list_ = list_[::-1] 
#         while i<lines: 
#             print(reversed_list_[i].replace('\n', '')) 
#             i+=1 
#     else:
#         list_.reverse() 
#         for i in list_: 
#             print(i.replace('\n', '')) 
# read_last(3, 'article.txt')


# def read_last(lines, filename): 
#     with open(filename) as file: 
#         list_ = file.readlines() 
#         list_.reverse() 
#     if len(list_) > lines: 
#         i = 0 
#         while i < lines: 
#             print(list_[i].replace('\n', '')) 
#             i += 1 
#     else: 
#         for i in list_: 
#             print(i.replace('\n', '')) 
# read_last(25, 'article.txt') 









# with open('article.txt') as file:
#     list_ = file.readlines()
#     list1 = []
#     for i in list_:
#         list1.append(i.replace('\n',''))
# from functools import reduce
# list2 = reduce(lambda x,y: x if len(x) > len(y) else y,list1)
# print(list2)


# task 7
# def longest_words(filename: str):
#     with open(filename) as file:
#         list_ = file.readlines()
#     list1 = []
#     for i in list_:
#         list1.append(i.replace('\n',''))
#     from functools import reduce
#     list2 = reduce(lambda x,y: x if len(x) > len(y) else y,list1)
#     print(list2)
# longest_words('article.txt')


# def longest_words(filename:str): 
#     with open(filename,'r') as file: 
#         listData = file.readlines() 
#     listData1=[] 
#     for x in listData: 
#         if '\n' in x: 
#             x = x.replace('\n','') 
#         else: pass 
#         if ' ' in x:
#             var = x.split() 
#             listData1.extend(var) 
#         else: 
#             listData1.append(x) 
#     maximum=[] 
#     for j in listData1: 
#         if len(j)==len(max(listData1,key=len)): 
#             maximum.append(j) 
#         else: 
#             pass 
#         if len(maximum)==1: 
#             print(maximum[0]) 
#         else: 
#             print(maximum) 
# longest_words('article.txt')


# def longest_words(filename: str): 
#     total = [] 
#     with open(filename, 'r') as book: 
#         list_book = book.readlines() 
#     list_book1 = [i.replace('\n', '') for i in list_book] 
#     a = ' '.join(list_book1) 
#     b = a.split() 
#     for i in b: 
#         if len(i) == len(max(b, key = len)): 
#             total.append(i) 
#             if len(total) > 1:
#                 print(total) 
#             else: 
#                 for i in total: 
#                     print(i) 
                
# longest_words('article.txt')



# def longest_words(filename: str):
#     with open(filename, 'r') as file:
#         content = file.read()

#     words = content.split()
#     max_length = max(len(word) for word in words)
#     longest = [word for word in words if len(word) == max_length]

#     return longest

# print(longest_words('article.txt'))








# task 8
# import csv 
# import datetime 
# import time
# filename = 'rows_300.csv' 
# with open(filename, 'w', newline='') as file: 
#     writer = csv.writer(file) 
#     for i in range(1, 301): 
#         now = datetime.datetime.now() 
#         second = now.second 
#         microsecond = now.microsecond 
#         writer.writerow([i, second, microsecond]) 
#         time.sleep(0.01)


# task 9
# import csv 
# def calc_price(filename: str) -> int: 
#     total_price = 0 
#     with open(filename, 'r') as file: 
#         reader = csv.reader(file, delimiter=' ') 
#     for row in reader: 
#         item_price = float(row[1]) * float(row[2]) 
#         total_price += item_price 
#     return float(total_price) 
# filename = 'prices.txt' 
# total_price = calc_price(filename) 
# print(f'Total price:{total_price} rubles')


# task 10
# import csv 
# from typing import Dict, List 
# def read_csv(filename: str) -> Dict[str, List[str]]: 
#     result = {} 
#     with open(filename, 'r') as file: 
#         reader = csv.reader(file) 
#     for row in reader: 
#         key = row[0] 
#         values = row[1:] 
#         result[key] = values 
#     return result 
# result = read_csv('data.csv') 
# print(result)





# task 11
# def filter_text(text_filename: str) -> str: 
#     with open(text_filename) as f: 
#         word = (f.read())
#     word1 = word.lower() 
#     with open('forbidden_words.txt') as f: 
#         forbidden = f.readline().split() 
#         for i in forbidden: 
#             word1 = word1.replace(i, '*' * len(i)) 
#     list_1 = list(word1) 
#     list_ = list(word) 
#     for i in range(0,len(word1)): 
#         if list_1[i] ==list_[i].swapcase(): 
#             list_1[i] = list_[i] 
#             a = ''.join(list_1) 
#     return a 
# filter_text('bad_text.txt')





# task 12
# def bad_students(filename: str): 
#     list_of_bad_students = [] 
#     with open(filename, 'r') as file: 
#         students = file.read().split('\n') 
#     students_list = [i.split() for i in students] 
#     for i in students_list: 
#         if int(i[2]) < 4: 
#             list_of_bad_students.append(i[1]) 
#     return list_of_bad_students 
# filename = 'students.txt' 
# print(bad_students(filename))









# task 13
# def reverse_file_print(filename: str) -> None: 
#     with open(filename) as file: 
#         list_ = file.readlines() 
#     list_ = [x[::-1] for x in list_] 
#     list_rev = '\n'.join(list_) 
#     print(list_rev) 
# filename = 'zen_of_python.txt' 
# print(reverse_file_print(filename))

























































































































"""=====================json tasks=================="""

# task 1
# import json 

# with open('task1.json') as file1:
#     python_obj = json.loads(file1.read()) 

# with open('task1.py', 'w') as file2: 
#     file2.write(str(python_obj))




# task 2
# import json 

# with open('task2.json', 'r') as f: 
#     json_obj = f.read() 
#     python_obj = json.loads(json_obj)



# task 3
# import json 
# python_obj = None 
# json_obj = json.dumps(python_obj) 
# print(json_obj)




# task 4
# import json 
# json_obj = "null" 
# python_obj = json.loads(json_obj) 
# print(python_obj)




# task 5
# import json 

# users = [ { 'name': 'John', 'last_name': 'Snow', 'age': 26, 'has_car': True,}, 
#           { 'name': 'Sam', 'last_name': 'Bolt', 'age': 4, 'has_car': False, } ] 
# json_users = json.dumps(users) 
# print(json_users)



# task 6
# import json

# json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]'

# py_obj = json.loads(json_products)
# for i in py_obj:
#     if i['rating'] > 4:
#         print(i['title'])





# task 7
# import json 
# with open('db.json') as file: 
#     dict_ = json.load(file) 
# for product in dict_: 
#     product["description"] = "..." 
# js_dict = json.dumps(dict_) 
# with open('new_db.json', 'w') as f1: 
#     f1.write(js_dict)




# task 8
# import json 
# with open('db.json') as file: 
#     list_ = json.load(file) 
# for product in list_: 
#     for k in product.keys(): 
#         if product[k] == 3: 
#             list_.remove(product) 
# js_dict = json.dumps(list_) 
# with open('new_db.json', 'w') as f1: 
#     f1.write(js_dict)




# task 9
# import json 

# def create_new(id: int, title: str, description: str, price: int, rating:float) -> None: 
#     dict_={'id':id, 'title':title, 'description':description, 'price':price, 'rating':rating} 
#     with open('db.json') as file: 
#         res = json.load(file) 
#         res.append(dict_) 
#     with open('new_db.json', 'w') as f: 
#         f.write(json.dumps(res)) 

# create_new(10, 'assa', 'asd', 12, 25.0)







# task 10
# import json 
# from typing import List 

# def get_sorted(json_filename: str) -> List[dict]: 
#     with open(f'{json_filename}') as file: 
#         products = json.load(file) 
#         sorts = sorted(products, key=lambda x: x['rating'], reverse=True) 
#     return sorts




# task 11
# import json

# def update(id: int, title: str=None, price: int=None, rating: float=None) -> None:
#     ls_key = ['title', 'price', 'rating'] 
#     ls_val = [title, price, rating] 
#     with open('db.json') as file: 
#         pyth_dict = json.load(file) 
#     key_list = list(filter(lambda x: x if x['id'] == id else None, pyth_dict)) 
#     if not key_list: 
#         raise ValueError('Нет такого ключа') 
#     else: 
#         for dict_ in pyth_dict: 
#             for key, val in zip(ls_key, ls_val): 
#                 if val is not None: 
#                     dict_[key] = val 
#     with open('new_db.json', 'w') as file: 
#         json.dump(pyth_dict, file, indent=4)







# task 12
# import json 
# def search(name: str): 
#     with open('db.json') as file: 
#         python_list = json.load(file) 
#     list_ = [] 
#     for k in python_list: 
#         if name in k['title']: 
#             list_.append(k) 
#     return list_ 
# print(search('sus'))




# task 13
# import json 

# def filter_by_price(price: int): 
#     with open('db.json') as file: 
#         python_list = json.load(file) 
#     list_ = [] 
#     for i in python_list: 
#         if i["price"] >= price: 
#             list_.append(i) 
#     return list_ 
# print(filter_by_price(1000))





# task 14
# import json 

# def bulk_create(products): 
#     with open('db.json') as f: 
#         old = json.load(f) 
#     id_ = [i['id'] for i in old] 
#     for el in products: 
#         if el['id'] not in id_: 
#             old.append(el) 
#     with open('new_db.json', 'w') as f2: 
#         json.dump(old, f2)
# bulk_create([{'id': 100, 'title': 'product1', 'price': 1500, 'rating': 4.6}])
















"""========================= classroom tasks ==============================="""

# # Создание файла numbers.txt и запись чисел от 1 до 20
# with open("numbers.txt", "w") as file:
#     for num in range(1, 21):
#         file.write(str(num) + "\n")
    

# # Считывание чисел из файла numbers.txt и запись их квадратов в squares.txt
# with open("numbers.txt", "r") as numbers_file, open("squares.txt", "w") as squares_file:
#     for i in numbers_file:
#         number = int(i.strip())
#         square = number ** 2
#         squares_file.write(str(square) + "\n")








# # Открытие файла usernames.txt в режиме записи
# with open("usernames.txt", "w") as file:
#     while True:
#         username = input("Введите имя (или 'End' для завершения): ")
#         if username == "End":
#             break
        
#         # Запись имени и количества букв в файл
#         file.write(f"{username}: {len(username)}\n")
