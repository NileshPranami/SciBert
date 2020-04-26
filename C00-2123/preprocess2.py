import csv
inputFile = 'file2.csv'
outputFile = 'file22.csv'

with open(inputFile) as in_file:
    with open(outputFile, 'w') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                writer.writerow(row)
