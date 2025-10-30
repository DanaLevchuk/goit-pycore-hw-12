from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres")

try:
    with engine.connect() as connection:
        print("✅ Підключення до бази даних успішне!")
except Exception as e:
    print("❌ Помилка підключення:", e)
