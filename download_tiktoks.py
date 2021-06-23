import random
from TikTokApi import TikTokApi
api = TikTokApi.get_instance()

#i don't think I need this if I'm not downloading?
#custom_did = str(random.randint(10000, 99999999))

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
    followers = author_info['stats']['followerCount']
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


#add number here
def download_tiktok(url):
    data=api.get_video_by_url(dgfsgdfg)
    with open("video.mp4", "wb") as out:
        out.write(data)



def main():
    api = TikTokApi.get_instance()

    tiktoks = api.byHashtag(hashtag, count=c)

    

df = pd.json_normalize(d, sep='_')

#with open("test.mp4", 'wb') as o:
#    o.write(api.get_Video_By_TikTok(t, custom_did=custom_did))



#print("success!")
#download_url=tiktoks[0]['video']['downloadAddr']
#print(download_url)
#vid=api.get_video_by_download_url('downloadAddr',custom_did=did)
#print(vid)