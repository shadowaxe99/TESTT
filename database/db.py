Sure! Here's the code for the file `database/db.py`:

```python
import pymongo

class Database:
    def __init__(self, host, port, username, password):
        self.client = pymongo.MongoClient(host, port, username=username, password=password)
        self.db = self.client["uber_clone"]

    def insert_user(self, user_data):
        users_collection = self.db["users"]
        users_collection.insert_one(user_data)

    def get_user(self, user_id):
        users_collection = self.db["users"]
        return users_collection.find_one({"_id": user_id})

    def update_user(self, user_id, updated_data):
        users_collection = self.db["users"]
        users_collection.update_one({"_id": user_id}, {"$set": updated_data})

    def delete_user(self, user_id):
        users_collection = self.db["users"]
        users_collection.delete_one({"_id": user_id})
```

This code defines a `Database` class that handles the interaction with the MongoDB database for the Über Clone platform. It provides methods for inserting, retrieving, updating, and deleting user data in the `users` collection of the `uber_clone` database.

Please note that this code assumes you have already installed the `pymongo` library for Python to interact with MongoDB.