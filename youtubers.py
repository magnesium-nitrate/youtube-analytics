import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd

df = pd.read_csv('INvideos.csv')
df_tea = df.groupby(['channel_title'])
#print(df.groupby('channel_title'))
df2 = pd.DataFrame()
j=0
print(df['channel_title'].value_counts())

objects = ['VikatanTV','etvteluguindia','Flowers Comedy','ETV Plus India','SAB TV','T-Series']
y_pos = np.arange(len(objects))
performance = [284, 282, 270, 253, 244,221]
 
plt.barh(y_pos, performance, align='center', alpha=.5)
plt.yticks(y_pos, objects)
plt.xlabel('Amount of Times Trended')
plt.title('Top Trenders in India')
plt.show()

#plt.scatter(df.views,df.likes,s=10)
#plt.show()
#tea = [6, 77, 26, 43, 4, 9, 177, 4, 19, 82, 21, 79, 36, 17, 4, 2, 75, 26, 68, 125, 1, 4, 8, 159, 38, 4, 2, 25, 4, 2, 25, 16]
#fig1, ax1 = plt.subplots()
#ax1.pie(tea,labels=objects)
#ax1.axis('equal')

#plt.barh(y_pos, tea, align='center', alpha=.5)
#plt.yticks(y_pos, objects)
#plt.xlabel('Amount of Politicians in each Party')
#plt.title('Party Size Comparison')

#plt.scatter(tea,performance)
#plt.show()
