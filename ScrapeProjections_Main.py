import mechanicalsoup
import io
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://barttorvik.com/schedule.php"

dfs = pd.read_html(url)
df = dfs[0]
df.drop(['Time (CT)', 'TTQ', 'Result', 'Unnamed: 5'], axis=1, inplace=True)
df = df.DataFrame(df.Matchup.replace(' vs ',',').replace(' at ',','))
print(df)



#df.to_csv("BartTovikALL.csv")