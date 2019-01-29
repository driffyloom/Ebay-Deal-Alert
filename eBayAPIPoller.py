from bs4 import BeautifulSoup
from ebaysdk.finding import Connection as Finding
import pymongo
import mongoengine

class eBaySearch:

    def __init__(self, appID):
        self.api = Finding(domain='svcs.sandbox.ebay.com',
              appid = appID,
              config_file=None)


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

        this.queryAndPrice = searchQuery + priceLimit
        
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
            
    def createResultDict(self,items):

        
        collectionDict = {}


        #need to modify this to have user as an extra layer above everything
        #to store user then their saves
        collectionDict[this.queryAndPrice] = {}
    
        for item in items:
            cat = item.categoryname.string.lower()
            title = item.title.string.lower()
            price = int(round(float(item.currentprice.string)))
            url = item.viewitemurl.string.lower()
            
            collectionDict[this.queryAndPrice] = {'}

test = eBaySearch("AustinCh-DealAler-SBX-a39332c51-8b41e853")


searchQuery = input("What are you searching for? (Using eBay Sandbox!)");

#needs to eventually get data from mongodb for things like category
priceLimit = input("Price Limit? (Using eBay Sandbox)");

#test.printSearchResults(test.search(searchQuery,priceLimit))

username = "AustinAdmin"
password = "Purp13rain!"

myclient = pymongo.MongoClient("mongodb://%s:%s@localhost:27017/"% (username, password))

#Create Database called eBaySearchData
mydb = myclient["eBaySearchData"]


#collection = table in mongoDB
mycol = mydb[queryAndPrice]


#should make table for each user search query
dblist = myclient.list_database_names()

if "eBaySearchData" in dblist:
  print("The database exists.")


