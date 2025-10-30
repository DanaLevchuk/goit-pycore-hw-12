from database import engine, Base
from create_db import *

Base.metadata.create_all(engine)

print("✅ Усі таблиці успішно створені!")
