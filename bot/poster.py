import logging

logger = logging.getLogger(__name__)

def post_tweet(client, tweet_text):
    """
    Post a tweet using the Twitter API v2.
    Returns True if successful, False otherwise.
    """
    if not tweet_text:
        logger.warning("No tweet text provided")
        return False
        
    try:
        # Log the attempt
        logger.info(f"Attempting to post tweet: {tweet_text[:50]}...")
        
        # Post the tweet using v2 API
        response = client.create_tweet(text=tweet_text)
        
        # Log success with tweet ID
        logger.info(f"Successfully posted tweet. Tweet ID: {response.data['id']}")
        return True
        
    except Exception as e:
        logger.error(f"Error posting tweet: {str(e)}")
        return False