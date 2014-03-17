# Scrapy settings for gameCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'gameCrawler'

SPIDER_MODULES = ['gameCrawler.spiders']
NEWSPIDER_MODULE = 'gameCrawler.spiders'

ITEM_PIPELINES = {
	'gameCrawler.pipelines.GamecrawlerPipeline':100
}

USER_AGENT = 'tsnCrawler (+http://www.github.com/didmau5/nhlDataCollector)'
