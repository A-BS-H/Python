import pandas as pd ;
import csv ;
from matplotlib import pyplot as plt ;
import seaborn as sns ;
import numpy as np ;

df=pd.read_csv('YT_data.csv') ;
print(df[:5]) ;
print(df.columns) ;

x=df["tags"] ;
plt.hist(x,edgecolor='black') ;
plt.xlabel("No. of Tags Used ") ;
plt.ylabel("Occurrences") ;

plt.show() ;

df1 = df.groupby('channel').agg(channel_count = ('channel', 'count')).sort_values(by='channel_count', ascending=False);
print(df1.reset_index(level='channel')[:10]);

df1.plot( kind= 'line', title='Channel Occurence', ylabel='Channel count',marker="o",color='black') ;
plt.show() ;


df_highest_views = df.groupby('channel').agg(view_count = ('views', 'sum')).sort_values(by='view_count', ascending=False);
print(df_highest_views.reset_index(level='channel')[:10]);

df_highest_views.plot(kind= 'bar', title='Most Viewed Videos', ylabel='Billions of Views', color = 'yellow',edgecolor='black') ;
plt.show() ;

Channel = df['channel'].unique() ;

Channel_count_and_views = pd.DataFrame() ;
Channel_count_and_views.index = Channel ;
Channel_count_and_views['channel_count'] = df1['channel_count'] ;
Channel_count_and_views['view_count'] = df_highest_views['view_count'] ;

print(Channel_count_and_views) ;

from sklearn.preprocessing import MinMaxScaler ;
mm = MinMaxScaler() ;
Channel_count_and_views_scaled = pd.DataFrame(mm.fit_transform(Channel_count_and_views), columns = Channel_count_and_views.columns) ;

print(Channel_count_and_views_scaled) ;




plt.plot(Channel ,Channel_count_and_views_scaled['channel_count'],marker="o", label='Channel Occurence');
plt.plot(Channel,Channel_count_and_views_scaled['view_count'],marker="o", label='Views');
plt.legend(loc="upper left");
plt.title('Scaled version of Channel occurance and total views');
plt.xlabel('Channels');
plt.ylabel('scaled values of count and viewership');
plt.xticks(Channel, Channel,fontsize=5,rotation=90);
plt.grid(True);
plt.show();
