import csv
import json

with open('global_sales.csv', "r", encoding="UTF-8") as file:
    global_sales = list(csv.DictReader(file))
    print(global_sales)

with open("regional_tariffs.json", "r", encoding="UTF-8") as file:
    regional_tariffs = json.load(file)
    print(regional_tariffs)
