import mechanicalsoup
import io
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
e.send_keys("ryanfdougherty@gmail.com") #kenpom username
e = driver.find_element("xpath", '/html/body/div/div[1]/div[1]/div[1]/form/input[2]')
e.send_keys("StraightCash22") #kenpom password
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

Hasla=Hasla
Hasla2=Hasla2

#Get BartTorvik Projections for Today
driver = webdriver.Chrome("/opt/anaconda3/bin/chromedriver 2") #path to webdriver
driver.get('https://barttorvik.com/schedule.php')

list_category_elements = driver.find_element("xpath", '/html/body/div/div/p[4]/table/tbody')  # finds torvik table elements
links = list_category_elements.find_elements(By.TAG_NAME ,'a')
links_values3 =[]
for i in range(len(links)):

    links_values3.append(links[i].text)


dft =pd.DataFrame(links_values3)

dft =pd.DataFrame(np.array((links_values3)),
                 columns=['team1'])


links_values3 =np.array(links_values3)

print(dft.iloc[0:20])

#creates torvik df
dft2=dft.team1.str.split(expand=True)

dft2=pd.DataFrame(dft.team1.str.split('\n',1).tolist(),
                         columns = ['Teams','PredictedScore'])

Tovrik=dft2.iloc[2::4]
Tovrik.columns=['score1','score2']

TovrikF=pd.DataFrame(Tovrik.score2.str.rsplit('-',n=2,expand=True))
TovrikF.columns=['score1','score2']
TovrikFinal2=pd.DataFrame(TovrikF.score2.str.rsplit('(',n=2,expand=True))
Tovrikcombo=pd.concat([Tovrik, TovrikF.reindex(Tovrik.index)], axis=1).iloc[0:50]
Tovrikx=pd.concat([Tovrikcombo, TovrikFinal2.reindex(Tovrikcombo.index)], axis=1).iloc[0:50]
Tovrikx.columns=['Team','Pred','Score1','-','Score2','-']

TovFinal=Tovrikx
TovFinal.drop(TovFinal.columns[[1,3,5]], axis=1, inplace=True)


#Download PredictionTracker projections and read into dataframe
response = requests.get("https://www.thepredictiontracker.com/ncaabbpreds.csv")

print('status_code:', response.status_code)

#if response.status_code == 200:
if response.ok:
    predtracker = pd.read_csv( io.StringIO(response.text) )
else:
    predtracker = None

print(predtracker)




#Export all dataframes to CSV
TovFinal.to_csv('BartTovik.csv')
Hasla.to_csv('HaslametricsHome.csv')
Hasla2.to_csv('HaslametricsAway.csv')
Kenpom.to_csv('KenPom.csv')
predtracker.to_csv('PredTracker.csv')
