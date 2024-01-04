import csv, json

csvFilePath = './blurb.csv'
jsonFilePath = 'blurb.json'

data = []
with open(csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile)
	for rows in csvReader:
		#print(rows['shortForm'])
		#id = rows['shortForm']
		data.append(rows)

with open(jsonFilePath, 'w+') as jsonFile:
	jsonFile.write(json.dumps(data, indent=4))
