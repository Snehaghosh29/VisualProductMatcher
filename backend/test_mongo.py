from pymongo import MongoClient

try:
    # your Atlas connection string
    uri = "mongodb+srv://snehaghosh2903_db_user:SN2903%40%239osh@visual-matcher-cluster.jzawms2.mongodb.net/?retryWrites=true&w=majority&appName=visual-matcher-cluster"
    
    # connect to cluster
    client = MongoClient(uri)

    # try listing databases
    print("✅ Connection successful!")
    print("Available Databases:", client.list_database_names())

except Exception as e:
    print("❌ Connection failed:")
    print(e)
