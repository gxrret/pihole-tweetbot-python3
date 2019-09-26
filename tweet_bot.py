//shebang needed for cronjob reference
#!/usr/bin/env python3

import tweepy
import datetime
import json
import urllib
from urllib.request import urlopen

// Reads and loads JSON data from Pi-Hole api URL specific to your static IP you set for your Raspberry Pi
data = urlopen('http://path.to.static.ip/admin/api.php').read()
print(data)
body = data.decode('utf-8')
data = json.loads(body)

tweet_template = "\nAds Blocked: %s\nAds Percentage Today: %i\nDNS Queries Today: %s\nDomains Blocked: %s"

data = tweet_template % (data['ads_blocked_today'], float (data['ads_percentage_today']), data['dns_queries_today'], data['domains_being_blocked'])

def get_api(cfg):
        auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
        auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
        return tweepy.API(auth)

def main():
        // Here we are defining the parameters for accessing Twitter's API securely, fill in the key with your corresponding twitter credentials
        cfg = {
                "consumer_key": "TWTTER_CONSUMER_KEY",
                "consumer_secret"       :       "TWITTER_CONSUMER_SECRET",
                "access_token"          :       "TWITTER_ACCESS_TOKEN",
                "access_token_secret"   :       "TWITTER_ACCESS_TOKEN_SECRET"
                }
        api = get_api(cfg)
        
        // The inital tweet that gets posted with string concatenation
        tweet = "I am a Raspberry Pi Python scripted bot\nThis is my daily #Pihole report:\n" + data  + "\n\nTime and date: " + datetime.datetime.today().strftime("%H:%M %m-%d-%Y")
        status = api.update_status(status=tweet)
        print(tweet)
        
if __name__ == "__main__":
        main()
