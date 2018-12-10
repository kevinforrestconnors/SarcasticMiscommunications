import tweepy
import secret_keys


consumer_key = secret_keys.get_consumer_key()
consumer_secret = secret_keys.get_consumer_secret_key()
access_token = secret_keys.get_access_token_key()
access_token_secret = secret_keys.get_access_token_secret_key()


# Creates the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Sets your access token and secret
auth.set_access_token(access_token, access_token_secret)

# Creates the API object while passing in auth information
api = tweepy.API(auth)


# The search term you want to find
queries = ["I was being sarcastic", "That was sarcasm", "It was sarcasm", "/s"]

# Language code (follows ISO 639-1 standards)
language = "en"


# q – the search query string
# lang – Restricts tweets to the given language, given by an ISO 639-1 code.
# locale – Specify the language of the query you are sending. This is intended
#   for language-specific clients and the default should work in the majority of cases.
# rpp – The number of tweets to return per page, up to a max of 100.
# page – The page number (starting at 1) to return, up to a max of roughly 1500 results (based on rpp * page.
# since_id – Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
# geocode – Returns tweets by users located within a given radius of the given latitude/longitude.
#   The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile.
#   The parameter value is specified by “latitide,longitude,radius”, where radius units must be specified
#   as either “mi” (miles) or “km” (kilometers). Note that you cannot use the near operator via the API to
#   geocode arbitrary locations; however you can use this geocode parameter to search near geocodes directly.
# show_user – When true, prepends “<user>:” to the beginning of the tweet. This is useful for readers that do
#   not display Atom’s author field. The default is false.



# Creates a new file
f = open("results.txt", "w+")

for query in queries:

    f.write("Query: " + query)

    for tweet in tweepy.Cursor(api.search, wait_on_rate_limit=True, wait_on_rate_limit_notif=True, q=query, count=100, result_type="recent", include_entities=True, lang="en").items():

        # get the entire comment chain

        comment_chain = [tweet.text]

        # if there is a reply:
        while tweet.in_reply_to_status_id is not None:
            reply = api.get_status(tweet.in_reply_to_status_id)
            comment_chain = [reply.text] + comment_chain

        # prints the entire comment chain
        for comment in comment_chain:
            f.write(comment + "\n")

        f.write("\n")