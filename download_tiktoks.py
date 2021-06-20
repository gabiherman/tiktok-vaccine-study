import random
from TikTokApi import TikTokApi
api = TikTokApi.get_instance()
custom_did = str(random.randint(10000, 99999999))

tiktoks = api.byHashtag("covidvaccine", count=2,custom_did=custom_did)
t=tiktoks[0]
with open("test.mp4", 'wb') as o:
    o.write(api.get_Video_By_TikTok(t, custom_did=custom_did))



#print("success!")
#download_url=tiktoks[0]['video']['downloadAddr']
#print(download_url)
#vid=api.get_video_by_download_url('downloadAddr',custom_did=did)
#print(vid)
