from scrapy.spider import Spider
from scrapy.selector import Selector
from gameCrawler.items import TsncrawlerItem
from datetime import date, timedelta


#given a list of dates mm/dd/yr, returns a list of urls
def formatUrl(dates):
	
	urls = []
	for elem in dates:
		dateList = str(elem).split('-')
		dateString = dateList[1] + '/' + dateList[2] + '/' + dateList[0]
		urls.append('http://www.tsn.ca/nhl/scores/?date=%s' % dateString)
	return urls

# cleans data info for forming a date for comparison
# returns a list of integers corresponding with the specified start and end dates
def cleanDate(start, end):

	#strip 0 from month and day
	monthDay = start[:2] + end[:2]
	cleanMonthDay = [i.lstrip('0') for i in monthDay]

	#add 20 to year
	year = [start[2]] + [end[2]] 
	cleanYear = ['20'+i for i in year]
	#return list in date() parameter order
	return[int(cleanYear[0])] + [int(cleanMonthDay[0])] + [int(cleanMonthDay[1])] + [int(cleanYear[1])] + [int(cleanMonthDay[2])] + [int(cleanMonthDay[3])] 
	

# given a start and end date, returns a list of dates in between
# (inclusive of start and end)
# date comparison algorithm found @ 
# http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates
def getDates(start, end):
	
	startSplit = start.split('/')
	endSplit = end.split('/')

	dateSpecs = cleanDate(startSplit,endSplit)
	d1 = date(dateSpecs[0],dateSpecs[1],dateSpecs[2])
	d2 = date(dateSpecs[3],dateSpecs[4],dateSpecs[5])

	delta = d2 - d1

	dates = []
	for i in range(delta.days + 1):
	    	dates.append( d1 + timedelta(days=i) )

	return dates

class TsnSpider(Spider):
    name = "tsn"
    allowed_domains = ["tsn.ca"]
    
    #date passed as parameter for start url
    def __init__(self, startDate=None, endDate = None, *args, **kwargs):
        super(TsnSpider, self).__init__(*args, **kwargs)
        
        #get dates
        dates = getDates(startDate, endDate)
        #for i in range(len(dates)): print dates[i]
        urls = formatUrl(dates)
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
        