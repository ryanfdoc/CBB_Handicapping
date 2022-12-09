import mechanicalsoup
import requests, re
import string
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#Get Haslametrics Ratings Projections for Today
driver = webdriver.Chrome("/opt/anaconda3/bin/chromedriver 2") #path to webdriver
driver.get('https://haslametrics.com/ratings.php')

list_category_elements = driver.find_element("xpath", '/html/body/div/table/tbody/tr[5]/td/div[3]/div/div/table')  # finds hasla table elements
links = list_category_elements.find_elements(By.CLASS_NAME, "scoreproj1")
links2 = list_category_elements.find_elements(By.CLASS_NAME, "scoreproj2")
links_values2 = []
links2_values2 = []
for i in range(len(links)):
    links_values2.append(links[i].text)
for i in range(len(links2)):
    links2_values2.append(links2[i].text)

dfh1 = pd.DataFrame(links_values2)
dfh2 = pd.DataFrame(links2_values2)
links_values2 = np.array(links_values2)
links2_values2 = np.array(links2_values2)

#Creates Hasla dataframe
dfh4=pd.DataFrame((links_values2[0::2]),columns=['Home'])
dfh3=pd.DataFrame((links_values2[1::2]),columns=['HScore'])

Hasla=pd.concat([dfh4, dfh3.reindex(dfh4.index)], axis=1).iloc[0:50]

dfh5=pd.DataFrame((links2_values2[0::2]),columns=['Away'])
dfh6=pd.DataFrame((links2_values2[1::2]),columns=['Ascore'])

Hasla2=pd.concat([dfh5, dfh6.reindex(dfh5.index)], axis=1).iloc[0:50]

Halsa=Hasla
Hasla2=Hasla2

Hasla_Combined = pd.concat([Hasla, Hasla2], axis=1, join='inner')
Hasla_Combined.columns = ['Home', 'HScore', 'Away', 'AScore']

Hasla_Combined['Home'] = Hasla_Combined['Home'].str.rstrip(string.digits)
Hasla_Combined['Away'] = Hasla_Combined['Away'].str.rstrip(string.digits)
#Hasla_Combined.to_csv('HaslametricsCombined.csv')

print(Hasla_Combined)