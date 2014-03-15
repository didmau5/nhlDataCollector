#!/usr/bin/env
import requests
from bs4 import BeautifulSoup
from scrapy.selector import Selector
import string
import urllib
import re
import json
import os
from scrapy import cmdline
import argparse

def printHeader():

	print "\n\n==================="
	print "NHL DATA COLLECTOR"
	print "===================\n\n"
	

#appends domain to url
#returns a formatted list of urls
def cleanItems(items):

	urls = []
	for elem in items['link']:
		url = "http://www.tsn.ca%s" % elem 
		urls.append(url)
	return urls


def getGoalData(soup):

	goals = []

	#for each <table> tab
	for table in soup.find_all('table'):
		#for each <tbody> tab
		for tbody in table.find_all('tbody'):
			#for each <td>
			for td in tbody.find_all('td'):
				a_tag = td.find_all(href=re.compile('/nhl/teams/players/bio/\?name=[a-zA-Z+]+[a-zA-Z+]'));
				
				#TEST PRINT ALL a_tag
				#print a_tag
				
				for player in a_tag:
					#If 3, two players assisted, if 2, one player assisted, if 1, no one assisted
					numInvolvedPlayers =  len(a_tag)
					playerString = str(player.contents)
					#if player string contains this, the player scored a goal
		
					if (playerString.find("(") > 0):
						dictEntry = {'scorer':playerString, 'assists':[], 'numPlayers':numInvolvedPlayers}
						goals.append(dictEntry)
	return goals					

def printGoalData(data):

	print ('NEW GAME\n')
	for entry in data:
		print entry

def main():

	printHeader();
	
	#open file in sub-directory
	for filename in os.listdir("tsnCrawler"):
		f = open(os.path.join("tsnCrawler", "boxscoreAddressList.json"), "r")

	#TESTPRINT
	items = json.load(f)
	
	
	#get URLS from json object
	urls = cleanItems(items)
	#TEST PRINT URLS
	print urls
	
	cd = os.getcwd()
	os.chdir("%s/tsnCrawler/"% cd)


	#visit each url
	for url in urls:
	
		#get page
		r = requests.get(url)

		#find Scoring Summary 
		pattern = re.compile('Scoring Summary')
		scoringSummaryFound = pattern.search(r.text)
		#if page has Scoring Summary section
		#(some urls dont provide a scoring summary)
		if scoringSummaryFound != None:
		
	
			#use beautifulsoup to read html
			html = urllib.urlopen(url).read()
			soup = BeautifulSoup(html)
			
			goalData = getGoalData(soup)
			printGoalData(goalData)
			
		
			
			###USE BEAUTYSOUP TO EXTRACT ALL PLAYER NAMES BETWEEN <a> TAGS

if __name__ == "__main__":
    main()