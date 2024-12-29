
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

    # Select checking accounts type with balance greater than 1000
    select_by_balance = {"$match": {"balance": {"$gt": 1000}, "account_type": "checking"}}

    # Organize documents in order from highest to lowest balance
    organize_by_original_balance = {"$sort": {"balance": -1}}

    # Return only the account type & balance fields, plus a new field containing balance in GDP
    return_specified_fiels = {
        "$project": {
            "account_type": 1, 
            "balance": 1, 
            "balance_in_gbp": {"$multiply": ["$balance", 1.3]},    # Conversion rate: 1.3
            "_id": 0
        }
    }

    # Create an aggregation pipeline
    pipeline = [select_by_balance, organize_by_original_balance, return_specified_fiels]

    # Execute the aggregation pipeline
    results = account_collections.aggregate(pipeline)

    print("Account type, original balance and balance in GDP with original balance >1000:")
    for item in results:
        pprint.pprint(item)
