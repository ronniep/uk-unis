from bs4 import BeautifulSoup
import re
import requests
import csv, json

csvFilePath = './uniList.csv'
outputFilePath = './uniList.txt'


shortUniList = []
longUniList = []
with open(csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile)
	idCount = 0
	for rows in csvReader:
        
		shortUniList.append(rows['shortForm'])
		longUniList.append(rows['uni'])
        

with open(outputFilePath, 'w+') as txtFile:


	txtFile.write('      uniListFull: [{')
	for index in range(len(shortUniList)):
	    	txtFile.write('shortUni: "' + shortUniList[index] + '", longUni: "' + longUniList[index])
	    	if (shortUniList[index] != shortUniList[-1]):
	    		txtFile.write('"}, {')
	    		
	txtFile.write('"}],\n')
    
	txtFile.write('      desiredUni: ["')
	for uni in shortUniList:
	    	txtFile.write(uni)
	    	if (uni != shortUniList[-1]):
	    		txtFile.write('", "')
	    		
	txtFile.write('"]')



#      uniListFull: [{ shortUni: "NWO", longUni: "Dutch Research Council (NWO)" }, { shortUni: "EUR", longUni: "Erasmus Universiteit Rotterdam" }, { shortUni: "LU", longUni: "Universiteit Leiden" }, { shortUni: "OU", longUni: "Open Universiteit" }, { shortUni: "RUN", longUni: "Radboud Universiteit Nijmegen" }, { shortUni: "RUG", longUni: "Rijksuniversiteit Groningen" }, { shortUni: "TUD", longUni: "Technische Universiteit Delft" }, { shortUni: "TUe", longUni: "Technische Universiteit Eindhoven" }, { shortUni: "Til", longUni: "Tilburg University" }, { shortUni: "UM", longUni: "Maastricht University" }, { shortUni: "UT", longUni: "Universiteit Twente" }, { shortUni: "UU", longUni: "Universiteit Utrecht" }, { shortUni: "UvA", longUni: "Universiteit van Amsterdam" }, { shortUni: "VU", longUni: "Vrije Universiteit Amsterdam" }, { shortUni: "WUR", longUni: "Wageningen University & Research" }],
#      desiredUni: ["NWO", "EUR", "LU", "OU", "RUN", "RUG", "TUD", "TUe", "Til", "UM", "UT", "UU", "UvA", "VU", "WUR"],








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
