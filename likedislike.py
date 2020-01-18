import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd

df = pd.read_csv('INVideos.csv')
df_tea = df.groupby(['channel_title'])
#print(df.groupby('channel_title'))
#df2 = pd.DataFrame()
#j=0
print(df['channel_title'].value_counts())
#df2['name'] = df.groupby(['channel_title'])
#df2['count'] = df['channel_title'].value_counts()
#df['count'] = df.groupby(['channel_title']).transform(pd.Series.value_counts)
#df2.sort_values('count', inplace=True, ascending=False)
#print('df sorted: \n{}'.format(df2))
#print(df)


#print(df_tea.size())
#print("yort")
#for i in df_tea:
#    print(i.size())
#print(df.groupby('channel_title').size())

#for i in df_tea:
    #print(i)
#for index,row in df.iterrows():
 #   a,b,c,d,e,f,g,h,i,t,k,l,m,n,o,p = row
  #  j+=1
df_tea.to_csv('tea.csv')

pd.value_counts(normalize=False, sort=True, ascending=False, bins=None)
totalv = df['views'].sum()
totall = df['dislikes'].sum()
print(totalv)
print(totall)
print(j)
print(totall/totalv)
