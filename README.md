======================
NHL Data Collector
======================

Collects regular season scoring data from gamesheets posted on tsn.ca or nhl.com.
Uses scrapy for web crawling and beautifulsoup to extract data from html.

*** Currently only crawls tsn.ca and nhl.com for goal data


========================
HOW TO RUN:
========================

First call the spider with <start date> <end date> as parameters:
	$cd gameCrawler
	$./spiderCaller.py <"mm/dd/yr"> <"mm/dd/yr">

Then process the data:
	$cd ..
	$./processDate.py
