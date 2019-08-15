import requests
import json
import csv

url = "http://makeup-api.herokuapp.com/api/v1/products.json"
response = requests.get(url).json()
data = json.dumps(response, indent=4, sort_keys=True)
print(type(data))
print(data)

# Save to a json file
file = open('makeup_data.json', encoding='utf-8', mode='w')
json.dump(data, file)
file.close()

# Save to a csv file
products = json.loads(data)
products_data = open('products.csv', 'w', newline='', encoding='utf-8')

csvwriter = csv.writer(products_data)
count = 0
for pro in products:
    if count == 0:
        header = pro.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(pro.values())

products_data.close()





