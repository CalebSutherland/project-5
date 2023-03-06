import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb
collection = db.brevets

def brevet_insert(start_time, brevets_dist, checkpoints):
    output = collection.insert_one({
        "start_time": start_time,
        "brev_dist": brevets_dist,
        "checkpoints": checkpoints})
    _id = output.inserted_id
    return str(_id)


def brevet_find():
    brevets = collection.find().sort("_id", -1).limit(1)

    for races in brevets:
        return races["start_time"], races["brev_dist"], races["checkpoints"]