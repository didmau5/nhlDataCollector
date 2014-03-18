import re
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

DATE_PATTERN_STRING = "(\w)*,? ?[(\w)(\w)(\w)](\w)*,? (\d)(\d)?,? '?(\d)(\d)[(\d)(\d)]?"

class GamecrawlerPipeline(object):
	def __init__(self):
		dispatcher.connect(self.spider_opened, signals.spider_opened)
		dispatcher.connect(self.spider_closed, signals.spider_closed)
		self.files = {}
		
	def spider_opened(self, spider):
		file = open('gameCrawlerItems.json', 'w+b')
		self.files[spider] = file
		self.exporter = JsonItemExporter(file)
		self.exporter.start_exporting()
		
	def spider_closed(self, spider):
		self.exporter.finish_exporting()
		file = self.files.pop(spider)
		file.close()
		
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
		self.exporter.export_item(item)
		return item
