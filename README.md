# Pi Hole Ad-Blocker Tweet Bot

This is a Python3 script bot that tweets out my Pi-Hole daily statistics to my Twitter developer account [@PIHoleT](https://twitter.com/piholet) like total DNS queries blocked, total blocked ads for the current day, the percentage of ads blocked, and how many domains are currently blacklisted. There are more JSON data types associated with Pi-Hole and you can use whatever you want, I just chose the latter for the most accurate and coherent statistics.

This can also be used as a basic template to read and parse JSON data in Python 3, just fill in your URL instead of the one parsing from Pi-Hole.

## Requirements

Install the following python dependency:
`sudo tweepy`


You'll need `json`, `urllib`, and `datetime`, but those are already pre-defined dependencies when Python is installed. If you don't have them, go ahead and install them.

## Cronjob

I use Cronjob to schedule the script to run at 12 PM every day.
To add a script to your Cronjob list, run crontab -e. You will then need to select an editor; I usually use Nano since it is the easiest for me.

At the end of crontab, I added this:

##### `00 12 * * * python3 /home/user/path/to/tweet_bot.py dev/null 2>&1`

The `00 12` refers to a specific time, which this would be 12:00PM. If you want this script to run every hour, day, week, or whatever time scale you want, refer to the [Cronjob documentation here](https://help.ubuntu.com/community/CronHowto)

`dev/null 2>&1` basically throws out any remaining returns from the command, while we are only looking for what we defined in the .py file.

Add a shebang on the first line of your .py file referring to your Python3 library. Refer to the .py file.

## Twitter Access Token, Token Secret, Consumer Secret
1. Create a Twitter account https://twitter.com

2. Apply at https://developer.twitter.com to create your script application and have access to Twitter's OAuth API.

3. Create your app, you don't need a callback URL, once there, find your tokens and secrets. Use those in the `cfg` scope of the script.
