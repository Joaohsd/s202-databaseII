from db.database import Database

class BookService():
    def __init__(self, database:Database):
        self._db = database

    def getLastId(self) -> int:
        results = self._db.collection.aggregate([
            {"$group":{"_id":None, "maxId":{"$max":"$_id"}}},
            {"$project":{"_id": 0, "maxId": 1}},
            {"$limit": 1}
        ])
        if results.alive:
            maxId = results.next().get('maxId')
        else:
            maxId = None
        return maxId
    