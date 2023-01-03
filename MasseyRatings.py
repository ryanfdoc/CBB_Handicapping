# Import libraries
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import lxml.html as lh
from selenium import webdriver

url = 'https://masseyratings.com/cb/ncaa-d1/games'
#Create a handle, page, to handle the contents of the website
browser = webdriver.Chrome()
browser.get(url)

html = browser.page_source
#Store the contents of the website under doc
soup = BeautifulSoup(html, 'lxml')
table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="tbl") 
rows = table.findAll(lambda tag: tag.name=='tr')
print(rows[:2])
