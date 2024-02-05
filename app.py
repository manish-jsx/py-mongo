import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint


def seed_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database']  # Replace 'your_database' with your actual database name

    # Seed sample data into 'users' collection
    users_collection = db['users']
    users_collection.insert_many([
        {"name": "John Doe", "isActive": True},
        {"name": "Alice Smith", "isActive": False},
        {"name": "Bob Johnson", "isActive": True},
        # Add more sample data as needed
    ])

    client.close()

def retrieve_active_users():
    load_dotenv()  # Load environment variables from .env file

    mongodb_uri = os.getenv('MONGODB_URI')
    debug_mode = os.getenv('DEBUG', '').lower() == 'true'

    # MongoDB Connection
    client = MongoClient(mongodb_uri)
    db = client['your_database']  # Replace 'your_database' with your actual database name

    # Retrieve documents from 'users' collection with 'isActive' set to true
    query = {'isActive': True}
    users_collection = db['users']
    result = users_collection.find(query)

     # Display the results in a formatted way using pprint
    print("Documents with 'isActive' set to true:")
    for document in result:
        pprint(document)

    # Logging Progress
    if debug_mode:
        print("Task completed successfully.")

    client.close()

# Seed data into the 'users' collection
seed_data()

# Retrieve and display active users
retrieve_active_users()
