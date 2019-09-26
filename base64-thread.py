#!/bin/python
import multiprocessing as mp
import sys
pool = mp.Pool(mp.cpu_count())

outFile = open('output.txt','w')

def readfile(passtext):
	lineList = [line.rstrip('\n') for line in open(passtext)]
	return appendString(lineList)

def appendString(lineList):
        #Need to create function to allow user to modify leading text.
        authList = ['admin:' + p for p in lineList]
	return convertB64(authList)

def convertB64(authList):
	convertList = []
	for i in authList:
		convertText = i.encode('base64', 'strict').rstrip('\n')
		#Need to create another function to allow user to specify output method stdout/file
                #convertList.append(convertText)
		print >>outFile, convertText

results = pool.apply(readfile(sys.argv[1]))

pool.close()

