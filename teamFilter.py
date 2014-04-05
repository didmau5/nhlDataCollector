#!/usr/bin/env python
#	\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#	
#	 Date : March 27,2014	
#	 Author : Daniel Mow
#	 Email : mow.daniel@gmail.com
#	 Purpose : filter goal data by team and write to CSV
#			   
#	
#	////////////////////////////////////////////////////////////////



import argparse
import csv


def getArgs():

	parser = argparse.ArgumentParser()
	parser.add_argument("team", help="type three letter caps that represent team to filter for")
	args = parser.parse_args()
	return args.team

def main():
	
	team = getArgs()
	
	ID = 1

	#open csv file
	openFilename = "goalDataNHL2010_2011.csv"
	read_fp = open( openFilename ,'r')
	
	#create file <team>FilteredGoalData.csv
	filename = team + openFilename
	write_fp = open(filename, 'wb')
	wr = csv.writer(write_fp)
	
	#write attributes
	wr.writerow(['id','team','scorer','assist1', 'assist2'])	
	
	#for each line, if line[0] == args.team
	#write line to new file
	for line in read_fp:
		strippedLine = line.strip("\n,\r")
		#strip newline char
		separatedLine = strippedLine.split(",")
		for elem in separatedLine:
			if (len(separatedLine) < 4):
				for i in range (4 - len(separatedLine)):
					separatedLine.append("")
		if (separatedLine[0] == team):
			writeLine = separatedLine.insert(0, ID)
			wr.writerow(separatedLine)
			ID+=1
	else:
		pass


if __name__ == "__main__":
    main()
    