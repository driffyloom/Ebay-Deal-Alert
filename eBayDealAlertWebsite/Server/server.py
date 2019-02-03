from flask import Flask, render_template, request
import pymongo

#templates are for html
#static folder is for js files
app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
client = pymongo.MongoClient("mongodb://%s:%s@localhost:27017/"% ("AustinAdmin", "test"))
mydb = client["eBaySearchData"]

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

@app.route('/somewhere' , methods = ["POST","GET"])
def some_page():
    search = request.form['searchBar']
    mycol = mydb["iphone200"]
    data = mycol.find()

    return  render_template("searchResults.html",data = data)

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()