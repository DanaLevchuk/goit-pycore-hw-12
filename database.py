from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Підключення до бази PostgreSQL у Docker
# Пароль і порт — такі ж, як у твоїй команді docker run
DATABASE_URL = "postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres"

# Створюємо engine
engine = create_engine(DATABASE_URL)

# Базовий клас для моделей
Base = declarative_base()

# Створюємо сесію
Session = sessionmaker(bind=engine)
session = Session()
