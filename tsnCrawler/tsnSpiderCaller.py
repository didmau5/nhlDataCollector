#!/usr/bin/env
from scrapy import cmdline



def main():

	##generate range of dates

	##execute call to scrapy
	cmdline.execute("scrapy crawl tsn -a date=03/13/14".split())

if __name__ == "__main__":
    main()