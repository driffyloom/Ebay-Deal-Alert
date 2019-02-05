from flask import Flask, render_template, request
import pymongo
from eBayAPIPoller import eBaySearch

#templates are for html
#static folder is for js files
app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

#for connecting to localhost
#client = pymongo.MongoClient("mongodb://%s:%s@localhost:27017/"% ("AustinAdmin", "test"))

client = pymongo.MongoClient("mongodb://%s:%s@ds057862.mlab.com:57862/dealalertdb"%("AustinAdmin", "testPassword1"))

#localhost version
#mydb = client["eBaySearchData"]
mydb = client["dealalertdb"] 

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route('/<string:search>', methods=["PUT"])
def handle_search(search):
    print("TEST")
    #searchRequest = request.args.get('searchBar')
    print(search)
    return search

@app.route('/searchResults/<int:page>' , methods = ["POST","GET"])
def searchResults(page):
    #if(request.method == 'POST'):
    search = request.form['searchBar']
    priceLimit = request.form['priceLimit']
    #if(request.method == 'GET'):
    eBayAPIPoller = eBaySearch("AustinCh-DealAler-SBX-a39332c51-8b41e853")

    eBayAPIPoller.addResultsToDB(eBayAPIPoller.search(search,priceLimit))
    collectionName = search + priceLimit
    mycol = mydb[collectionName]
    data = mycol.find().skip((page-1)*20).limit(20)

    return  render_template("searchResults.html",data = data)

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()