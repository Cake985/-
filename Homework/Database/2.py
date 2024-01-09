"""
Создайте базу данных пользователя состояющую из следующих столбцов: id,username,password(В виде хэша).
Создайте программу которая предлагает пользователю зарегистрироваться или авторизироваться.
При регистрации программа запрашивает логин и пароль и добавляет в базу данных нового пользователя.
При авторизации программа запрашивает логин и пароль и выводит сообщение об успешной/неуспешной авторизации.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import Column, Integer, String, Float
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine("sqlite:///users.db")


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String)
    password = Column(String)


Base.metadata.create_all(bind=engine)


def signup():
    print('---регистрация---')
    username = input('введите логин: \n')
    password = input('введите пароль: \n')
    user = User(username=username, password=generate_password_hash(password))
    with Session(bind=engine,autoflush=False) as db:
        db.add(user)
        db.commit()
        print('регистрация прошла успешно')
    signin()

def signin():
    print('---Авторизация---')
    username = input('введите логин: \n')
    password = input('введите пароль: \n')
    with Session(bind=engine, autoflush=False) as db:
        user = db.query(User).filter(User.username == username).first()
        if user == None:
            print('пользователь с таким username не найден')
        else:
            if check_password_hash(user.password, password):
                print('вы успешно авторизовались')
            else:
                print('пароль не верен')


answer = input('введите 1 - для регистрации \nвведите 2 - для авторизации \n')
if answer == '1':
    signup()
elif answer == '2':
    signin()
else:
    print('перезапускай')