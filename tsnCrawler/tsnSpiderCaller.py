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
	parser.add_argument("date", help="input a date: mm/dd/yr")
	args = parser.parse_args()
	print args.date
	
	#first delete boxsoreAddressList from previous executions
	try:
   		os.remove("boxscoreAddressList.json")
	except OSError:
		pass
	
	##execute call to scrapy
	##with date and output file as parameters
	execString = ("scrapy crawl tsn -a date=%s -o boxscoreAddressList.json" % args.date)
	cmdline.execute(execString.split())

if __name__ == "__main__":
    main()