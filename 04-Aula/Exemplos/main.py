from database import Database
from save_json import writeAJson

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
])

writeAJson(result, 'media')

result2 = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])

writeAJson(result2, 'result2')

result3= db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"_id.data": 1, "total": -1}},
    {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
])

writeAJson(result3, 'result3')
