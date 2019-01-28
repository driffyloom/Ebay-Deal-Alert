from bs4 import BeautifulSoup
from ebaysdk.finding import Connection as Finding

searchQuery = input("What are you searching for? (Using eBay Sandbox!)");

#eventually need to get rid of and get past item data
priceLimit = input("Price Limit? (Using eBay Sandbox)");

api = Finding(domain='svcs.sandbox.ebay.com', appid="AustinCh-DealAler-SBX-a39332c51-8b41e853", config_file=None)
api_request = {'keywords':searchQuery, 'outputSelector': 'SellerInfo', 'sortOrder': 'PricePlusShippingLowest'}

response = api.execute('findItemsAdvanced',api_request)
#find

soup = BeautifulSoup(response.content, 'lxml')

totalentries = int(soup.find('totalentries').text)

items = soup.find_all('item')

for item in items:
    cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()
    #only works for non sandbox site
    try:
        image = item.galleryurl.string.lower()
    except AttributeError:
        print("No Image") 
    print(item)
    print('________')
    print('cat:\n' + cat + '\n')
    print('title:\n' + title + '\n')
    print('price:\n' + str(price) + '\n')
    print('url:\n' + url + '\n')
    input()
