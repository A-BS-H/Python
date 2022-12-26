# YouTube-Playlist-Analysis
YT-analysis


## Importing Libraries
```
from googleapiclient.discovery import build
import pandas as pd
import csv
from matplotlib import pyplot as plt
import numpy as np
```
After creating an API key from Google/Youtube open sourse platfrom, getting the playlist ID for playlist.

```
api_key='----123----'
playlist_id='--546--'

youtube=build('youtube','v3',developerKey=api_key)

```

## Use of Playlist ID

Using playlist ID to get playlist details and required video statistics

```
videos = [] 

while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute() ;

    vid_ids = [] 
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId']) ;

    vid_request = youtube.videos().list(
        part='snippet,statistics',
        id=','.join(vid_ids)
    ) ;

    vid_response = vid_request.execute() 

    for item in vid_response['items']:
        channel=item['snippet']['channelTitle']
        title=item['snippet']['title']
        published=item['snippet']['publishedAt']
        tag_count= len(item['snippet']['tags'])
        view_count=item['statistics'].get('viewCount',0)
        like_count=item['statistics'].get('likeCount',0)
        dislike_count=item['statistics'].get('dislikeCount',0)
        comment_count=item['statistics'].get('commentCount',0)

        vid_id = item['id'] 

        videos.append(
            {
                'channel': str(channel),
                'title': str(title),
                'published': str(published),
                'tags': int(tag_count),
                'views': int(view_count),
                'likes': int(like_count),
                'dislikes': int(dislike_count),
                'comments': int(comment_count)
            }
        ) 

    
```
## Sorting Retrived data
```
videos.sort(key=lambda vid: vid['views'], reverse=True)
for video in videos[:10]:
    print(video['channel'], video['views']) 
```
![image](https://user-images.githubusercontent.com/111043457/184089301-97b4ed30-efde-423a-b965-d25df43b8bca.png)

## Saving scrapped data as a csv File

```
df=pd.DataFrame(videos) ;

df.to_csv("YT.csv") ;
df.head() ;
```


