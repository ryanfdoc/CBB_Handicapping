import mechanicalsoup
import urllib
import io
import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#Download PredictionTracker projections and read into dataframe
response = requests.get("https://www.thepredictiontracker.com/ncaabbpreds.csv")

print('status_code:', response.status_code)

#if response.status_code == 200:
if response.ok:
    predtracker = pd.read_csv( io.StringIO(response.text) )
else:
    predtracker = None

print(predtracker)