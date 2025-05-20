import logging

logger = logging.getLogger(__name__)

def post_tweet(api, tweet_text):
    """
    Post a tweet using the Twitter API.
    Returns True if successful, False otherwise.
    """
    if not tweet_text:
        logger.warning("No tweet text provided")
        return False
        
    try:
        # Log the attempt
        logger.info(f"Attempting to post tweet: {tweet_text[:50]}...")
        
        # Post the tweet
        response = api.update_status(tweet_text)
        
        # Log success with tweet ID
        logger.info(f"Successfully posted tweet. Tweet ID: {response.id}")
        return True
        
    except Exception as e:
        logger.error(f"Error posting tweet: {str(e)}")
        return False