"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship

engine = create_engine("sqlite:///books.db")

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    books = relationship('Book', back_populates='user')


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates='books')


Base.metadata.create_all(engine)

with Session(autoflush=False, bind=engine) as db:
    kaplan = User(name='Kaplan', books=[
        Book(title='Book 1', author='Author 1'),
        Book(title='Book 2', author='Author 2')
    ])
    makaka = User(name='Matvei', books=[
        Book(title='Book 3', author='Author 3'),
        Book(title='Book 4', author='Author 4')
    ])
    areg = User(name='Areg', books=[
        Book(title='Book 5', author='Author 5'),
        Book(title='Book 6', author='Author 6')
    ])

    db.add_all([kaplan, makaka, areg])
    db.commit()


def get_books_for_user(user_name):
    with Session(bind=engine) as db:
        user = db.query(User).filter_by(name=user_name).first()
        if user:
            books = user.books
            for book in books:
                print(f"{user.name}'s book: {book.title} by {book.author}")
        else:
            print(f"User {user_name} not found")


get_books_for_user('Kaplan')