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

	#open csv file
	read_fp = open( "goalData_all.csv" ,'r')
	
	#create file <team>FilteredGoalData.csv
	filename = team + "_FilteredGoalData.csv"
	write_fp = open(filename, 'wb')
	wr = csv.writer(write_fp)
	
	#write attributes
	wr.writerow(['team','scorer','assist1', 'assist2'])	
	
	#for each line, if line[0] == args.team
	#write line to new file
	for line in read_fp:
		strippedLine = line.strip("\n")
		#strip newline char
		separatedLine = strippedLine.split(",")
		if (separatedLine[0] == team):
			wr.writerow(separatedLine)
	else:
		pass
	
	#else
	#ignore


if __name__ == "__main__":
    main()
    