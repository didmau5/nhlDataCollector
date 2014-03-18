#!/usr/bin/env
from scrapy import cmdline
import argparse
import os

##needs to iterate over a range of valid dates

def main():

	##todo
	##generate range of dates
	
	#parse date arguement
	parser = argparse.ArgumentParser()
	parser.add_argument("startDate", help="input a start date: mm/dd/yr")
	parser.add_argument("endDate", help="input an end date: mm/dd/yr")
	args = parser.parse_args()
	print args
	
	#first delete boxsoreAddressList from previous executions
	try:
   		os.remove("boxscoreAddressList.json")
	except OSError:
		pass
	
	##execute call to scrapy
	##with date and output file as parameters
	##writes to JSON object boxscoreAddressList
	execString = ("scrapy crawl tsn -a startDate=%s -a endDate=%s " % (args.startDate, args.endDate))
	#execString = ("scrapy crawl nhl -o boxscoreAddressList.json")
	cmdline.execute(execString.split())

if __name__ == "__main__":
    main()
    