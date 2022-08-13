from instagrapi import Client
import praw
import time
import random
import requests
import json
from time import sleep


cl = Client()
u = "reddit___memes__"
p = "Jeremic06"
cl.login(u, p)


tags = " #bikini #nude #hot #girl #beach #pool #sexy #tween"

while True: 
	subreddit = 'bikini'
	count = 1
	timeframe = 'all' #hour, day, week, month, year, all
	listing = 'random' # controversial, best, hot, new, random, rising, top
	 
	def get_reddit(subreddit,count):
	    try:
	        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
	        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
	    except:
	        print('An Error Occured')
	    return request.json()
	 
	top_post = get_reddit(subreddit,count)
	 
	if listing != 'random':
	    title = top_post['data']['children'][0]['data']['title']
	    url = top_post['data']['children'][0]['data']['url']
	else:
	    title = top_post[0]['data']['children'][0]['data']['title']
	    url = top_post[0]['data']['children'][0]['data']['url']
	 
	 
	try:
		filename = '1.jpg'
		res = requests.get(url)
		print(res.status_code)
		with open(filename, 'wb') as out:
		    out.write(res.content)
		    print("Downloaded")
	except:
		print("Failed to download!")
		continue

	try:
		media = cl.photo_upload(
		    "1.jpg",
		    title + tags,
		    extra_data={
		        "custom_accessibility_caption": "alt text example",
		        "like_and_view_counts_disabled": 0,
		        "disable_comments": 0,
		    }
		)
		print("Uploaded photo! xO xO")
	except:
		print("Failed to upload!")
		continue

	try:
		commens_ammount = 20
		medias = cl.hashtag_medias_top('bikini', amount=commens_ammount)
		for i in range(commens_ammount):
			comment = cl.media_comment(medias[i].dict()['id'], "Hey sweetie, check out my profile for some hot and slicy pics! :d")
			print('Posted comment number '+ str(i))
			sleep(120)
	except:
		print("Failed")
		continue

#######################pokusaj cl.relogin()