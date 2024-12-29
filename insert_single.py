
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

from dotenv import load_dotenv
import os
import datetime

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

    # Insert a single document into the collection
    new_account = {
        "account_holder": "Addison Shelton",
        "account_id": "MDB955769550",
        "account_type": "checking",
        "balance": 1000,
        "last_updated": datetime.datetime.now()
    }

    # Insert the new account into the collection
    result = account_collections.insert_one(new_account)
    document_id = result.inserted_id
    print(f"Inserted document with ID {document_id}")

    client.close()
