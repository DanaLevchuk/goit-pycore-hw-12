import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Підключення до бази
conn = sqlite3.connect("university.db")
cur = conn.cursor()

# --- Дані для генерації ---
GROUPS = ["Group A", "Group B", "Group C"]
TEACHERS = [fake.name() for _ in range(5)]
SUBJECTS = ["Math", "Physics", "History", "Biology", "Programming", "English", "Chemistry"]

# --- Заповнення таблиці groups ---
for g in GROUPS:
    cur.execute("INSERT INTO groups (name) VALUES (?)", (g,))

# --- Заповнення таблиці teachers ---
for t in TEACHERS:
    cur.execute("INSERT INTO teachers (name) VALUES (?)", (t,))

# --- Отримуємо ID викладачів ---
cur.execute("SELECT id FROM teachers")
teacher_ids = [row[0] for row in cur.fetchall()]

# --- Заповнення таблиці subjects ---
for s in SUBJECTS:
    teacher_id = random.choice(teacher_ids)
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (s, teacher_id))

# --- Заповнення таблиці students ---
cur.execute("SELECT id FROM groups")
group_ids = [row[0] for row in cur.fetchall()]

for _ in range(40):  # ~40 студентів
    name = fake.name()
    group_id = random.choice(group_ids)
    cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))

# --- Заповнення таблиці grades ---
cur.execute("SELECT id FROM students")
student_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT id FROM subjects")
subject_ids = [row[0] for row in cur.fetchall()]

for student_id in student_ids:
    for subject_id in subject_ids:
        for _ in range(random.randint(5, 20)):  # кожен студент має кілька оцінок
            grade = random.randint(60, 100)
            days_ago = random.randint(1, 200)
            date_received = datetime.now() - timedelta(days=days_ago)
            cur.execute("""
                INSERT INTO grades (student_id, subject_id, grade, date_received)
                VALUES (?, ?, ?, ?)
            """, (student_id, subject_id, grade, date_received.date()))

conn.commit()
conn.close()

print("✅ Database successfully filled with random data!")
