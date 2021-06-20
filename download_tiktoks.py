import random
from TikTokApi import TikTokApi
api = TikTokApi.get_instance()

#i don't think I need this if I'm not downloading?
#custom_did = str(random.randint(10000, 99999999))

tiktoks = api.byHashtag(hashtag, count=c)

def construct_tiktok_url(t):
    author=str(t['author']['uniqueId'])
    num=str(t['id'])
    url= 'https://www.tiktok.com/@'+author+'/video/'+num
    return url

def download_tiktok(t):
    data=api.get_video_by_url('https://www.tiktok.com/@cutepetowner/video/6975921434954583302')
    with open("video.mp4", "wb") as out:
        out.write(data)


get_tiktoks("covidvaccine",3)



#with open("test.mp4", 'wb') as o:
#    o.write(api.get_Video_By_TikTok(t, custom_did=custom_did))



#print("success!")
#download_url=tiktoks[0]['video']['downloadAddr']
#print(download_url)
#vid=api.get_video_by_download_url('downloadAddr',custom_did=did)
#print(vid)
