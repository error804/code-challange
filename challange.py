#!/bin/python

import random


givenString ="{I am|I'm} {working on|starting} this {online |}interview. I hope Cortx thinks I am{{very|extremely} qualified|great|awesome}{!|.}"

# function to split the given string by '}' and add it to the list
def getRandomWord(inputString):
	inlist = []
	value = inputString.split('}')
	for i in value:
		if i != "":
			inlist.append(i.strip())

	return inlist


# function to create the final list from the initial list and make a nested list by separating with '|'
def dataClean(dlist):
	finalList = []
	for i in range(len(dlist)):
		
		# spliting the value 
		if '|' in dlist[i]:
			finalList.append(dlist[i].split('|'))
		else:
			for i in dlist[i]:
				if '|' in i and i[1] != "":
					finalList.append(i.split('|'))
				else:
					# handling the empty element in the list
					if len(i) > 0:
						temp = []
						temp.append(i)
						finalList.append(temp)
	return finalList


		
clist = getRandomWord(givenString)

flist = []
for i in clist:
	if i[0] == '{':
		flist.append(i.replace('{',''))
	else:
		flist.append(i.split('{'))



def display(opts):
	output= []
	for i in range(len(opts)):
		#print opts[i]
		output.append(random.choice(opts[i]).strip())

	print ' '.join(output)


#print dataClean(flist)
display(dataClean(flist))

