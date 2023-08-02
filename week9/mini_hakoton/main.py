"""
3.1 Класс Database:

Метод init(): Инициализация базы данных и соединение с JSON.

Метод create(): Создание новой записи в базе данных.

Метод read(): Получение данных из базы данных по определенным критериям (например, все записи или по идентификатору).

Метод update(): Обновление существующих записей в базе данных.

Метод delete(): Удаление записей из базы данных.

Метод close(): Закрытие соединения с базой данных.

"""


# import json


# class Database:
#     def __init__(self,database: dict):
#         self.database = database
#         with open('phones.json','w+') as file:
#             data_json = json.dumps(str(database))
#             file.write(data_json)


#     def create(self,name,memory,color):
#         self.database['name'] = name
#         self.database['memory'] = memory
#         self.database['color'] = color
#         with open('phones.json','w+') as file:
#             data_json = json.dumps(str(self.database))
#             file.write(data_json + '\n')

#     def update(self,name, memory,color):
#         self.database['name'] = name
#         self.database['memory'] = memory
#         self.database['color'] = color
#         with open('phones.json','a') as file:
#             data_json = json.dumps(str(self.database))
#             file.seek(0)
#             file.write(data_json)

#     def delete(self):
#         with open('phones.json','w') as file:
#             data_json = {}
#             file.write(data_json)






#     def read(self):
#         with open('phones.json','r') as file:
#             json_obj = file.read()
#             py_obj = json.loads(json_obj)
#             print(py_obj)


# a = {'name':'iPhone 7','memory': 128,'color':'red'}
# b = Database(a)


# # b.read()
# b.create('iphone 5',64,'black')
# b.read()
# b.update('sumsung s21',256,'white')
# b.read()




import json

class Database:
    def __init__(self, file_path):
        self.file_path = file_path
        self.connection = None
        self.connect()

    def connect(self):
        self.connection = open(self.file_path, 'r+')

    def create(self, data):
        self.connection.seek(0)
        records = json.load(self.connection)
        records.append(data)
        self.connection.seek(0)
        json.dump(records, self.connection, indent=4)
        self.connection.truncate()

    def read(self, criteria=None):
        self.connection.seek(0)
        records = json.load(self.connection)
        if criteria is None:
            return records
        else:
            filtered_records = [record for record in records if all(item in record.items() for item in criteria.items())]
            return filtered_records

    def update(self, criteria, new_data):
        self.connection.seek(0)
        records = json.load(self.connection)
        for record in records:
            if all(item in record.items() for item in criteria.items()):
                record.update(new_data)
        self.connection.seek(0)
        json.dump(records, self.connection, indent=4)
        self.connection.truncate()

    def delete(self, criteria):
        self.connection.seek(0)
        records = json.load(self.connection)
        records = [record for record in records if not all(item in record.items() for item in criteria.items())]
        self.connection.seek(0)
        json.dump(records, self.connection, indent=4)
        self.connection.truncate()

    def close(self):
        self.connection.close()



class Model:
    def __init__(self, data):
        self.data = data

    def validate(self):
        # Добавьте здесь код для валидации данных модели, если необходимо
        pass





class View:
    @staticmethod
    def display_records(records):
        for record in records:
            print(record)





class Controller:
    def __init__(self, db):
        self.db = db

    def create_record(self, data):
        self.db.create(data)

    def read_records(self, criteria=None):
        return self.db.read(criteria)

    def update_records(self, criteria, new_data):
        self.db.update(criteria, new_data)

    def delete_records(self, criteria):
        self.db.delete(criteria)




def run_tests():
    # Инициализация базы данных и создание объектов
    db = Database('data.json')
    controller = Controller(db)

    # Создание записей
    record1 = {"id": 1, "name": "John Doe", "age": 30}
    record2 = {"id": 2, "name": "Jane Smith", "age": 25}
    controller.create_record(record1)
    controller.create_record(record2)

    # Проверка чтения всех записей
    all_records = controller.read_records()
    View.display_records(all_records)

    # Проверка чтения записей по критериям
    filtered_records = controller.read_records({"name": "John Doe"})
    View.display_records(filtered_records)

    # Обновление записи
    controller.update_records({"name": "John Doe"}, {"age": 31})
    updated_records = controller.read_records({"name": "John Doe"})
    View.display_records(updated_records)

    # Удаление записи
    controller.delete_records({"name": "Jane Smith"})
    remaining_records = controller.read_records()
    View.display_records(remaining_records)

    # Закрытие соединения с базой данных
    db.close()

# Запуск тестов
run_tests()

