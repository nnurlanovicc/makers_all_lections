'''
введение в Django REST

REST (representational state transfer) -> стиль API (стандарт которому следует API)

Принципы REST:
    1) "client - server" разграничение клиента и сервера (разделение клиента от сервера) клиент не связан с хранением данныхб 
        а сервер не связан с интерфейсомили же состоянием пользователя 

    2) "stateless" отсуствие состояния (нет сохранения состояния на сервере) -> сервер не должен хранить какую либо 
        информацию о клиенте 

    3) "cache"  кэширование (клиент сохраняет данные у себя в памяти) снижение нагрузки на сервере 
        и увеличение скорости

    4) многоуровневая система в системе могут быть не только уровни клиента и сервера, но и прокси слой - отвечающий
        за авторизация, выступает в роли сервера при отправки запроса клиентом 
        и в роли клиента при отправке ответа сервером

    5) единый интерфейс -> общение между клиентом и сервером 
        5.1) унификация ресурса - один url
        5.2) манипуляция через представление - клиент не меняет данные самостоятельно, а только предоставляет серверу  свое видение данных,
                а сервер решает менять их или нет
        5.3) самоописываемые сообщения (http запросы и ответы)
        5.4) гипермедиа как двигатель состояния ,набор гиперссылок htm, документы, json объекты со списком доступных ресурсов для запроса 
                сервер должен подсказывать клиенту какие шаги он может предпринять 

    6) код предоставляется по запросу:
        RESTfill API -> API которое соответсвует правилам REST
        URL -> конечные точки API определяют его структуру


порядок создания django проекта:
    1) создать вир окр
    2) установить:
        pip3 install -r django, djangorestframework
    3) создание самого проекта:
        django-admin startproject <name> .
    4) настройка бд
    5) регис библиотек и приложении

команды:
    python3 manage.py runserver - запускает наш проект на 127.0.0.1:8000
    python3 manage.py createsuperuser 
    python3 manage.py startapp <app_name> - создание приложения
    python3 manage.py makemigrations - создает файлы для имиграции
    python3 manage.py migrate - считывает файлы миграции и применяет их к бд , создает таблицы с указанными колонками и  ограничениями, 
                                    вносит изменения в существующие таблицы ...
    

'''



'''
=========================== Models ==============================


Model - класс, который характеризует структуру нашей таблицы в бд.
Атрибуты поля в таблице, наследуется от  django.db.models.Model 



========================== Поля ===========================

CharField -> для строковых значений, обяз нужно указывать max_length
SlugField -> для хранения  slag  короткая метка содержащая только буквы, тире и нижнее подчеркиванике. Обычно испоьзуется в URL 
TextField -> для хранения текста 
DcimalField ->  для дробных чисел.  
    max_digits - кол-во цифер целой части
    decimal_places - кол-во цифр после запятой
IntegerField -> для чисел 
BooleanField -> для bool 
DateField -> ...
    auto_now_add -  задается автоматически при создании объекта
    auto_now - обновляется каждый раз  когда объект сохраняется
DateTimeField -> ...
    auto_now_add ...
    auto_now ...
TimeField -> ...
DurationField ->  для периодов времени
EmailField -> ...
FileField ->  для загрузки файлов 
    upload_to -  для указания директории, где будут хранится, в бд хранится путь до файла
ImageField ->  для фото, тоже самое что  FileField  но требуется использовать библиотеку  Pillow
JSONField ->  для хранения строк в формате  JSON


'''

'''
QuerySet (related_name, related_query_name, ManyToManyField, OnetoOneField)


===Связи:

on to one
many to many
foreign key

=== on_delete:

models.CASCADE -> каскадное удаление, при удалении главного объекта, удаляется все зависящие от него объекты

models.PROTECT ->  вызывает ошибку при попытке удалить главный объект

models.RESTRICT -> в отличии от PROTECT, удаление главного объекта допускается , если он также ссылается на другой объект, 
    который удаляется в той же операции, но через отношение CASCADE

models.SET_NULL -> не удаляет зависящие объекты , а оставит null (null=True)

models.SET_DEFAULT -> ставит default, только если определен default 

models.DO_NOTHING -> вообще ничего не делает, так что буудет ошибка


==== как проходит запрос:
1. wsgi/asgi -> те кто принимают запросы и отправляют ответ
2. settings - middleware -> функции которые обрабатывают  запрос
3. urls ->  маршрутизатор который проверяет часть url и если выходит совпадение, передает запрос нужной функции views
4. views ->  функции которые возвращают данные в нужном формате
5. serializers ->  классы которые преобразуют данные из  json  в объекты от моделей и наоборот
6. models
7. managers (objects) ->  это классы еоторые работают с  ORM , у них есть методы для создания , обновления, удаления, получения ... 
    записей из таблицы 
8. db


'''
