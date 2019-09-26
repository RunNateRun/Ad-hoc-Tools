#!/bin/python
import multiprocessing as mp
import traceback
import sys
import os
pool = mp.Pool(mp.cpu_count())

def readfile(passtext):
	lineList = [line.rstrip('\n') for line in open(passtext)]
	return lineList


def appendString(startList):
	#Need to create function to allow user to modify leading text.
	authList = ['admin:' + p for p in startList]
	return convertB64(authList)

def convertB64(authList):
 	convertList = []
 	for i in authList:
 		convertText = i.encode('base64', 'strict').rstrip('\n')
 		#Need to create another function to allow user to specify output method stdout/file
        #convertList.append(convertText)
 		print >>outFile, convertText


if os.path.exists("output.txt"):
	os.remove("output.txt")
	print("Starting...")

try:
	outFile = open('output.txt','w')
	startFile = readfile(sys.argv[1])
	pool.apply(appendString(startFile))
except Exception as e:
	print('Complete!')

pool.close()
