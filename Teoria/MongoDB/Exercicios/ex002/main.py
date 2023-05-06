from pymongo import MongoClient

def main():
    print('Olá, mundo!')
    client = MongoClient('mongodb://localhost:27017')
    db = client['dbworld']
    countries = db['countries']
    result = countries.update_one({'name.common':'Andorra'},{'$set':{'name.common':'João Henrique'}})
    
    if result.acknowledged:
        print('Deu bão')
    else:
        print('Deu ruim')

    results = countries.find({'name.common': 'João Henrique'}, {'name.common':1})

    for result in results:
        print(result)

if __name__ == "__main__":
    main()