import random
from TikTokApi import TikTokApi
import pandas as pd

#extract metadata from tiktok dict t, download author dict for follower count
def extract_metadata(t):
    author=str(t['author']['uniqueId'])
    tiktok_id=str(t['id'])
    likes=str(t['stats']['diggCount'])
    shares=str(t['stats']['shareCount'])
    comments=str(t['stats']['commentCount'])
    plays=str(t['stats']['playCount'])
    url= 'https://www.tiktok.com/@'+author+'/video/'+tiktok_id
    author_info = api.get_user(author)
    followers = author_info['userInfo']['stats']['followerCount']
    dct= {
        'author':author,
        'url':url,
        'likes':likes,
        'shares':shares,
        'comments':comments,
        'author_followers':followers,
        'plays': plays
    }
    return dct



def download_tiktok(url):
    data=api.get_video_by_url(dgfsgdfg)
    with open("video.mp4", "wb") as out:
        out.write(data)




api = TikTokApi.get_instance()
c=20
tiktoks = api.byHashtag("covidvaccine", count=c)
dat=[]
for t in tiktoks:
    dat.append(extract_metadata(t))

df = pd.DataFrame(dat)
df.to_csv('./out/sample_df.csv')
print("success")


#df = pd.json_normalize(d, sep='_')

#with open("test.mp4", 'wb') as o:
#    o.write(api.get_Video_By_TikTok(t, custom_did=custom_did))



#print("success!")
#download_url=tiktoks[0]['video']['downloadAddr']
#print(download_url)
#vid=api.get_video_by_download_url('downloadAddr',custom_did=did)
#print(vid)