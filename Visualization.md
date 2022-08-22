# Visualization using Python
```
df=pd.read_csv('YT_data.csv')
print(df[:5])
print(df.columns)
```
![image](https://user-images.githubusercontent.com/111043457/184090975-dac15399-2cd0-4d05-9683-3d1f81ab989e.png)

# Histogram
```
x=df["tags"] ;
plt.hist(x,edgecolor='black') 
plt.xlabel("No. of Tags Used ") 
plt.ylabel("Occurrences") 

plt.show() 
```
![image](https://user-images.githubusercontent.com/111043457/184091160-35ed2417-1611-4de9-86ba-babb3897d29d.png)

# Line Chart

```
df1 = df.groupby('channel').agg(channel_count = ('channel', 'count')).sort_values(by='channel_count', ascending=False)
print(df1.reset_index(level='channel')[:10])

df1.plot( kind= 'line', title='Channel Occurence', ylabel='Channel count',marker="o",color='black')
plt.show()
```
![image](https://user-images.githubusercontent.com/111043457/184091411-e6cae70d-fed8-4e6c-9d3b-0cd51f5f253c.png)

# Bar Chart

```
df_highest_views = df.groupby('channel').agg(view_count = ('views', 'sum')).sort_values(by='view_count', ascending=False);
print(df_highest_views.reset_index(level='channel')[:10]);

df_highest_views.plot(kind= 'bar', title='Most Viewed Videos', ylabel='Billions of Views', color = 'yellow',edgecolor='black') ;
plt.show() ;
```
![image](https://user-images.githubusercontent.com/111043457/184091770-3bdfa93c-a528-4fbf-9a25-2e66427aeb4c.png)

# Standard Scaled Plot
The frequency of occurrence of channel in playlist and no. of views converted into a standard scale and plotted to visualize relationship.
```
from sklearn.preprocessing import MinMaxScaler ;
mm = MinMaxScaler() ;
Channel_count_and_views_scaled = pd.DataFrame(mm.fit_transform(Channel_count_and_views), columns = Channel_count_and_views.columns) ;

##print(Channel_count_and_views_scaled) ;

plt.plot(Channel ,Channel_count_and_views_scaled['channel_count'],marker="o", label='Channel Occurence');
plt.plot(Channel,Channel_count_and_views_scaled['view_count'],marker="o", label='Views');
plt.legend(loc="upper left");
plt.title('Scaled version of Channel occurance and total views');
plt.xlabel('Channels');
plt.ylabel('scaled values of count and viewership');
plt.xticks(Channel, Channel,fontsize=5,rotation=90);
plt.grid(True);
plt.show();
```
![image](https://user-images.githubusercontent.com/111043457/184092468-b41000db-0ca0-4508-afcc-02c7de37583f.png)




