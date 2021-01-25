# socialScrapper
[![GPL](https://img.shields.io/github/license/slowy07/socialScrapper?style=for-the-badge)](LICENSE)
![action_status](https://img.shields.io/github/workflow/status/slowy07/socialScrapper/Python%20application?logo=github&style=for-the-badge)
![file_size](https://img.shields.io/github/languages/code-size/slowy07/socialScrapper?color=green&style=for-the-badge)

scrapping cyber bully on social media

## requirements
- python 3.x version with pip3 installed
```bash
sudo apt-get install python3-pip
```
check pip version
```bash
pip3 --version
```
- geckodriver mozilla firefox, [click for more information](https://github.com/mozilla/geckodriver/releases)

## user list creation
tool can  handle N-number of user account scrapping wich be given a ``user.txt``


## installation
- clone / download git repo
```bash
git clone https://github.com/slowy07/socialScrapper.git
cd socialScrapper
```
- automatic setup
```bash
chmod +x setup
./setup
```
- manual installation
```bash
pip3 install -r requirements.txt
```

**api keys**
We haven't included our keys for usage. Add your respective api keys to SocialScraper/social/api.py and replace the google credentials.json and client_secret.json to sample directory and facebook credentials in credentials.yaml for scrappering the accounts.

**google API**
Get it signed in and once you get your API key, make sure that you have enabled gmail service to this.So that automatic mail can function, [Gmail API](https://developers.google.com/gmail/api)

**deep ai**
sign up deep ai and get the api key, [deepAI api](https://deepai.org/)

**imagga API**
get the api key [imagga api](https://imagga.com/auth/signup)

## running
```bash
python3 main.py
```