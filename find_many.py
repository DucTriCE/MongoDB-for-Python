
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

    document_to_find = {"balance": {"$gt": 500}}

    # Find all documents that match the query
    cursor = account_collections.find(document_to_find)

    num_docs = 0
    for document in cursor:
        num_docs += 1
        pprint.pprint(document)
        print()

    print(f"Number of documents found: {num_docs}")

    client.close()
