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

import kenpompy as kp

from kenpompy.utils import login
browser = login("ryanfdougherty@gmail.com","StraightCash22")

