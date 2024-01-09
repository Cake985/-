"""
Создайте модели базы данных работников it-компании
Таблица Работники содержит следующие столбцы: id,имя,стаж, должности
Таблица Должности содержит следующие столбцы: id, название, работники.
Напишите функции вывода всех должностей запрашиваемого работника, всех работников по должности, всех работников определенной должности со стажем больше 5.
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///example.db', echo=True)

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience = Column(Integer)
    position_id = Column(Integer, ForeignKey('positions.id'))
    position = relationship('Position', back_populates='employees')

class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    employees = relationship('Employee', back_populates='position')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def get_positions_by_employee(employee_name):
    employee = session.query(Employee).filter_by(name=employee_name).first()
    if employee:
        return [position.title for position in employee.position]
    else:
        return []

def get_employees_by_position(position_title):
    position = session.query(Position).filter_by(title=position_title).first()
    if position:
        return [employee.name for employee in position.employees]
    else:
        return []

def get_employees_by_position_and_experience(position_title, min_experience=5):
    employees = session.query(Employee).join(Position).filter(
        Position.title == position_title,
        Employee.experience > min_experience
    ).all()
    return [employee.name for employee in employees]

employee_name = 'John Doe'
print(f"All positions of {employee_name}: {get_positions_by_employee(employee_name)}")

position_title = 'Software Engineer'
print(f"All employees with position {position_title}: {get_employees_by_position(position_title)}")

print(f"All Software Engineers with experience > 5 years: {get_employees_by_position_and_experience(position_title)}")