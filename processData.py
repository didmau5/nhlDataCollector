#!/usr/bin/env python
#	\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#	
#	 Date : March 18,2014	
#	 Author : Daniel Mow
#	 Email : mow.daniel@gmail.com
#	 Purpose : Processes the JSON object containing scoresheet links
#			   and retreives goal data.
#	
#	////////////////////////////////////////////////////////////////

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
import csv

MAX_NUM_ASSISTERS = 2
PLAYER_PATTERN = '(\d)(\d)? (\w).(\w)+\((\d)(\d)?\)'

###	print program header
def printHeader():
	line = "=" * 50
	print("\n\n")
	print(line)
	print("++++         -- NHL DATA COLLECTOR --         ++++")
	print(line)
	print("\n\n")
	
###	opens list of boxscore addresses
def openJsonFile():
	#open file in sub-directory
	for filename in os.listdir("gameCrawler"):
		f = open(os.path.join("gameCrawler", "gameCrawlerItems.json"), "r")
	return json.load(f)


###	appends domain to link
###	returns a formatted list of urls
def cleanItems(item):
	urls = []
	for elem in item['link']:
		url = "http://www.tsn.ca%s" % elem 
		urls.append(url)
	return urls

###		WORKING HERE    #####

###	returns list of game data given an nhl gamesheet html page
###	extracts scorer, assisters, and number of players involved in the goal
def getNhlGameData(soup):

	#conatins dictionary entries of each goal data
	#(per game/per boxscore sheet)
	goals = []
	
	##get players involved
	for td in soup.find_all(align='left'):
		for contents in td.contents:
			if (re.match(PLAYER_PATTERN, str(contents)) is not None):
				print contents
				
				#team field possible?
#				dictEntry = {'team':'', 'scorer':'','assists':[],'num_players':0}


				#TEST PRINT ALL a_tag
				#print a_tag
				
#				for player in a_tag:
					#If 3, two players assisted, if 2, one player assisted, if 1, no one assisted
#					numInvolvedPlayers =  len(a_tag)
#					playerString = str(player.contents[0])
					
					#if player string contains this, the player scored a goal
#					if (playerString.find("(") > 0):
#						dictEntry['scorer'] = playerString.rstrip('0123456789() ')
#						dictEntry['num_players'] = numInvolvedPlayers
						#the following remaining items are assisters
#						for assister in a_tag[1:]:
#								playerString = str(assister.contents[0])
#								dictEntry['assists'].append(playerString)
						#append to goals list
#						goals.append(dictEntry)
	return goals	

###	returns list of game data given a tsn boxscore html page
###	extracts scorer, assisters, and number of players involved in the goal
def getTsnGameData(soup):

	#conatins dictionary entries of each goal data
	#(per game/per boxscore sheet)
	goals = []
	
	#for each <table> tab
	for table in soup.find_all('table'):
		#for each <tbody> tab
		for tbody in table.find_all('tbody'):
			#for each <td>
			for td in tbody.find_all('td', 'alignLeft'):

				a_tag = td.find_all(href=re.compile('/nhl/teams/players/bio/\?name=[a-zA-Z+]+[a-zA-Z+]'));
				
				#team field possible?
				dictEntry = {'team':'', 'scorer':'','assists':[],'num_players':0}


				#TEST PRINT ALL a_tag
				#print a_tag
				
				for player in a_tag:
					#If 3, two players assisted, if 2, one player assisted, if 1, no one assisted
					numInvolvedPlayers =  len(a_tag)
					playerString = str(player.contents[0])
					
					#if player string contains this, the player scored a goal
					if (playerString.find("(") > 0):
						dictEntry['scorer'] = playerString.rstrip('0123456789() ')
						dictEntry['num_players'] = numInvolvedPlayers
						#the following remaining items are assisters
						for assister in a_tag[1:]:
								playerString = str(assister.contents[0])
								dictEntry['assists'].append(playerString)
						#append to goals list
						goals.append(dictEntry)
	return goals					

###	given game data, prints it
def printGameData(data,date):
	line ='=' * 75
	stars = '*' * len(line)
	print(line)
	print ('||		NEW GAME:	%s		||' % str(date))
	print(stars)
	for entry in data:
		print entry
	print(stars)
	print(line)
	print('\n')

###	print log of program
def printReport(data):

	#sum all goals
	numGoals = 0
	for game in data:
		numGoals += len(game)
	
	print("%d goals recorded" % numGoals)
	print("%d games examined" % len(data))

# given list of game data
# outputs to csv file
def writeGameData(data):

	fp = open('goalData.csv', 'wb')
	wr = csv.writer(fp)
	
	#write attributes
	wr.writerow(['scorer','assist1', 'assist2'])
	
	for goal in data:
		row = []
		for attr in goal:
			if ('scorer' in attr):
				row.append(goal[attr].replace("'", ""))
			if('assists' in attr):
				#fill in NULL attributes
				#less than 2 assisters
				for assister in goal[attr]:
					row.append(assister.replace("'", ''))				
				if(len(goal[attr]) < MAX_NUM_ASSISTERS):
					for i in range(MAX_NUM_ASSISTERS-len(goal[attr])):
						row.append('')
		#put scorer to front of row
		row = [row[2]]+row[:2]
		print row
		wr.writerow(row)

def main():

	printHeader()
	
	#open JSON file containing scraped links
	items = openJsonFile()

	#holds all goal info
	allGameData = []

	#indicator flag: tsn = 0 ,nhl =1
	tsnOrNhl = 0

	#for each date
	for item in items:
		#set date
		date = item['date']
		
		#form URLs if they are scraped from tsn (not from nhl)
		if ("http://www.nhl.com/scores/htmlreports" not in item['link'][0]):
			urls = cleanItems(item)
		else:
			tsnOrNhl = 1
			urls = item['link']
		
		numGames = len(urls)
		
		#TEST PRINT URLS
		#print urls
	
		#holds all game data returned by getGameData
		data = []
	
		#visit each url
		for url in urls:
		
			#use beautifulsoup to read html
			html = urllib.urlopen(url).read()
			soup = BeautifulSoup(html)	
			if(tsnOrNhl == 0 ):
				gameData = getTsnGameData(soup)
			else:
				gameData = getNhlGameData(soup)
			data.append(gameData)
		
		for game in data:
			#TEST PRINT GAME DATA
			printGameData(game, date[0])
			#append all goal data to all game data
			for goal in game:
				allGameData.append(goal)
		
		#print per day stats
		#printReport(data)
	
	#TEST PRINT ALL THE GAME DATA
	for i in allGameData:
		print i
	print len(allGameData)
	writeGameData(allGameData)
	
if __name__ == "__main__":
    main()