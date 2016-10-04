from pymongo import MongoClient
from datetime import datetime

#client = MongoClient("mongodb://gadi:Aueujo12!@ds033996.mlab.com:33996/shifts")
#db = client.get_default_database()
mongolab_uri = "mongodb://test:test@ds033996.mlab.com:33996/shifts"

client = MongoClient(mongolab_uri)
db = client.get_default_database()

For num in xrange(10):
	cursor = db.doctors.find({"gimel_pay":"Day-Off"})
		for document in cursor:
    		print document["first"] + " " + document["last"]
	num = num +1


