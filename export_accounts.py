
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

    # Export all documents in the collection to a python file with indentation
    with open("accounts.py", "w") as file:
        cursor = account_collections.find({})
        for document in cursor:
            pprint.pprint(document, file, indent=4)
            print("\n", file=file)
