#!/usr/bin/env
import requests
from bs4 import BeautifulSoup
import string
import urllib
import re

def printHeader():

	print "\n\n==================="
	print "NHL DATA COLLECTOR"
	print "===================\n\n"
	

def main():

	printHeader();

	url = 'http://www.tsn.ca/nhl/scores/boxscore/?id=18815'
	
	#get page
	r = requests.get(url)

	#find Scoring Summary 
	pattern = re.compile('Scoring Summary')
	scoringSummaryFound = pattern.search(r.text)
	
	#if page has Scoring Summary section
	#(some urls dont provide a scoring summary)
	if scoringSummaryFound != None:
	

		###USE BEAUTYSOUP TO EXTRACT TABLES	
		
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html)
		
		
		
		for table in soup.find_all('table'):
		
			##FOR EACH TABLE FOUND FIND <tbody> TAGS
			for tbody in table.find_all('tbody'):
		
				#RE:href=re.compile('/nhl/teams/players/bio/\?name=[(\w+)]+[(\w+)]'
				#a_tag = tbody.find_all(href=re.compile("/nhl/teams/players/bio/\?name=[a-zA-Z+]+[a-zA-Z+]"))
		
				###FOR EACH <a> TAG FOUND, LOOK FOR (INT) IMMEDIATELY FOLLOWING PLAYER NAME
				###THEN COLLECT EVERYTHING BETWEEN ROUND PARAENTHESIS
				#for a_tag_found in a_tag:

				##FOR EACH TBODY FOUND FIND <td> TAG
				for td in tbody.find_all('td'):
				
					##FOR EACH <td> TAG FIND SOMETHING OF THE FORM HREF(HREF,HREF)
					a_tag = td.find_all(href=re.compile('/nhl/teams/players/bio/\?name=[a-zA-Z+]+[a-zA-Z+]'));
					
					for player in a_tag:
						#If 3, two players assisted, if 2, one player assisted, if 1, no one assisted
						numInvolvedPlayers =  len(a_tag)
						playerString = str(player.contents)
						#if player string contains this, the player scored a goal
						if (playerString.find("(") > 0):
							print playerString
							print numInvolvedPlayers
						
		
		###USE BEAUTYSOUP TO EXTRACT ALL PLAYER NAMES BETWEEN <a> TAGS

if __name__ == "__main__":
    main()