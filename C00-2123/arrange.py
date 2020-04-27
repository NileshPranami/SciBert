import pandas as pd
import csv

filepath1 = 'file2.csv'
filepath2 = 'finalSent1.txt'
outpath = 'outSentence.csv'

# df2 = pd.read_csv(filepath1)
# df2.to_csv(r'newCSV.csv',index = True, index_label = 'id')

# def maxn(list1, N): 
#     final_list = [] 
  
#     for i in range(0, N):  
#         max1 = (0,0)
          
#         for j in range(len(list1)):      
#             if list1[j][0] > max1[0]: 
#                 max1 = list1[j]; 
                  
#         list1.remove(max1); 
#         final_list.append(max1) 
          
#     return final_list 		
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
			thewriter.writerow([cnt+2,line['value']])

# for cnt, line in df1.iterrows():
# 	# f5.write(str(cnt))
# 	list1 = list()
# 	list1.append(line['Comment'].lower())
# 	result = list()
# 	# df2 = pd.read_csv(filepath)
# 	for cnt1, line1 in df2.iterrows():
# 		#start  =  time()	
		
# 		list2 = list()

# 		list2.append(line1['value'].lower())	
# 		# print(list1)
# 		# print(list2)
# 		# sentence_obama = line.lower().split()
# 		# sentence_president = line1.lower().split()
# 		# sentence_obama = [w for w in sentence_obama]
# 		# sentence_president = [w for w in sentence_president]
# 		v1 = client.encode(list1)
# 		v2 = client.encode(list2)
# 		distance = cosine_similarity(v1, v2)

# 		#model.init_sims(replace=True)  # Normalizes the vectors in the word2vec class.
# 		#distance = model.wmdistance(sentence_obama, sentence_president)
# 		# f5.write('\t'+ str(distance))
# 		tu = (distance[0][0],line1["value"])
# 		result.append(tu)

# 		# print("Line {}: {}".format(cnt, list1))
# 		# print("Line {}: {}".format(cnt1, list2))
# 		# #print("distance b/w sentence cnt and cnt1  = %.3f" % distance )
# 		# #print('Cell took %.2f seconds to run.' % (time() - start))      
# 		print("-----------------------------------------") 		
		
# 	result = maxn(result,5)
# 	for line3 in result:
# 		f5.write('\t'+str(line3[1]))
# 		f5.write('\n')
# 	# f5.write('\t'+ str(result[1]))
# 	# f5.write('\n') 
# f5.close()		


# with open(filepath) as fp:
# 	for cnt, line in enumerate(fp):
# 		f5.write(str(cnt))
# 		result = list()
# 		with open(filepath) as fp1: 
# 			for cnt1, line1 in enumerate(fp1):
# 				#start  =  time()	
# 				list1 = list()
# 				list2 = list()
				
# 				list1.append(line.lower())
# 				list2.append(line1.lower())	
# 				print(list1)
# 				print(list2)
# 				# sentence_obama = line.lower().split()
# 				# sentence_president = line1.lower().split()
# 				# sentence_obama = [w for w in sentence_obama]
# 				# sentence_president = [w for w in sentence_president]
# 				v1 = client.encode(list1)
# 				v2 = client.encode(list2)
# 				distance = cosine_similarity(v1, v2)

# 				#model.init_sims(replace=True)  # Normalizes the vectors in the word2vec class.
# 				#distance = model.wmdistance(sentence_obama, sentence_president)
# 				# f5.write('\t'+ str(distance))
# 				tu = (distance,cnt1)
# 				result.append(tu)

# 				print("Line {}: {}".format(cnt, line))
# 				print("Line {}: {}".format(cnt1, line1))
# 				#print("distance b/w sentence cnt and cnt1  = %.3f" % distance )
# 				#print('Cell took %.2f seconds to run.' % (time() - start))      
# 				print("-----------------------------------------") 		
			
# 		result = maxn(result,5)
# 		f5.write('\t'+ str(result))
# 		f5.write('\n')
# f5.close()



