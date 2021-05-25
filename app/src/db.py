import pymongo

def connect_to_mongodb(DB_URI: str):
    try:
        # initiate db connection
        client = pymongo.MongoClient(
            host=DB_URI,
            authSource="admin",
            serverSelectionTimeoutMS=7000
        )
        client.server_info()
    except Exception as ex:
        # show error
        print("ERROR: Connection failed. Check if Database is up.")
        print(ex)
    else:
        return client


