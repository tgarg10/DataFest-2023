import csv

reader = csv.reader(open("C:\\Users\\tanis\\Downloads\\questionposts.csv", 'r', errors='replace'), delimiter=',')
writer = csv.writer(open("C:\\Users\\tanis\\Downloads\\newquestionposts.csv", 'w', errors='replace', newline=''), delimiter='|')
writer.writerows(reader)