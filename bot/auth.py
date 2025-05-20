import os
from dotenv import load_dotenv
import tweepy
import logging

logger = logging.getLogger(__name__)

def create_api():
    """Create and verify Twitter API connection"""
    try:
        auth = tweepy.OAuth1UserHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )
        api = tweepy.API(auth)
        
        # Verify credentials
        api.verify_credentials()
        logger.info("Twitter API authentication successful")
        return api
        
    except Exception as e:
        logger.error(f"Twitter API authentication failed: {str(e)}")
        return None
