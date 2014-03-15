======================
||NHL Data Collector||
======================

Collects scoring data using "Boxscore" view available on most NHL score reporting websites.
Uses scrapy for web crawling and beautifulsoup to extract data from html.

*** Currently only crawls tsn page


========================
HOW TO RUN:
========================

First call the spider:
	$cd tsnCrawler
	$python tsnSpiderCrawler.py <"mm/dd/yr">

Then process the data:
	$cd ..
	$python processDate.py
