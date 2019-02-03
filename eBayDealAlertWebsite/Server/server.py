from flask import Flask, render_template, request
import pymongo

#templates are for html
#static folder is for js files
app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
client = pymongo.MongoClient("mongodb://%s:%s@localhost:27017/"% ("AustinAdmin", "test"))
mydb = client["eBaySearchData"]

@app.route("/")
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
    default_name = '0'
    data = request.form.get('searchBar', default_name)
    print(data)

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()