from pymongo import MongoClient
import pprint

# Abrindo uma conexão
client = MongoClient('mongodb://localhost:27017')

# Indicar qual Database deseja-se acessar
db = client['dbworld']

# Indicando qual collection será utilizada
paises = db.countries

# Buscando tudo
'''
results = paises.find()

# For each
for result in results:
    pprint.pprint(result)
'''

# Filter-> Buscando todos os países da Europa que possuem area maior que 300000
# Project -> apenas o nome dos países
results = paises.find(
    {"region": "Europe", "area":{"$gt": 300000}}, #FILTER
    {"name": 1}
)

# For each
for result in results:
    pprint.pprint(result)