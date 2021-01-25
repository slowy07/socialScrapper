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
                    f1.write("\nShortCode :"+i["node"]["shortcode"])
                    f1.write("\nComment :"+str(i[node]["edge_media_to_comment"]['count']))
                    media1 = igql_api.get_media(i['node']["shortcode"])
                    comments = []
                    for comments_batch in media1.comments():
                        comments.append(comments_batch)
                    for comments_batch in comments[0]:
                        j1 = ast.literal_eval(str(comments_batch['node']))
                        f1.write("\nOwner :"+j1['owner']['username'])
                        f1.write("\nText :"+j1['text'])
                        if j1['text'] in wordlist:
                            predator.append(j1['owner']['username'])
                            print(R+"{} may be a predator".format(j1['owner']['username'])+W)
                    
                    f1.write("\nTimestamp:"+ str(i['node']["taken_at_timestamp"]))
                    f1.write("\nDimensions:"+str(i['node']["dimensions"]['height'])+" X "+str(i['node']["dimensions"]['width']))
                    f1.write("\nURL:"+str(i['node']["display_url"]))
                    urllib.request.urlretrieve(str(i['node']["display_url"]),str(username1)+"/"+i['node']["id"]+".jpg")
                    f1.write("\nLikes:"+str(i['node']["edge_liked_by"]['count']))
                    f1.write("\nLocation:"+str(i['node']["location"]))
                    f1.write("\nOwner:"+str(i['node']["owner"]["username"]))
                    f1.write("accessibility_caption:"+str(i['node']["accessibility_caption"]))
                    if str(i['node']["accessibility_caption"]) in wordlist:
                        f1.write(R+"Image may Contain Insecure Content")
            '''p=machine(username1)
            if p==True:
                predator.append(j1['owner']['username'])
            else:
                pass'''
            f1.close()
            print(W)
            if len(predator)>0:
                print(R+"\nPredator Identity Details:\n")
                for i in predator:
                    Instagram(i)
                    arr=os.listdir("./{}".format(str(i)))
                    for j in arr:
                        if re.match(r".+\.jpg",j):
                            if imageai("./{}".format(str(i))+"/"+j) == True:
                                print(R+"{} Is a Predator".format(str(i))+W)
                print("Fetched Details are Saved at "+"./{0}/{1}.txt".format(username1,username1))
                for i in predator:
                    print("./{0}/{1}.txt".format(i,i))
                    f=open("./{0}/{1}.txt".format(i,i),'r')
                    message=f.read()
                    f.close()

                    #AutoMail Generated
                    mail(message)
            '''else:
                print(R+"\nUser Profile Details:\n"+W)
                print("Fetched Details are Saved at "+"./{0}/{1}.txt".format(username1,username1))
                f=open("./{0}/{1}.txt".format(username1,username1),'r')
                f.seek(0)
                message=f.read()
                f.close()
                #AutoMail Generated
                mail(message)'''

    elif r.status_code == 404:
        print(R+"Error: Profile Not Found")
        exit()
    else:
        print(R+"Error: Something Went Wrong")
        exit()
    f1.close()
