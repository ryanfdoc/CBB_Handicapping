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

driver.get('https://il.sportsbook.fanduel.com/sports/navigation/11086.3/11087.3')  # finds fanduel table elements
b = driver.find_element_by_class_name(
    "btn.tab.active")  # sends fanduel to 'all games' tab - may need tweaking if featured games tab present
print(b)
b.click()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

url = "https://il.sportsbook.fanduel.com/sports/navigation/11086.3/11087.3"

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
list_category_elements = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[6]/main/div/div/div/div/div[1]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[2]')
linksspread = list_category_elements.find_elements(By.CLASS_NAME, "event")

links_valuesFD = []
for i in range(len(linksspread)):
    links_valuesFD.append(linksspread[i].text)

dffd = pd.DataFrame((links_valuesFD[0::]), columns=['Fanduel'])  # fanduel df
dffd = pd.DataFrame((links_valuesFD), columns=['Fanduel'])
dffd.set_index('Fanduel')

dffd3 = pd.DataFrame(dffd.Fanduel.str.rsplit('\n', n=25, expand=True))

Fanduel = dffd3