import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/neurolab08")

database = client["neurolab08"]

collection = database['Products']

d = {'companyName':'ineuron',
     'product': 'Affordable AI',
     'courseOffered':'Machine Learning with Deployment'}

rec = collection.insert_one(d)

all_record = collection.find()

for idx, record in enumerate(all_record):
    print(f"{idx}: {record}")