from utils.save_json import writeToJson

class productAnalyzer():
    def __init__(self, db):
        self.db = db

    def totalSpentByCustomer(self, customer='A'):
        '''
            Returns the total spent by customer
        '''
        results = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$match": {"_id": customer}},
            {"$limit":1}
        ])
        return results.next()['total']

    def leastSoldProduct(self):
        '''
            Returns the least sold product in the dataset
        '''
        results = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id":"$produtos.nome", "quantidade":{"$sum":"$produtos.quantidade"}}},
            {"$sort":{"quantidade":1}},
            {"$limit":1}
        ])
        return results.next()['_id']
    
    def leastCustomerSpent(self):
        '''
            Returns the customer who spent the least
        '''
        results = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$project": {"_id": 1, "gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": "$_id", "menorGasto":{"$sum":"$gasto"}}},
            {"$sort":{"menorGasto":1}},
            {"$limit":1}
        ])
        id = results.next()["_id"]
        results = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"_id": id}},
            {"$group":{"_id":"$cliente_id", "gasto":{"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ])
        return results.next()["_id"]
    
    def productsWithTwoOrMoreUnitsSold(self):
        '''
            Returns the products that had more than 2 products sold
        '''
        results = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id":"$produtos.nome", "quantidade":{"$sum":"$produtos.quantidade"}}},
            {"$match": {"quantidade":{"$gt":2}}},
            {"$project":{"_id": 1}}
        ])

        products = []

        for result in results :
            products.append(result["_id"])

        return products
        
    