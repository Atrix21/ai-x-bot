from random import choice, sample
from bot.ai_gen import generate_reply, get_personality_variation
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def like_tweet(api, tweet_id):
    try:
        api.create_favorite(tweet_id)
        logger.info(f"Liked tweet {tweet_id}")
    except Exception as e:
        logger.error(f"Error liking tweet {tweet_id}: {e}")

def reply_to_tweet(api, tweet_id, username, reply_text):
    if not reply_text:
        logger.warning(f"No reply text generated for tweet {tweet_id}")
        return
        
    try:
        reply_status = f"@{username} {reply_text}"
        api.update_status(status=reply_status, in_reply_to_status_id=tweet_id)
        logger.info(f"Replied to tweet {tweet_id}")
        # Add a small delay to avoid rate limiting
        time.sleep(2)
    except Exception as e:
        logger.error(f"Error replying to tweet {tweet_id}: {e}")

def follow_user(api, user_id):
    try:
        api.create_friendship(user_id)
        logger.info(f"Followed user {user_id}")
        # Add a small delay to avoid rate limiting
        time.sleep(2)
    except Exception as e:
        logger.error(f"Error following user {user_id}: {e}")

def search_tweets(api, query, count=10):
    try:
        tweets = api.search_tweets(q=query, lang="en", count=count)
        return tweets
    except Exception as e:
        logger.error(f"Error searching tweets for query '{query}': {e}")
        return []

def interact(api, base_personality, topics):
    """
    Interact with tweets based on given topics and personality.
    Uses varying personalities to make interactions more natural.
    """
    for topic in topics:
        logger.info(f"Searching for tweets about: {topic}")
        tweets = search_tweets(api, topic, count=20)
        if not tweets:
            logger.warning(f"No tweets found for topic: {topic}")
            continue
        
        # Like 3-5 random tweets
        num_likes = min(5, len(tweets))
        for tweet in sample(tweets, num_likes):
            like_tweet(api, tweet.id)
            time.sleep(1)  # Small delay between likes
        
        # Reply to 1-2 random tweets with varying personalities
        num_replies = min(2, len(tweets))
        for tweet in sample(tweets, num_replies):
            # Get a random personality variation
            personality = get_personality_variation()
            reply_text = generate_reply(tweet.text, personality)
            if reply_text:
                reply_to_tweet(api, tweet.id, tweet.user.screen_name, reply_text)
        
        # Follow 1 user from those tweets
        user_to_follow = choice(tweets).user.id
        follow_user(api, user_to_follow)
        
        # Add a delay between topics to avoid rate limiting
        time.sleep(5)
