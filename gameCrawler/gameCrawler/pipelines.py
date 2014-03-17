import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

DATE_PATTERN_STRING = "(\w)*,? ?[(\w)(\w)(\w)](\w)*,? (\d)(\d)?,? '?(\d)(\d)[(\d)(\d)]?"

class GamecrawlerPipeline(object):
 			

    def process_item(self, item, spider):
    	
    	##filter out boxscore(tsn) and htmlreport(nhl) links
    	if (item['link']):
    		boxscoreLinks = []
    		for link in item['link']:
    			#tsn boxscore
    			if ("/nhl/scores/boxscore" in link):
    				boxscoreLinks.append(link)
    			#nhl html game report
    			if ("/scores/htmlreports" in link):	
    				boxscoreLinks.append(link)
    		item['link'] = boxscoreLinks

    	#check if actually date(Mar 13 '14) with regex
		if (item['date']):
 			dates = []
 			for date in item['date']:
				#check if actually date(Mar 13 '14) OR (Monday, March 13, 2014) with regex
				if (re.match(DATE_PATTERN_STRING, date) is not None):
					dates.append(date)
			item['date'] = dates
		return item