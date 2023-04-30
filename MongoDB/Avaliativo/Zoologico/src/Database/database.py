from typing import Collection
import pymongo

class Database:
    def __init__(self, url, database, collection):
        self.connect(url, database, collection)

    def connect(self, url, database, collection):
        try:
            connectionString = url
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def disconnect(self):
        self.clusterConnection = None
        self.db = None
        self.collection = None