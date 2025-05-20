import os
from dotenv import load_dotenv
import tweepy
import logging

logger = logging.getLogger(__name__)

def create_api():
    """Create and verify Twitter API connection"""
    try:
        # Create v2 client
        client = tweepy.Client(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )
        
        # Verify credentials
        client.get_me()
        logger.info("Twitter API v2 authentication successful")
        return client
        
    except Exception as e:
        logger.error(f"Twitter API authentication failed: {str(e)}")
        return None
