content = open('finalSent.txt','r').readlines()

content_set = set(content)

cleandata = open('finalSent1.txt','w')

for line in content_set:
	cleandata.write(line)