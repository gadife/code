from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.shifts

result = db.doctors.insert_one(
    {
        "name": "Moshe Haim",
        "start_date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
        "gimel_pay": "off",
        "stations": {
            "pagia_toran": True,
            "aleph": True,
            "bet": True,
            "pagia_yom": True,
            "zvulun": True,
            "tira": True,
            "yokneam": True,
            "tipat_halav": True
        },
        "day_off": [datetime.strptime("2016-09-17", "%Y-%m-%d"), datetime.strptime("2016-09-06", "%Y-%m-%d"), datetime.strptime("2016-09-16", "%Y-%m-%d")]
    }
)

#print result.inserted_id