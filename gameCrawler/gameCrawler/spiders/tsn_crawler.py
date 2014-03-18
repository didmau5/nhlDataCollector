from scrapy.spider import Spider
from scrapy.selector import Selector
from gameCrawler.items import TsncrawlerItem
from datetime import date, timedelta


#given a list of dates mm/dd/yr, returns a list of urls
def formatUrl(dates):
	
	return ['http://www.tsn.ca/nhl/scores/?date=%s' % dates]

#given a start and end date, returns a list of daten in between
#(inclusive of start and end)
def getDates(start, end):
	
	startSplit = start.split('/')
	endSplit = end.split('/')

	#add 20 to 14 for 2014
	#strip leading 0s of day and month
	d1 = date(2014,3,3)
	d2 = date(2014,3,9)

	delta = d2 - d1

	for i in range(delta.days + 1):
	    	print d1 + timedelta(days=i)

	return start

class TsnSpider(Spider):
    name = "tsn"
    allowed_domains = ["tsn.ca"]
    
    #date passed as parameter for start url
    def __init__(self, startDate=None, endDate = None, *args, **kwargs):
        super(TsnSpider, self).__init__(*args, **kwargs)
        
        #get dates
        dates = getDates(startDate, endDate)
        urls = formatUrl(dates)
        #set returned list to start_urls
        self.start_urls = urls


    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//body/form/div/div')
        items = []
        for site in sites:
        	#initialize crawler
            item = TsncrawlerItem()
            #get date
            date = site.xpath('//div/h1/text()').extract()
            item['date'] = [date[0].strip('\n\r ')]
            # gather links
            item['link'] = site.xpath('//div/div/div/div/p/a/@href').extract()
            items.append(item)

        return items
        