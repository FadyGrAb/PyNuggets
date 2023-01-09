import sqlite3
import random
import pathlib

db_path = pathlib.Path("cityTraffic.sqlite")

if db_path.exists():
    db_path.unlink()

cnx = sqlite3.connect(db_path)
cursor = cnx.cursor()

# Create Table
cursor.execute("""
    CREATE TABLE traffic (
        id INT PRIMARY KEY NOT NULL,
        timestampt TEXT NOT NULL,
        city TEXT NOT NULL,
        district TEXT NOT NULL,
        vehicleType TEXT NOT NULL
    )
""")

for _ in range(10000):
    pass

cnx.close()
