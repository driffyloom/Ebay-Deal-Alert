Goal:
Our goal is to create a deal alert for eBay that sends notifications by email whenever an item 
is listed at or below price we set.

1.) Select an item that closest matches what you are looking for 
2.) The API will poll for items that match category and are below price specified (or are a "deal"
in that it is a set percentage lower than average price)  
3.) Based on user preferences will send email out with found deals to user 


Current Objectives/In Progress:  

(DONE) Use Ebay API and parse through with key to get item data, return items below the price specified. (Austin) 
(DONE) Added VirtualEnv for python safety  
2.) Get familiar with flask for web app development. (Austin)  
3.) Get familiar with Amazon API? (Alex)  


To Do:  
1.) Choose times to send query and send email.  
2.) Create web app to send search to both Amazon and Ebay APIS  
3.) Create back-end for users to save searches and when this price was last at this price.  
4.) Maybe get past data or current data and if a certain percentage cheaper list it as well.  

https://developer.ebay.com/DevZone/finding/CallRef/types/ItemFilterType.html  

Currently Installed by pip  

- ebaySDK  
- BeautifulSoup4  
- request  
- virtualenv  
- pymongo  
- flask  
- mongoengine (for python object mapping to mongodb)  