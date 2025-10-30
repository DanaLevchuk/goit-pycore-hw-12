from database import session
from models import Grade, Student, Teacher, Subject, Group

# Очистимо всі таблиці перед новим засівом
session.query(Grade).delete()
session.query(Student).delete()
session.query(Subject).delete()
session.query(Teacher).delete()
session.query(Group).delete()
session.commit()

from faker import Faker
from random import randint, choice
from datetime import date
from database import session
from create_db import Group, Student, Teacher, Subject, Grade

fake = Faker()

# --- створення груп ---
groups = [Group(name=f"Group {c}") for c in ["A", "B", "C"]]
session.add_all(groups)
session.commit()

# --- створення викладачів ---
teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

# --- створення предметів ---
subjects = [
    Subject(name=name, teacher=choice(teachers))
    for name in ["Math", "History", "Biology", "Physics", "English", "IT"]
]
session.add_all(subjects)
session.commit()

# --- створення студентів ---
students = [
    Student(fullname=fake.name(), group=choice(groups))
    for _ in range(40)
]
session.add_all(students)
session.commit()

# --- створення оцінок ---
for student in students:
    for subject in subjects:
        for _ in range(randint(5, 10)):
            grade = Grade(
                grade=randint(60, 100),
                date_received=fake.date_between(start_date="-6m", end_date="today"),
                student=student,
                subject=subject,
            )
            session.add(grade)

session.commit()
print("✅ Database seeded successfully!")
