
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

    document_to_update = {"_id": ObjectId('6770009a8913c929d0f4a53b')}
    add_to_balance = {"$inc": {"balance": 600}}

    # Print original document
    pprint.pprint(account_collections.find_one(document_to_update))

    # Update the document
    result = account_collections.update_one(document_to_update, add_to_balance)

    pprint.pprint(account_collections.find_one(document_to_update))

    client.close()