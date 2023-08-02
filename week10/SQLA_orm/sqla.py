'''
SQLAlchemy -> библеотека для работы с базой данных 

SQLAlchemy ORM (Object Relational Mapping) -> объектно реляционное отображение -> позволяет работать с бд с помощью ООП.
Создание таблиц и связей между ними с помощью классов Python. Предоставляет систему для создания запросов с помощью ООП вместо SQL.

'''

from sqlalchemy import create_engine, Column, Integer, String,DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import sessionmaker, Session
from datetime import datetime

db = 'postgresql://nursultan:@localhost:5432/main'
engine = create_engine(db, echo=True)
# engine.execute(
#     'CREATE TABLE ...'
# )

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(80), unique=True,nullable=False)
    password = Column(String(30), nullable=True)
    posts = relationship('Post',backref='author')




class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(100), nullable=False)
    body = Column(String(250), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    author_id = Column(Integer, ForeignKey('users.id'))



    # __table_args = (
    #     PrimaryKeyConstraint('id',name='post_pk'),
    # )


# Base.metadata.create_all(engine)


Session = sessionmaker(engine)
session = Session()

user1 = User(
    username='john',
    email='johnsnow@gmail.com',
    password='12345678'
)

user2 = User(
    username='rob',
    email='robstark@gmail.com',
    password='12345678'
)


user3 = User(
    username='Sansa',
    email='sansastark@gmail.com',
    password='12345678'
)

# print(user1.email)

# session.add(user1)                   #добавление одного
# session.add_all([user2, user3])      #добавление несколько объектов
# print(session.new)
# session.commit()



post1 = Post(
    title = 'first post',
    body = 'hello everyone',
    author_id = 1
)

post2 = Post(
    title = 'second post',
    body = 'hello everyone for a second time',
    author_id = 1
)

post3 = Post(
    title = 'third post',
    body = 'hello everyone and fuck you',
    author_id = 1
)


# session.add_all([post1, post2, post3])
# print(session.new)
# session.commit()




# posts = session.query(Post).all()
# for post in posts:
#     print(post.title,post.body)




post_count = session.query(Post).count()
print(post_count)

post_1 = session.query(Post).first()
print(post_1)

post_id = session.query(Post).get(4)
print(post_id.title)

















'''
удаление данных в бд:
'''

session.query(Post).filter(Post.body == 'hello everyone').delete()
session.commit()
