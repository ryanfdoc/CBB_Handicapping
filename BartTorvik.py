import pandas as pd
import numpy as np
import requests, re


url = "https://barttorvik.com/schedule.php"
dfs = pd.read_html(url)

#Create Dataframe and Drop Unnecessary Columns
df = dfs[0]
df = df.rename(columns={'Matchup': 'Away'})
df.drop(['Time (CT)', 'TTQ', 'Result'], axis=1, inplace=True)
df[['Away', 'Home']] = df['Away'].str.split(' at | vs ',expand=True)


#Format Home and Away Columns, Reorder Dataframe
#Remove Special Characters and Numbers
df['Away'] = df['Away'].str.replace(r'\d+', r'', regex=True)
df['Home'] = df['Home'].str.replace(r'\d+', r'', regex=True)
df['Home'] = df['Home'].str.replace(r'[!,*)@#%($_?^+]', r'', regex=True)

#Remove Broadcaster Substring
df['Home'] = df['Home'].replace(r' ESPN', r'', regex=True)
df['Home'] = df['Home'].replace(r' ACCN', r'', regex=True)
df['Home'] = df['Home'].replace(r' ABC', r'', regex=True)
df['Home'] = df['Home'].replace(r' ACCN', r'', regex=True)
df['Home'] = df['Home'].replace(r' ACCNX', r'', regex=True)
df['Home'] = df['Home'].replace(r' BIG12ESPN', r'', regex=True)
df['Home'] = df['Home'].replace(r' BTN', r'', regex=True)
df['Home'] = df['Home'].replace(r' CBSSN', r'', regex=True)
df['Home'] = df['Home'].replace(r' FOX', r'', regex=True)
df['Home'] = df['Home'].replace(r' FS', r'', regex=True)
df['Home'] = df['Home'].replace(r' LHN', r'', regex=True)
df['Home'] = df['Home'].replace(r' PAC', r'', regex=True)
df['Home'] = df['Home'].replace(r' Peacock', r'', regex=True)
df['Home'] = df['Home'].replace(r' SECN', r'', regex=True)

#Reorder Dataframe
df = df[['Away', 'Home', 'T-Rank Line']]

#Reformat T-Rank Line to expand Dataframe and make all data usable
# EXAMPLE FORMAT: "Creighton -1.2, 69-67 (55%)"
df = df.rename(columns={'T-Rank Line': 'BT_Fav'})
df[['BT_Fav', 'BT_Spread', 'Fav_Score', 'Dog_Score', 'BT_XWin']] = df['BT_Fav'].str.split('[-|,|-|;|(]',expand=True)
df['BT_Spread'] = df['BT_Spread'].replace(r'[!,*)@#%($_?^+]', r'', regex=True)
df['BT_Spread'] = df['BT_Spread'].replace(r'100', r'', regex=True)
df['BT_XWin'] = df['BT_XWin'].replace(r'[!,*)@#($_?^+]', r'', regex=True)

#Print to CSV
df.to_csv("bart_test.csv")
