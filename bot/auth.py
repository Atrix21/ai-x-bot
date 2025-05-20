import os
from dotenv import load_dotenv
import tweepy

load_dotenv()

def create_api():
    auth = tweepy.OAuth1UserHandler(
        os.getenv("API_KEY"),
        os.getenv("API_KEY_SECRET"),
        os.getenv("ACCESS_TOKEN"),
        os.getenv("ACCESS_TOKEN_SECRET")
    )
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        print("Error during authentication:", e)
        raise e
    return api
