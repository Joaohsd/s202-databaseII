from mongoDB.db.productsDB import productsDB
from mongoDB.services.productAnalyzer import productAnalyzer

import json

def main():
    # Opening the dataset
    with open('./dataset/data.json',encoding='utf8') as data:
        dataset = json.load(data)

    # Create the database
    prodDB = productsDB(database='shop', collection='acquisition_history')
    # Reset the database and pass the new dataset
    prodDB.resetDatabase(dataset=dataset)

    # Create product analyzer service
    prodAnalyzer = productAnalyzer(prodDB)

    # Call methods created in productAnalyzer service
    print('The client B spent:',prodAnalyzer.totalSpentByCustomer('B'))
    print('The least sold product was the:',prodAnalyzer.leastSoldProduct())
    print('The customer who spent the least was the:', prodAnalyzer.leastCustomerSpent())
    print('Products that had more than 2 products sold:')
    for product in prodAnalyzer.productsWithTwoOrMoreUnitsSold():
        print(product)

if __name__ == '__main__':
    main()
