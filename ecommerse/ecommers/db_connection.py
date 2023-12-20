import pymongo

url='mongodb://localhost:27017'
products=pymongo.MongoClient(url)
db=products['Ecommers']