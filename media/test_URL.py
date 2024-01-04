from bs4 import BeautifulSoup
import re, requests, csv, json, sys

csvFilePath = './news.csv'
jsonFilePath = './news.json'

headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    # Add more headers as needed
}

def imageSelector(tag):
    return tag.name == "meta" and tag.has_attr("property") and "og:image" == tag.get("property")

def titleSelector(tag):
    return tag.name == "meta" and tag.has_attr("property") and "og:title" == tag.get("property")

def timeSelector(tag):
    return (tag.name == "meta" and tag.has_attr("property") and ("_time" in tag.get("property"))) | (tag.name == "time" and tag.has_attr("datetime"))




response = requests.get(sys.argv[1], headers=headers, cookies = {'CONSENT' : 'YES+'} )
if response.status_code != 200:
    print("Error fetching page")
    print(response.status_code)

else:
    content = response.content
    
    soup = BeautifulSoup(response.content, 'html.parser') 
    
    try:
        print(soup.title.string)
    except:
        print("Couldn't find title")
    
    try:
        print(soup.find(timeSelector).get("content"))
    except:
        print("couldn't get date from content")
    try:
        print(soup.find(timeSelector).get("datetime"))
    except:
        print("couldn't get date from datetime")


    try:
        print(soup.find(imageSelector).get("content"))
    except:
        print("couldn't get image from content")
