# Dependencies
import tweepy
import time

# Twitter API Keys
consumer_key = "ZQdPBPM1CtYOZOq5gzZ45ONGu"
consumer_secret = "kH65fX9MTldOdXoxq4lOURMDzupoBqIxUk2CqJ67VsDNLYutTC"
access_token = "943258585311694848-aV9Dp1OsIRdGOoXGZKy0SPWiCZMpwd0"
access_token_secret = "Yr81e3f9OanedDmSsskNW7yRQZOA2qgnwnPZiXgHhQH8V"


# Create quotes to tweet
quote_list = ["Quote 1","Quote 2","Quote 3"]

# Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
# Create function for tweeting
def QuoteItUp():

    i=0
    # Tweet the next quote
    api.update_status(quote_list[i])
    # Print success message
    print("%s Quote tweeted successfully"%(i+1))
    i+=1


# Set timer to run every minute
counter=0
while(counter<3):
    QuoteItUp()
    time.sleep(30)
