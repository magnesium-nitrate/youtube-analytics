#link to dataset https://www.kaggle.com/datasnaek/youtube-new

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import pygal

df = pd.read_csv('USvideos.csv')

likes=[]
views=[]

for cnt in df['likes']:
   likes.append(cnt)

for cnt in df['views']:
   views.append(cnt)
   
total=0
x=len(likes)
print(x)
for x in range(x):
   if likes[x]!=0:
       ratio=views[x]/likes[x]
       total=total+ratio

x=len(likes)
USRatio=(total/x)



df = pd.read_csv('CAvideos.csv')

likes=[]
views=[]

for cnt in df['likes']:
   likes.append(cnt)

for cnt in df['views']:
   views.append(cnt)
   
total=0
x=len(likes)
print(x)
for x in range(x):
   if likes[x]!=0:
       ratio=views[x]/likes[x]
       total=total+ratio

x=len(likes)
CARatio=(total/x)



df = pd.read_csv('GBvideos.csv')

likes=[]
views=[]

for cnt in df['likes']:
   likes.append(cnt)

for cnt in df['views']:
   views.append(cnt)
   
total=0
x=len(likes)
print(x)
for x in range(x):
   if likes[x]!=0:
       ratio=views[x]/likes[x]
       total=total+ratio

x=len(likes)
GBRatio=(total/x)


df = pd.read_csv('INvideos.csv')

likes=[]
views=[]

for cnt in df['likes']:
   likes.append(cnt)

for cnt in df['views']:
   views.append(cnt)
   
total=0
x=len(likes)
print(x)
for x in range(x):
   if likes[x]!=0:
       ratio=views[x]/likes[x]
       total=total+ratio

x=len(likes)
INRatio=(total/x)

df = pd.read_csv('RUvideos.csv')

likes=[]
views=[]

for cnt in df['likes']:
   likes.append(cnt)

for cnt in df['views']:
   views.append(cnt)
   
total=0
x=len(likes)
print(x)
for x in range(x):
   if likes[x]!=0:
       ratio=views[x]/likes[x]
       total=total+ratio

x=len(likes)
RURatio=(total/x)

chart = pygal.Bar()
chart.add('US',USRatio)
chart.add('IN',INRatio)
chart.add('GB',GBRatio)
chart.add('RU',RURatio)
chart.add('CA',CARatio)

chart.render_to_file('LikesViews.svg')
