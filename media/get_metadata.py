from bs4 import BeautifulSoup
import re
import requests
import csv, json

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



data = []
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    idCount = 0
    for rows in csvReader:
        
        print(rows)
        response = requests.get(rows['URL'], headers=headers)
        if response.status_code != 200:
            print("Error fetching page")
            print(response.status_code)

        else:
            content = response.content
            
            soup = BeautifulSoup(response.content, 'html.parser') 
            
            if not (rows['Title']):
                try:
                    rows['Title'] = soup.title.string
                except:
                    print("Couldn't find title")
                    rows['Title'] = "unknown title"
                
            try:
                Date1 = soup.find(timeSelector).get("content")
            except:
                Date1 = None
            try:
                Date2 = soup.find(timeSelector).get("datetime")
            except:
                Date2 = None


            if Date1:
                rows['Date'] = Date1
                print("Added date 1: " + Date1)
            elif Date2:
                rows['Date'] = Date2
                print("Added date 2: " + Date2)
            elif rows['Date'] == "":
                rows['Date'] == "2022-01-01"

            if not (rows['Image']):
                try:
                    rows['Image'] = soup.find(imageSelector).get("content")
                    if (rows['Image'] == None):
                        rows['Image'] = "https://www.mappingfossilties.org/media/placeholder.png"
                except:
                    rows['Image'] = "https://www.mappingfossilties.org/media/placeholder.png"


        rows['id'] = idCount
        idCount = idCount+1
        data.append(rows)
        

with open(jsonFilePath, 'w+') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))












#response = requests.get("https://nos.nl/collectie/13940/artikel/2481064-ontroering-en-lof-maar-ook-kritiek-op-vergiffenis-toespraak-van-koning")
#response = requests.get("https://www.bbc.com/news/world-australia-66309637")
#response = requests.get("https://www.rtlnieuws.nl/nieuws/nederland/artikel/5386970/extinction-rebellion-a12-blokkade-klimaat-protest")
#response = requests.get("https://www.delta.tudelft.nl/article/beraadslaging-over-fossiele-banden-tu-ik-heb-mijn-mening-bijgesteld")
#response = requests.get("https://www.nwo.nl/en/news/nwo-debate-series-cancel-companies-id-rather-work-together")





#print(soup.title.string)
#print(soup.find_all('meta'))
#print(soup.find_all('time'))
#print(soup.find(imageSelector).get("content"))
#print(soup.find(titleSelector).get("content"))
#print(soup.find(timeSelector).get("content"))
#print(soup.find(timeSelector).get("datetime"))
#print(soup.img)

#<meta content="https://cdn.nos.nl/image/2023/07/01/983045/1024x576a.jpg" property="og:image">
