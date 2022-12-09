import kenpompy
import mechanicalsoup
import requests, re
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

from kenpompy.utils import login
browser = login("ryanfdougherty@gmail.com","StraightCash22")

#df_fanmatch = kenpompy.FanMatch.FanMatch(browser)

tester = kenpompy.summary.get_height(browser, season=None)
print(tester)