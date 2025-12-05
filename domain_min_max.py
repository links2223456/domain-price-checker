import csv
from collections import defaultdict

input_file = "domains.csv"
output_file = "result.csv"

prices = defaultdict(list)

with open(input_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    
    for row in reader:
        domain = row[0].strip()
        price = float(row[1])
        prices[domain].append(price)

with open(output_file, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["domain", "min_price", "max_price"])

    for domain, pr in prices.items():
        writer.writerow([domain, min(pr), max(pr)])

print("Готово! Результат в result.csv")
