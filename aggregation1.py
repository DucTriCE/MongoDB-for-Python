
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

    # Select accounts with balance less than 2200
    select_by_balance = {"$match": {"balance": {"$lt": 5000}}}

    # Separate the accounts by account type and calculate the average balance
    separate_by_account_type = {"$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}}

    # Create an aggregation pipeline
    pipeline = [select_by_balance, separate_by_account_type]

    # Execute the aggregation pipeline
    results = account_collections.aggregate(pipeline)
    print("Aggregation results:")
    for item in results:
        pprint.pprint(item)