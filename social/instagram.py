import requests
from igql import InstagramGraphQL
import urllib.request
import ast
import os
import re
from machine import *


R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'


def Instagram(user):
    print(W + '[+]'+ G + 'Fetching data of {} from instagram'.format(user)+W)
    r = requests.get("https://instagram.com/"+user+"/?__a=1")
    if r.status_code == 200:
        try:
            os.mkdir(user)
        except:
            pass
        f1 = open("./{0}/{1}.txt".format(user,user), "W+")
        res = r.json()['graphql']['user']
        f1.write("\nUsername :"+res['username'])
        f1.write("\nFull name:"+res['full_name'])
        
        try:
            f1.write("\nBussines category :"+res['edge_follow']['bussines_category_name'])
        except:
            f1.write("\nAccount :"+"public")
        finally:
            f1.write("\nBiograph :"+res['biography'])
            f1.write("\nURL :"+str(res['external_url']))
            f1.write("\nFollowers :"+str(res['edge_followed_by']['count']))
            f1.write("\nFollowing :"+str(res['edge_follow']['count']))
            f1.write("\nProfile picture HD :"+res['profile_pic_url_hd']+"\n")
            print()
            predator = []
            username1 = user
            f = open('wordlist.txt', 'r')
            wordlist = []
            for i in f:
                for j in i.split():
                    wordlist.append()
            f.close()
            igql_api = InstagramGraphQL()
            user = igql_api.get_user(user)
            for media in user.timeline():
                for i in media:
                    f1.write("\nID :"+i['node']["id"])
                    try:
                        f1.write("\nCaption :"+str(i["node"]["edge_media_to_caption"]["edges"][0]['node']['text']))
                    except:
                        f1.write("")
                    else:
                        f1.write("\nCaption:")