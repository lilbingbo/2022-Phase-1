import csv
with open('transmissions.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)