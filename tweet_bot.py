#shebang needed for cronjob reference
#!/usr/bin/env python3

import tweepy
import datetime
import json
import urllib
from urllib.request import urlopen

#Reads and loads JSON data from Pi-Hole api URL specific to your static IP you set for your Raspberry Pi
data = urlopen('http://path.to.your.pihole.url/admin/api.php').read()
print(data)
body = data.decode('utf-8')
data = json.loads(body)

dataTQ = "{:,}".format(data['dns_queries_today'])
dataQB = "{:,}".format(data['ads_blocked_today'])
dataPB = "{:.2f}%".format(data['ads_percentage_today'])
dataDA = "{:,}".format(data['domains_being_blocked'])

tweet_template = "\nTotal DNS Queries: %s\nDNS Queries Blocked: %s\nPercentage Blocked: %s\nDomains on Adlists: %s"

data = tweet_template % (dataTQ, dataQB, dataPB, dataDA)

def get_api(cfg):
        auth = tweepy.OAuthHandler(cfg['api_key'], cfg['api_key_secret'])
        auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
        return tweepy.API(auth)

def main():
        #Here we are defining the parameters for accessing Twitter's API securely, fill in the key with your corresponding twitter credentials
        cfg = {
                "api_key": "TWITTER_API_KEY",
                "api_key_secret"       :       "TWITTER_API_KEY_SECRET",
                "access_token"          :       "TWITTER_ACCESS_TOKEN",
                "access_token_secret"   :       "TWITTER_ACCESS_TOKEN_SECRET"
                }
        api = get_api(cfg)
        
        #The inital tweet that gets posted with string concatenation
        tweet = "\nMy #Pihole Report For Last 24hrs:\n" + data  + "\n\nTime and date: " + datetime.datetime.today().strftime("%H:%M %d-%m-%Y")
        status = api.update_status(status=tweet)
        print(tweet)
        
if __name__ == "__main__":
        main()
