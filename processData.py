#!/usr/bin/env
import requests
from bs4 import BeautifulSoup
import string
import urllib
import re

def main():

	url = 'http://www.tsn.ca/nhl/scores/boxscore/?id=18815'
	
	#f = open("NormalizedPlayerData.csv", 'r+');
	r = requests.get(url)
	
	for line in r:
	
		#for first line set attributes
	
		#for every other line, if new team, add new line in file
		#start sum of 
		pattern = re.compile('Scoring Summary')
		found = pattern.search(line)
		if found != None:
			print found.group()
		
		
	###USE BEAUTYSOUP TO EXTRACT TABLES	
		
	#html = urllib.urlopen(url).read()
	#soup = BeautifulSoup(html)
	#tables = soup.find_all('table')
	#print tables


if __name__ == "__main__":
    main()