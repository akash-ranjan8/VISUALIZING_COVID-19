# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oNr6WMSjf33Oxq9O0jdkRyK6Wgw8MnsV

#VISUALIZING THE COVID-19

#IMPORTING THE LIBRARIES
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.style.use('fivethirtyeight')

"""#READING THE DATASET"""

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv',parse_dates = ['Date'])
df.head()

"""#INTRODUCING NEW TOTAL CASES COLUMN FOR EACH COUNTRY"""

df['Total Cases'] = df[['Confirmed','Recovered','Deaths']].sum(axis=1)
df.head()

"""#MAKING A NEW FRAME FOR WHOLE COUNTRY OVER A DATE"""

worldwide_df = df.groupby(['Date']).sum()
worldwide_df.head()

"""#PLOTTING THE WORLD WIDE CASES"""

w = worldwide_df.plot(figsize=(8,5))
w.set_xlabel('Date')
w.set_ylabel('# of cases WorldWide')
w.title.set_text('WorldWide COVID insights')
plt.show()

"""# PLOTTING INDIA VS WORLDWIDE CASES"""

india_df = df[df['Country']=='India'].groupby(['Date']).sum()
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)
ax.plot(worldwide_df[['Total Cases']],label='Worldwide')
ax.plot(india_df[['Total Cases']],label='INDIA')
ax.set_xlabel('Date')
ax.set_ylabel('# Total Cases')
ax.title.set_text('WorldWide Vs. INDIA Total Cases')
plt.legend(loc ='upper left')
plt.show()

"""#DAILY INDIA CASES AND DEATHS"""

india_df=india_df.reset_index()
india_df['Daily Confirmed'] = india_df['Confirmed'].sub(india_df['Confirmed'].shift())
india_df['Daily Deaths'] = india_df['Deaths'].sub(india_df['Deaths'].shift())
fig = plt.figure(figsize=(20,8))
ax = fig.add_subplot(111)
ax.bar(india_df['Date'],india_df['Daily Confirmed'],color='b',label='INDIA Daily Confirmed Cases')
ax.bar(india_df['Date'],india_df['Daily Deaths'],color='r',label='INDIA Daily Deaths')
ax.set_xlabel('Date')
ax.set_ylabel('# No. of People Affected')
ax.title.set_text('INDIA Daily Cases and Deaths')
plt.legend(loc='upper left')
plt.show()

"""#WORST HIT COUNTRIES BY COVID-19"""

from datetime import date,timedelta
yesterday = date.today() - timedelta(days=1)
yesterday.strftime('%Y-%m-%d')
today_df = df[df['Date']==yesterday]
top_10 = today_df.sort_values(['Confirmed'],ascending=False)[:10]
top_10.loc['rest-of-world'] = today_df.sort_values(['Confirmed'],ascending=False)[10:].sum()
top_10.loc['rest-of-world','Country'] = 'Rest of World'
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(top_10['Confirmed'],labels=top_10['Country'],autopct='%1.1f%%')
ax.title.set_text('Hardest Hit Countries WorldWide')
plt.legend(loc='upper left')
plt.show()