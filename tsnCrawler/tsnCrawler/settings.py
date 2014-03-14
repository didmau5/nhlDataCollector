# Scrapy settings for tsnCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tsnCrawler'

SPIDER_MODULES = ['tsnCrawler.spiders']
NEWSPIDER_MODULE = 'tsnCrawler.spiders'
ITEM_PIPELINES = {'tsnCrawler.pipelines.TsncrawlerPipeline':100}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tsnCrawler (+http://www.yourdomain.com)'
