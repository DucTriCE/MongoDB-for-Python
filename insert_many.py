
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

    # Insert many documents into the collection
    new_accounts = [
        {
            "account_id": "MDB574189320",
            "account_holder": "Coşkun",
            "account_type": "savings",
            "balance": 2123.87,
            "transfers_complete": [
                "TR488315128",
                "TR401663822"
            ]
        },
        {
            "account_id": "MDB335652528",
            "account_holder": "Marcus",
            "account_type": "savings",
            "balance": 123.14,
            "transfers_complete": [
                "TR488315128",
                "TR655897500"
            ]
        }
    ]

    result = account_collections.insert_many(new_accounts)
    document_ids = result.inserted_ids
    print(f"Inserted documents with IDs {document_ids}")

    client.close()
