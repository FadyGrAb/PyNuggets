import sqlite3
import random
import pathlib
import datetime
import string

db_path = pathlib.Path("cityTraffic.sqlite")

if db_path.exists():
    db_path.unlink()

cnx = sqlite3.connect(db_path)
cursor = cnx.cursor()

# Create Table
cursor.execute("""
    CREATE TABLE traffic (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        city TEXT NOT NULL,
        zone TEXT NOT NULL,
        vehicleType TEXT NOT NULL,
        vehiclePlate TEXT NOT NULL
    )
""")

current_timestamp = datetime.datetime(
    year=2022,
    month=12,
    day=1
)

for _ in range(100000):

    city = random.choice(["FunLand", "AwsomeLand", "GoodCiy", "GreatCity"])
    zone = "Z" + str(random.randint(1, 5))
    vehicle_type = random.choice(["Truck", "EV", "Pickup", "Van", "Regular"])
    vehicle_plate = random.choices(
        string.ascii_uppercase, k=3) + random.choices(string.digits, k=4)
    vehicle_plate = "".join(vehicle_plate)

    print(current_timestamp.strftime("%Y-%m-%d %H:%M:%S"), city,
          zone, vehicle_type, vehicle_plate, sep=', ')

    cursor.execute(
        """
            INSERT INTO traffic (timestamp, city, zone, vehicleType, vehiclePlate)
            VALUES ('{}', '{}', '{}', '{}', '{}') 
        """.format(
            current_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            city,
            zone,
            vehicle_type,
            vehicle_plate
        )
    )

    current_timestamp = current_timestamp + \
        datetime.timedelta(seconds=random.randint(1, 30))

cnx.commit()

cnx.close()
