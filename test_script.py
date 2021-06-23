import random
from TikTokApi import TikTokApi
api = TikTokApi.get_instance()

#i don't think I need this if I'm not downloading?
#custom_did = str(random.randint(10000, 99999999))
#pull the tiktoks
#tiktoks = api.byHashtag("covidvaccine", count=10)

#def construct_tiktok_url(t):
#    author=str(t['author']['uniqueId'])
#    num=str(t['id'])
#    url= 'https://www.tiktok.com/@'+author+'/video/'+num
#    return url

#print(api.get_user("annie_wu_22"))

#for follower count it's api.get_user[stats][followerCount]

#print(tiktoks[0].keys())
#print(tiktoks[0]['author'])

#url is https://www.tiktok.com/@[['author']['uniqueId']]/video/['id']

#data=api.get_video_by_url(construct_tiktok_url(tiktoks[0]))
#with open("out/video.mp4", "wb") as out:
#    out.write(data)


author_info = api.get_user('brandongrogan61')
print(author_info.keys())
followers = author_info['userInfo']['stats']['followerCount']

print(followers)