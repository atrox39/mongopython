import json
# Constants
CONNECTION_STRING = "mongodb://localhost/"

def get_database():
    from pymongo.mongo_client import MongoClient
    client = MongoClient(CONNECTION_STRING)
    return client['pymongo']

if __name__ == "__main__":
    dbname = get_database()
    collection = dbname['test']
    items = collection.find({"item_name": "Test Item"})
    for item in items:
        print(item)