#!/usr/bin/env python
from bs4.diagnose import diagnose
import urllib

html = urllib.urlopen("http://www.nhl.com/scores/htmlreports/20082009/GS021229.HTM").read()

diagnose(html)