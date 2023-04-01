import csv 

with open('data/test-questions.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
       print(row[9])