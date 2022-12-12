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

#Get KenPom FanMatch Projections for Today
driver = webdriver.Chrome("/opt/anaconda3/bin/chromedriver 2") #path to webdriver
driver.get('https://kenpom.com/index.php')


driver.find_element("xpath", '/html/body/div/div[1]/div[1]/div[1]/form')
e = driver.find_element("xpath", '/html/body/div/div[1]/div[1]/div[1]/form/input[1]')
print(e)
e.send_keys("") #kenpom username
e = driver.find_element("xpath", '/html/body/div/div[1]/div[1]/div[1]/form/input[2]')
e.send_keys("") #kenpom password
e = driver.find_element("xpath", '/html/body/div/div[1]/div[1]/div[1]/form/input[3]')
e.click()

b = driver.find_element("xpath", '/html/body/div/div[1]/div[1]/div[2]/nav/ul/li[2]/a')
print(b)
b.click()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://kenpom.com/fanmatch.php"

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
list_category_elements = driver.find_element("xpath", '/html/body/div/div[1]/div[3]/table')  # finds table elements and prints as text
links = list_category_elements.find_elements(By.TAG_NAME, "td")
links_values = []
for i in range(len(links)):
    links_values.append(links[i].text)
df = pd.DataFrame((links_values), columns=['team'])
print(df)

links_values = np.array(links_values)

#creates kenpom df and names columns
df2=pd.DataFrame(df.team.str.rsplit(' ',n=2,expand=True))

df3=df2.iloc[1::7,:2]
df=df.iloc[0::7,:2]

df3.columns=['team','score']
df4=pd.DataFrame(df3.score.str.rsplit('-',n=2,expand=True))
df4.columns=['score1','score2']

Kenpom=pd.concat([df3['team'], df4.reindex(df3.index)], axis=1).iloc[0:100]

print(Kenpom)
