import random
from TikTokApi import TikTokApi
import pandas as pd
import json

#extract metadata from tiktok dict t, download author dict for follower count
def extract_metadata(t):
    author=str(t['author']['uniqueId'])
    tiktok_id=str(t['id'])
    likes=str(t['stats']['diggCount'])
    shares=str(t['stats']['shareCount'])
    comments=str(t['stats']['commentCount'])
    plays=str(t['stats']['playCount'])
    desc=str(t['desc'])
    url= 'https://www.tiktok.com/@'+author+'/video/'+tiktok_id
    followers="NULL"
    if author!="internalmeddoctor": #this account seems to have been deleted and is gumming things up - hackiest fix possible
        print("author ok")
        author_info = api.get_user(author)
        followers = author_info['userInfo']['stats']['followerCount']
    dct= {
        'author':author,
        'url':url,
        'likes':likes,
        'shares':shares,
        'comments':comments,
        'author_followers':followers,
        'plays': plays,
        'description':desc
    }
    return dct


#hashtags can be found in 'desc'
def download_tiktok(url):
    data=api.get_video_by_url(dgfsgdfg)
    with open("video.mp4", "wb") as out:
        out.write(data)


verifyFp="verify_kqlmgn2f_sgABDdgW_KdLv_46hN_87VW_PRVAVQvPspDs"
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

tiktoks = api.byHashtag("covidvaccine", count=250,custom_verifyFp=verifyFp)

with open('./out/all_dicts.json', 'w') as f:
    json.dump(tiktoks, f, indent=True)
dat=[]
for t in tiktoks:
    dat.append(extract_metadata(t))

df = pd.DataFrame(dat)
df.to_csv('./out/tiktok_metadata_07-01-2021_2112.csv')
print("success")




#df = pd.json_normalize(d, sep='_')

#with open("test.mp4", 'wb') as o:
#    o.write(api.get_Video_By_TikTok(t, custom_did=custom_did))



#print("success!")
#download_url=tiktoks[0]['video']['downloadAddr']
#print(download_url)
#vid=api.get_video_by_download_url('downloadAddr',custom_did=did)
#print(vid)