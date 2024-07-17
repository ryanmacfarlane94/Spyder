from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pymongo import MongoClient

#https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

def save_page(store, url, page_source):
    pages = database["pages"]
    page = {
        "store": store,
        "url": url,
        "content": page_source
    }

    id = pages.update_one(
        {"store":1, "url":url},
        { "$set": page },
        upsert=True)
    print(id)

def get_content(url):
    driver.get("https://stage2-www.zumiez.com" + url)
    time.sleep(5)
    driver.execute_script("""
        for(let script of document.querySelectorAll('link[rel="preload"]')) script.remove()
    """)
    driver.execute_script("""
        for(let script of document.querySelectorAll('script')) script.remove()
    """)
    
    page_source = driver.page_source
    return page_source


 
# Connect to the MongoDB database
mongodb_client = MongoClient("mongodb://localhost:27017")
database = mongodb_client["spyder"]
print("Connected to the MongoDB database!")

# Create a new Chrome WebDriver instance
options = Options()
options.add_argument("--headless=new")
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

url = "/shoes.html"
page_source = get_content(url)
save_page(1, url, page_source)

driver.quit()
exit()

url = "/womens"
page_source = get_content(url)
save_page(1, url, page_source)

url = "/womens/tops/t-shirts.html"
page_source = get_content(url)
save_page(1, url, page_source)

fileToWrite = open("page_source.html", "w")
fileToWrite.write(page_source)
fileToWrite.close()

url = "/ed-hardy-flaming-skull-black-crop-t-shirt.html"
page_source = get_content(url)
save_page(1, url, page_source)

url = "/womens"
page_source = get_content(url)
save_page(1, url, page_source)

url = "/shoes.html"
page_source = get_content(url)
save_page(1, url, page_source)
 
# Close the browser window
driver.quit()
