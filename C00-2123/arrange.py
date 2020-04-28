import pandas as pd
import csv

filepath1 = 'file2.csv'
filepath2 = 'finalSent1.txt'
outpath = 'outSentence.csv'
 	
df1 = pd.read_csv(filepath1)

lst = open(filepath2).readlines()
list2 = []
for line in lst:
	line = line.strip().lower()
	list2.append(line)
print('.................Length = ',len(list2))
# with open
# df3 = pd.read_csv('newCSV.csv')
with open(outpath,'w', newline = '')as f:
	thewriter = csv.writer(f)
	listRow = ['id', 'sentence']
	thewriter.writerow(listRow)
	
	for cnt, line in df1.iterrows():
		if line['value'].strip().lower() in list2:
			thewriter.writerow([cnt+2,line['value'].capitalize()])



