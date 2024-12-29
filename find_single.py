
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

from dotenv import load_dotenv
import os
import datetime
import pprint

if __name__ == "__main__":
        
    load_dotenv()
    api_key = os.environ["API_KEY"]

    uri = api_key

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Get reference to the database
    db = client.bank

    # Get reference to the 'accounts' collection
    account_collections = db.accounts

    document_to_find = {"_id": ObjectId('6770009a8913c929d0f4a53b')}

    # Find a single document in the collection
    result = account_collections.find_one(document_to_find)
    pprint.pprint(result)

    client.close()
