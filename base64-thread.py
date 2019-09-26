#!/bin/python
import multiprocessing as mp
import sys
#print("Number of processors: ", mp.cpu_count())
pool = mp.Pool(2)

outFile = open('output.txt','w')

def readfile(passtext):
	lineList = [line.rstrip('\n') for line in open(passtext)]
	#print(lineList)
	return appendString(lineList)

def appendString(lineList):
	authList = ['admin:' + p for p in lineList]
	#print(authList)
	return convertB64(authList)

def convertB64(authList):
	convertList = []
	for i in authList:
		convertText = i.encode('base64', 'strict').rstrip('\n')
		convertList.append(convertText)
		print >>outFile, convertText
		#print(convertList) 

results = pool.apply(readfile(sys.argv[1]))

pool.close()
#print(results)