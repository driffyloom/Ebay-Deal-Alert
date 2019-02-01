from bs4 import BeautifulSoup
from ebaysdk.finding import Connection as Finding
import pymongo


class eBaySearch:

    def __init__(self, appID):
        self.api = Finding(domain='svcs.sandbox.ebay.com',
              appid = appID,
              config_file=None)
        
        username = "AustinAdmin"
        password = "test"
        
        self.myclient = pymongo.MongoClient("mongodb://%s:%s@localhost:27017/"% (username, password))



    #sends api request with searchQuery and priceLimit to ebayAPI and returns response
    def search(self, searchQuery, priceLimit):
        #needs to eventually get data from mongodb for things like category
        api_request = {'keywords': searchQuery,
               'outputSelector': 'SellerInfo',
               'sortOrder': 'PricePlusShippingHighest',
               'itemFilter': [
                {'name': 'MaxPrice',
                 'value': priceLimit},
                ]}

        self.queryAndPrice = searchQuery + priceLimit
        
        response = self.api.execute('findItemsAdvanced',api_request)
        soup = BeautifulSoup(response.content, 'lxml')

        totalentries = int(soup.find('totalentries').text)

        items = soup.find_all('item')

        return items;

    def printSearchResults(self,items):
        
        for item in items:
            cat = item.categoryname.string.lower()
            title = item.title.string.lower()
            price = int(round(float(item.currentprice.string)))
            url = item.viewitemurl.string.lower()
            #Photo only exists for non sandbox site
            try:
                image = item.galleryurl.string.lower()
            except AttributeError:
                print("No Image skipping image save")
                
            #print(item)
            print('________')
            print('cat:\n' + cat + '\n')
            print('title:\n' + title + '\n')
            print('price:\n' + str(price) + '\n')
            print('url:\n' + url + '\n')
            input()
            
    def addResultsToDB(self,items):
        #Create Database called eBaySearchData
        mydb = self.myclient["eBaySearchData"]

        #need to modify collection to have user as an extra layer above everything
        #to store user then their saves
        #collection = table in mongoDB
        queryAndPriceCollection = mydb[self.queryAndPrice]

        allItemsToAddToCol = []
    
        for item in items:
            collectionDict = {}
            title = item.title.string.lower()
            cat = item.categoryname.string.lower()
            price = int(round(float(item.currentprice.string)))
            url = item.viewitemurl.string.lower()
            try:
                image = item.galleryurl.string.lower()
            except AttributeError:
                image = "N/A"
            collectionDict[self.queryAndPrice] = {"title": title, "category":cat, "price":price,
                                                  "url":url , "image" :image}
            allItemsToAddToCol.append(collectionDict)


        completedInsertionIDList = queryAndPriceCollection.insert_many(allItemsToAddToCol)

        print(completedInsertionIDList.inserted_ids)

test = eBaySearch("AustinCh-DealAler-SBX-a39332c51-8b41e853")



searchQuery = input("What are you searching for? (Using eBay Sandbox!)");

#needs to eventually get data from mongodb for things like category
priceLimit = input("Price Limit? (Using eBay Sandbox)");

#test.printSearchResults(test.search(searchQuery,priceLimit))

test.addResultsToDB(test.search(searchQuery,priceLimit))

#should make table for each user search query
#dblist = myclient.list_database_names()



if "eBaySearchData" in dblist:
  print("The database exists.")


