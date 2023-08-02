'''
HTTP протокол (HyperTextTransferProtocol)

это протокол для передачи данных (клиент-сервер протокол)
его задача обмен данными между пользователем и веб-сервером

ip, tcp, udp, smtp, ftp, httpa, https ...


HTTP - запрос
Метод URI HTTP/версия 
Стратовая строка:
GET /category HTTP/1.1


стартовая строка:
    method -> представляет собой одно слово, написанное заглавными буквами.
    (POST, GET, PUT, PATCH, DELETE)

    URI -> (Union Resorse Identifier) -> путь до конкретного ресурса (/,/shop, /category ,...)

    HTTP version (с какой версией составлен запрос) (1.1, 2 ...)


Меттоды HTTP:
    GET -> получение ресурса
    POST -> отправка данных (создание ресурса)
    PUT -> полная замена ресурса
    PATCH -> частичное изменение ресурса
    DELETE -> удаление ресурса

Заголовки запроса:
    Host: makers.kg -> адрес ресурса
    Body: тело запроса -> данные, которые мы хотим передать
    Accept -> спимок форматов ресурса
    Accept-Encoding -> перечень способов кодирования
    Accept-Language -> список языков, которые поддерживает клиент 
    Authorization -> данные для авторизации
    User-Agent -> имя и версия клиента

Тело запроса(Body):
    Body: email=test@gmail.com&password=12345678

GET/HTTP/1.1
Host: makers.kg

Пример HTTP response (ответ)
HTTP/1.1 200 OK -> Стартовая строка
Server: nginx
Date: 09, Aprel 2022 22:34:54


Структура HTTP ответа:
    стартовая строка HTTP/версия кода
    состояния, пояснения


Заголовки ответа: 
    Content-Type: ...
    Content-Lenght: ...
    Content-Language: ...
    Content-Encoding: ...
    Expires: дата, после которой ответ перестанет быть актуальным
    Location: URI по которому нужно перейти  или созданного ресурса


Коды состояния:
    1xx -> информационные
    2xx -> успех
    3xx -> перенаправление
    4xx -> ошибки клиента
    5xx -> ошибка сервера



    
URL -> (Uniform Resourse Location) метонахождения ресурса
URN -> (Uniform Resourse Name) 
URI -> (Uniform Resourse Identifier)

Domain -> уникальное название (www.google.com) 
HOST -> адрес на который мы отправляем запрос
PORT -> номер сервиса на сервере (backend: 8000, frontend: 3000, http-server: 80)


'''