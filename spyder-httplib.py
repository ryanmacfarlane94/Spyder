import httplib2
from pymongo import MongoClient

mongodb_client = MongoClient("mongodb://localhost:27017")
database = mongodb_client["spyder"]
print("Connected to the MongoDB database!")

pages = database["pages"]
url = "/kids"

h = httplib2.Http(".cache")
resp, content = h.request("https://stage2-www.zumiez.com" + url, "GET")

page = {
    "store": 1,
    "url": url,
    "content": content.decode("utf-8")
}

id = pages.insert_one(page)

print(id)

fileToWrite = open("page_source.html", "wb")
fileToWrite.write(content)
fileToWrite.close()

mongodb_client.close()