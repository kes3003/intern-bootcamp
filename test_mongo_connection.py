from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def test_mongo_connection():
    try:
        # Connect to your local MongoDB instance
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
        
        # Ping the server
        client.admin.command("ping")
        print("MongoDB connection successful!")

        # Optionally, list databases
        print("Databases:", client.list_database_names())

        # Close connection
        client.close()

    except ConnectionFailure as e:
        print("MongoDB connection failed:")
        print(e)

if __name__ == "__main__":
    test_mongo_connection()
