"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import Column, Integer, String, Float

engine = create_engine("sqlite:///films.db")


class Base(DeclarativeBase): pass


class Films(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    year = Column(Integer)
    genre = Column(String)
    rating = Column(Float)


Base.metadata.create_all(bind=engine)


def create_film(name, year, genre, rating):
    with Session(bind=engine, autoflush=False) as db:
        new_film = Films(name=name, year=year, genre=genre, rating=rating)
        db.add(new_film)
        db.commit()

# create_film("Titanic", 1997, "melodrama", 8.4)
# create_film("Kaplan v kino", 2023, "horror", 10)


def show_films():
    with Session(bind=engine, autoflush=False) as db:
        all_films = db.query(Films).all()
        for film in all_films:
            print(f"{film.name} - {film.year}: {film.genre}")


def show_film_of_year(year):
    with Session(bind=engine, autoflush=False) as db:
        film = db.query(Films).filter(Films.year==year).first()
        print(film.name)

show_film_of_year(2023)