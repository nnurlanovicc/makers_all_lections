
'''
Введение в PostgreSQL. Создание БД, таблиц
'''

# PostgreSQL -> система управления базами данных (СУБД) Набор программ, позволяющй управлять юазами данных и манипулировать данными (создание бд, таблиц, добавления, обнавление, удаление данных...)

# MySQL, Firestore, MongoDB, PostgreSQL, SQLite ...

'''
почему именно PostgreSQL -> почитать
'''

# БД -> хранилище данных (организованная структура для хранения, изменения и обработки взаимосвязанной информации)


'''
Команды
'''

# 1. sudo -i -u postgres -> переход в консоль PostgreSQL под пользователем postgres

# 2. psql -> подключение к базе данных (по умолчанию postgres)

#3.  \q -> команда для выхода из postgres
#4.  \exit -> команда для выхода из postgresql

# psql -> вход в postgres под вашим юзером и вашей бд (после настройки)

# \l -> выводит список всех бд
# \du -> выводит список всех пользователей
# \c <database_name> -> подключение к бд database_name
# \dt -> список всех таблиц бд
# \d table_name -> просмотр информации о таблице table_name
# psql -U <user> -d <db_name> -> подключение под выбранным юзером(user) к бд db_name


'''
Типы полей (данных) в Postgres
'''

# 1. Numeric Types (Числовые типы)
# a. smallint(2 bytes) -> -32768 до 32767
# b. integer(4 bytes) -> -2147483648 до 2147483647
# c. bigint(8 bytes)

# d. smallserial -> целые положительные числа с автоинкрементом
# e. serial 
# f. bigserial 


# Character Types (строковые типы)

# a. varchar(кол-во символов) -> будет занимать меньше места в памяти, если указать 50 символов и записать 10 символов, то остальные будут свободны  (макс. количество 255 символов)

# b. char(кол-во символов) -> строка с постоянной длиной (если указать 50, а заполгить 10, то все остальные заполнятся пробелами) (макс кол-во символов 255)

# c. text() -> неограниченное кол-во символов

# Boolean Type 

    # a. boolean (1 byte) -> TRUE/FALSE

# date -> календарная дата (год.месяц.день)

# location -> координатная точка -> {243, -23} -> {x, y}

# ... и тд.

# CREATE USER <user_name> WITH PASSWORD 'password'; #создание пользователя

# ALTER ROLE <user> WITH SUPERUSER CREATEROLE CREATEDB; -> предоставление прав

# CREATE DATABASE <db_name>; ->  создание бд

# CREATE DATABASE <db_name> WITH OWNER <user>; -> создание бд с нужным юзером

# GRAND ALL PRIVILEGES ON DATABASE <db_name> TO <user>; -> дать все привилегии

# CREATE TABLE <table_name>(название колонок и тип данных);  

# DROP ROLE <user>; -> удаление пользователя

# DROP DATABASE <db_name>;

# DROP TABLE <table_name>;

'''
SQL не чувствителен к регистру, ключевые слова обычно пишутся в верхнем регистре
'''

'''
========= ограничения (constraints) =========
'''

# 1. UNIQUE -> ВСЕ ЗНАЧЕНИЯ ДОЛЖНЫ БЫТЬ УНИКАЛЬНЫМИ (не должны повторяться)
# 2. DEFAULT -> у столбца будет значение по умолчанию
# 3. NULL/NOT NULL -> определяет, будет ли поле обязательным для заполнения 
# 4. CHECK -> проверяет значения столбца на определенное условие
# 5. PRIMARY KEY -> определяет, будет ли столбец идентификатором (нужен для идентификации записи, чтобы отличать один объект от другого) Первичный ключ гарантирует, что нет двух записей с одинаковыми значениями ключа (используется в связях)
# 6. FOREIGN KEY -> задается для ссылки на другую таблицу. Внешний ключ, ограничение, которое накладывается на поле, которое ссылается на pk в другой таблице

'''Заполнение таблиц'''
# '''запись данных в таблицу (заполнение всех полей)'''
# insert into <table_name> values ('data');
# insert into <table_name> (columns_name) values ('data');
# insert into <table_name> (columns_name) values ('data'), ('data'), ('data');


