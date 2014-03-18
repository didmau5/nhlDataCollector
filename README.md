======================
NHL Data Collector
======================

Collects scoring data using "Boxscore" view available on most NHL score reporting websites.
Uses scrapy for web crawling and beautifulsoup to extract data from html.

*** Currently only crawls tsn.ca and nhl.com for goal data


========================
HOW TO RUN:
========================

First call the spider:
	$cd gameCrawler
	$python spiderCaller.py <"mm/dd/yr">

Then process the data:
	$cd ..
	$python processDate.py
