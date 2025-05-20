def post_tweet(api, tweet_text):
    try:
        api.update_status(tweet_text)
        print("Tweet posted:", tweet_text)
    except Exception as e:
        print("Error posting tweet:", e)