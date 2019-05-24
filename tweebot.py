import tweepy


def followback(noofusers):
    for follower in tweepy.Cursor(api.followers).items(noofusers):
        follower.follow()

    print("Followed %s followers" % (noofusers))


def follow(search, nooftweets):
    for tweet in tweepy.Cursor(api.search, search).items(nooftweets):
        try:
            #follow
            tweet.user.follow()
            print("--------------------------")
            print(tweet.user.name)
            print("--------------------------")

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


def Retweet(search, nooftweets):
    for tweet in tweepy.Cursor(api.search, search).items(nooftweets):
        try:
            #Retweet
            tweet.retweet()
            print("--------------------------")
            print("Retweeted tweet")
            print("--------------------------")

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


def MarkFav(search, nooftweets):
    for tweet in tweepy.Cursor(api.search, search).items(nooftweets):
        try:
            #favourtie
            tweet.favorite()
            print("--------------------------")
            print("favorite tweet")
            print("--------------------------")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# Get your keys and token from apps.twitter.com. Make app and get keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
print("Welcome "+user.name + " From " + user.location)

print("Please select any option from below")

print("""
0. Follow users who following you
1. Follow Users based on Search
2. Retweet Tweets based on search
3. Favourite tweets based on search
""")
val = input("Enter your Select ? ex.1 \n")

if val == "0":
    nooffollower = input("Enter no of users to follow ?\n")
    followback(int(nooffollower))

elif val == "1":
    nooftweets = input("Enter no of tweets ?\n")
    search = input("Enter search term ?\n")
    follow(search, int(nooftweets))

elif val == "2":
    nooftweets = input("Enter no of tweets ?\n")
    search = input("Enter search term ?\n")
    Retweet(search, int(nooftweets))

elif val == "3":
    nooftweets = input("Enter no of tweets ?\n")
    search = input("Enter search term ?\n")
    MarkFav(search, int(nooftweets))


print("\n\n Thank you for using Tweebot :) ")
print("\n Created by Akash Senta")
