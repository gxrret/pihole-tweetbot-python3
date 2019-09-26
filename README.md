# Pi-Hole-Ad-Blocker-Tweet-Bot

This is a Python3 script bot that tweets out to my Twitter developer account https://twitter.com/piholet my Pi-Hole daily statistics
like DNS queries blocked, total blocked ads

This can also be used as a basic template to read and parse JSON data in Python 3.

## Requirements

Install the following python dependency:
`sudo tweepy`


You'll need `json`, `urllib`, and `datetime`, but those are already pre-defined dependencies when Python is installed.

## Cronjob

I use Cronjob to schedule the script to run at 12 PM every day.
To add a script to your Cronjob list, run crontab -e. You will then need to select an editor; I usually use Nano since it is the easiest for me.

At the end of crontab, add this:

##### `00 12 * * * python3 /home/user/path/to/tweet_bot.py dev/null 2>&1`

Add a shebang on the first line of your .py file referring to your Python3 library.

## Twitter Access Token, Token Secret, Consumer Secret
1. Create a Twitter account https://twitter.com

2. Apply at https://developer.twitter.com to create your script application and have access to Twitter's OAuth API.

3. Create your app, you don't need a callback URL unless you want one.

4. 



## NEED TO FINISH
