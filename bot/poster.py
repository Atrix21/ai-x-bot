def post_tweet(api, message):
    api.update_status(status=message)
    print("Tweet posted:", message)
