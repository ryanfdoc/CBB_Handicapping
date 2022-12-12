import mechanicalsoup
import requests, re
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#Get BartTorvik Projections for Today
driver = webdriver.Chrome("/opt/anaconda3/bin/chromedriver 2") #path to webdriver
driver.get('https://barttorvik.com/schedule.php')

list_category_elements = driver.find_element("xpath", '/html/body/div/div/p[4]/table/tbody')  # finds torvik table elements
links = list_category_elements.find_elements(By.TAG_NAME ,'a')
links_values3 =[]
for i in range(len(links)):

    links_values3.append(links[i].text)


dft = pd.DataFrame(links_values3)
dft = pd.DataFrame(np.array((links_values3)),
                 columns=['team1'])

links_values3 = np.array(links_values3)

print(dft.iloc[0:20])

#creates torvik df
dft2 = dft.team1.str.split(expand=True)
print(dft2)
dft2 = pd.DataFrame(dft.team1.str.split('\n',1).tolist(),
                         columns = ['Teams','PredictedScore'])
print(dft2)
Tovrik = dft2.iloc[2::4]
print(Tovrik)
Tovrik.columns = ['score1','score2']
print(Tovrik)

TovrikF = pd.DataFrame(Tovrik.score2.str.rsplit('-',n=2,expand=True))
TovrikF.columns = ['score1','score2']
TovrikFinal2 = pd.DataFrame(TovrikF.score2.str.rsplit('(',n=2,expand=True))
Tovrikcombo = pd.concat([Tovrik, TovrikF.reindex(Tovrik.index)], axis=1).iloc[0:50]
Tovrikx = pd.concat([Tovrikcombo, TovrikFinal2.reindex(Tovrikcombo.index)], axis=1).iloc[0:50]
Tovrikx.columns = ['Team','Pred','Score1','-','Score2','-']



TovFinal = Tovrikx
TovFinal.drop(TovFinal.columns[[1,3,5]], axis=1, inplace=True)


#TovFinal.to_csv('BartTovik.csv')
#print(TovFinal)