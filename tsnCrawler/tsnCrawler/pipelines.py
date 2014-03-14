# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class TsncrawlerPipeline(object):


	##filter out boxscore links
    def process_item(self, item, spider):
    	
    	boxscoreLinks = []
    	if (item['link']):
    		for link in item['link']:
    			if ("/nhl/scores/boxscore" in str(link)):
    				boxscoreLinks.append(link)
    		item['link'] = boxscoreLinks
    		return item