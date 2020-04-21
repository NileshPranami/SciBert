import pandas as pd
import csv

filename = 'file2.csv'
outpath = 'output3.csv'
df = pd.read_csv(filename)


with open(outpath,'w', newline = '') as f:
	thewriter = csv.writer(f)

	thewriter.writerow(['paper_title','value'])
	for index, line in df.iterrows():
		# print(index, line)
		
		# sent.append(line['paper_title'])
		sent = line['value'].lower().split('. ')
		for line1 in sent:
			print(line1)
			if len(line1) < 15:
				print('__________________________________________')
				continue
			sent = (line['paper_title'], line1.strip())
			# sent.append()
			thewriter.writerow(sent)
			
		
f.close()