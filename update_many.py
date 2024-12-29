
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

    #Filter
    document_to_update = {"account_type": "checking"}
    set_field = {"$set": {"minimum_balance": 50}}

    # Update the document
    result = account_collections.update_many(document_to_update, set_field)
    print(f"Number of documents matched: {result.matched_count}")
    print(f"Number of documents updated: {result.modified_count}")

    pprint.pprint(account_collections.find_one(document_to_update))

    client.close()