'''Вывод данных из таблицы'''
# select * from <table_name>; # -- получение всех записей с таблицы (всех полей) 
# select <column_name> from <table_name>; 

'''Условия'''
# ORDER BY: Позволяет нам сортировать данные по убыванию или возрастанию. ASC(по возрастанию) и DESC(по убыванию) используються для определения сортировки
# SELECT * FROM <table_name> ORDER BY <column_name>; -- сортировка по определенному полю (по возрастанию ASC)
# SELECT * FROM  <table_name>  ORDER BY <column_name> DESC; -- сортировка по определенному полю (по убыванию DESC)


# LIMIT: Позволяет нам вернуть данные в ограниченном количестве
# SELECT * FROM  <table_name>  LIMIT 5; -- выводит первые 5 записей
# SELECT * FROM  <table_name>  OFFSET 5; -- пропускает первые 5 записей
# SELECT * FROM  <table_name>  LIMIT 4 OFFSET 3;
# -- пропускает первые 3 записей
# -- выбирает следующие 4 записей

# DISTINCT: Позволяет нам убирать дубликаты и возвращает только уникальные значения
# SELECT DISTINCT <column_name> FROM  <table_name> ;

# =========================================== операции сравнения
# >, <, >=, <=, =, != или <>
# ======================== where - для фильтрации текста
# WHERE: Используется для фильтрации по полям. Будут выводиться только те условия которые верны WHERE
# SELECT <column_name> FROM  <table_name>  WHERE <condition>; -- получение всех записей соответствующих этому условию

# Логические операции: and, or, not
# select * from product where not price > 15;
# проверка на вхождение (in)
# select * from product where name in ('world', 'name'); # IN
# SELECT * FROM product WHERE price >= 200 AND price <= 5000;
# BETWEEN - проверка на нахождение в диапазоне
# SELECT * FROM product WHERE price BETWEEN 200 AND 1500;



# LIKE: Выводит результать который соостветсвует введеному шаблону. Чувствителен к регистру
# ILKIE: Тоже самое только не зависит от регистра
# where name like 'A%' - имена нач на A
# like %@gmail.com
# %a% - что бы была а в слове
# like 'Ki_%' после только один символ
# like '__Ki%' перед 2 символа
# ilike не чувст к регистру

# SELECT * FROM  <table_name>  WHERE <column_name> like '%world%';

# SELECT * FROM <table_name>  WHERE <column_name> ilike '%world%'; --не чувтвителен к регистру


'''Удаление записей из таблицы'''
# DELETE FROM  <table_name> ; --удаление всех записей из таблицы
'''Условия'''
# delete from <table_name>  where <condition>; -- удаление всех записей соответствующих этому условию


'''Обновление записей в таблице'''
# UPDATE  <table_name>  SET <column_name> = new_val; -- обновление всех записей в таблице
'''Условия'''
# UPDATE  <table_name>  SET <column_name> = new_val WHERE <condition>; -- обновление всех записей соответствующих этому условию



'''================================='''
# GROUP BY - это ключевое слово которое позволяет выводить значение из колонок объеденённые в группы.
# GROUP BY: разделяет строки, возвращаемы оператором SELECT на группы. И теперь для каждой группы можно применить фукнцию

# Синтаксис: SELECT <column_name>, COUNT(*) from  <table_name> GROUP BY <column_name>;

# HAVING: Работает так же как и WHERE только он используется в GROUP BY
# HAVING
# HAVING - ключевое слово которое ВСЕГДА
# используется с GROUP BY конструкцией.
# HAVING VS WHERE
# HAVING как и WHERE отвечает за создание
# какого-либо условия для вывода на экран
# только определённых строк кода. Однако если WHERE отвечает за вывод строк по условию,
# то HAVING отвечает за вывод целых груп/
# категорий значений имеющих общие признаки.
# ПРИМЕР:
# SELECT *
# FROM clients
# GROUP BY profession
# HAVING salary > 2500;

# select * from post group by id having id > 1;






'''case работает так же как и if else
syntax:
    select <column> case when <column_data> = '...' then 'ok' when <column_data> = '...' then 'good' end 
    указывается поле где будет отображаться (hello, type ....) from <table_name>;
'''