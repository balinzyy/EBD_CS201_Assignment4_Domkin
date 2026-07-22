import csv
import json

with open('global_sales.csv', "r", encoding="UTF-8") as file:
    global_sales = list(csv.DictReader(file))
    print(global_sales)


with open("regional_tariffs.json", "r", encoding="UTF-8") as file:
    regional_tariffs = json.load(file)
    print(regional_tariffs)

for row in global_sales:
    for column in ['quantity', 'revenue']:
        if row.get(column) == "N/A" or not row.get(column):
            row[column] = 0.0
        else:
            row[column] = float(row[column])

print(global_sales)

for region, tarrif in regional_tariffs.items():
    if tarrif == 'N/A':
        regional_tariffs[region] = 0.0
    else:
        regional_tariffs[region] = float(tarrif)

print(regional_tariffs)

for i in global_sales:
    net_profit = i["revenue"] - i["revenue"] * (regional_tariffs[i["region"]]/100)
    i["net_profit"] = net_profit

print(global_sales)








