#!/usr/bin/env python
#	\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#	
#	 Date : March 27,2014	
#	 Author : Daniel Mow
#	 Email : mow.daniel@gmail.com
#	 Purpose : binarize a data file and output to csv file
#				(account for symmetry of data)
#			   
#	
#	////////////////////////////////////////////////////////////////

import argparse
import csv


def getArgs():

	parser = argparse.ArgumentParser()
	parser.add_argument("data", help="input filename to binarize")
	args = parser.parse_args()
	return args.data


def getScorersDict(fp):

	## for each scorer
	##		make list of assisters
	dict = []
	
	for line in fp:
		if("id,team,scorer,assist1,assist2" not in line):
			separatedLine = line.strip('\r\n').split(',')
			team = separatedLine[1]
			scorer = separatedLine[2]
			assisters = separatedLine[3:]
			dictEntry = {'team':team, 'scorer':scorer, 'assisters':assisters}
			dict.append(dictEntry)
		
	return dict

def checkUniqueAssister(assisters, checkAssister):
	
	if(checkAssister in assisters):
		return 0
	else:
		return 1

def getAssisterList(scorers):

	assisterList = []
	for entry in scorers:
		for assister in entry['assisters']:
			if (checkUniqueAssister(assisterList, assister) and (assister != '')):
				assisterList.append(assister)
	return assisterList

def checkUniqueScorer(scorers, checkScorer):
	
	if(checkScorer in scorers):
		return 0
	else:
		return 1

def getScorerList(scorers):

	scorerList = []
	for entry in scorers:		
		if(checkUniqueScorer(scorerList, entry['scorer'])):
			scorerList.append(entry['scorer'])
				
	return scorerList

def makeHeader(elements):

	header = ['id','team','scorer']
	for element in elements:
		header.append(element)
	return header
	

def makeRow(dict, scorer, aList, i):

	
	
	aCountList = [0] * len(aList)

	for entry in dict:
		if(entry['scorer'] == scorer):
			team = entry['team']
			for assister in aList:
				for assist in entry['assisters']:
					if(assist == assister):
						aCountList[aList.index(assister)] += 1
	
	row = []
	row.append(i)
	row.append(team)
	row.append(scorer)
	for entry in aCountList:
		row.append(entry)
	return row

def main():
	
	## open data file to binarize
	dataFileName = getArgs()
	dataFp = open(dataFileName,'r')
	
	## open csv file to write binarized data to
	writeFileName = dataFileName.strip(".csv") + "_binarized.csv"
	writeFp = open(writeFileName, 'wb')
	
	
	## make dict of scorers
	scorersDictionary = getScorersDict(dataFp)
	#print scorersDictionary

	
	assisterList = getAssisterList(scorersDictionary)
	#print assisterList
	scorersList = getScorerList(scorersDictionary)
	#print scorersList
	
	
	## MAKE ROW
	header = makeHeader(assisterList)
	
	## write header
	wr = csv.writer(writeFp)
	
	#write attributes
	wr.writerow(header)	
	
	## for each scorer
	## 		find assisters and insert 1 in appropriate entry
	i = 1
	for scorer in scorersList:
		row = makeRow(scorersDictionary, scorer, assisterList,i)
		i+=1
		## write row
		wr.writerow(row)



if __name__ == "__main__":
    main()
    
