from pymongo import MongoClient
from datetime import datetime

#client = MongoClient("mongodb://gadi:Aueujo12!@ds033996.mlab.com:33996/shifts")
#db = client.get_default_database()
mongolab_uri = "mongodb://test:test@ds035046.mlab.com:35046/schedy"

client = MongoClient(mongolab_uri)
db = client.get_default_database()

cursor = db.test1_events.find({"business_id":"1"})
for document in cursor:
	print document["customer_name"]