# main.py
import os
import time
import logging
import random
from datetime import datetime, time as dtime
from dotenv import load_dotenv
from bot.auth import create_api
from bot.ai_gen import generate_tweet, get_personality_variation
from bot.poster import post_tweet
from bot.interactions import interact

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def is_peak_hours():
    """Check if current time is during peak social media hours"""
    current_time = datetime.now().time()
    peak_hours = [
        (dtime(8, 0), dtime(10, 0)),   # Morning
        (dtime(12, 0), dtime(14, 0)),  # Lunch
        (dtime(17, 0), dtime(19, 0)),  # Evening
        (dtime(20, 0), dtime(22, 0))   # Night
    ]
    return any(start <= current_time <= end for start, end in peak_hours)

def get_activity_level():
    """Determine how active the bot should be based on time of day"""
    if is_peak_hours():
        return random.randint(2, 3)  # More active during peak hours
    return random.randint(1, 2)  # Less active during off hours

def load_config():
    """Load configuration from environment variables"""
    load_dotenv()
    
    # Default topics if not specified in environment
    default_topics = [
        "artificial intelligence",
        "machine learning",
        "technology trends",
        "future of work",
        "digital transformation"
    ]
    
    # Get topics from environment or use defaults
    topics = os.getenv('BOT_TOPICS', '').split(',')
    topics = [t.strip() for t in topics if t.strip()] or default_topics
    
    # Get base personality from environment or use default
    base_personality = os.getenv('BOT_PERSONALITY', 'friendly and witty')
    
    # Get interaction settings
    tweets_per_topic = int(os.getenv('TWEETS_PER_TOPIC', '2'))
    
    return {
        'topics': topics,
        'base_personality': base_personality,
        'tweets_per_topic': tweets_per_topic
    }

def run_bot_cycle(api, config):
    """Run one complete cycle of the bot's activities"""
    try:
        # Determine activity level based on time of day
        activity_level = get_activity_level()
        logger.info(f"Current activity level: {activity_level}")
        
        # Randomly decide whether to post original tweets
        if random.random() < 0.7:  # 70% chance to post original tweets
            # Generate and post original tweets
            for topic in random.sample(config['topics'], min(activity_level, len(config['topics']))):
                for _ in range(config['tweets_per_topic']):
                    personality = get_personality_variation()
                    tweet = generate_tweet(topic, personality)
                    if tweet:
                        post_tweet(api, tweet)
                        logger.info(f"Posted tweet about {topic}")
                        # Random delay between tweets (30-90 seconds)
                        time.sleep(random.uniform(30, 90))
                    else:
                        logger.warning(f"Failed to generate tweet for topic: {topic}")
        
        # Randomly decide whether to interact with others
        if random.random() < 0.6:  # 60% chance to interact
            # Interact with other tweets
            interact(api, config['base_personality'], config['topics'])
        
    except Exception as e:
        logger.error(f"Error in bot cycle: {e}")

def main():
    try:
        # Load configuration
        config = load_config()
        logger.info("Starting bot with configuration:")
        logger.info(f"Topics: {config['topics']}")
        logger.info(f"Base personality: {config['base_personality']}")
        
        # Initialize Twitter API
        api = create_api()
        if not api:
            logger.error("Failed to initialize Twitter API")
            return
        
        logger.info("Successfully initialized Twitter API")
        
        # Run one cycle of the bot
        run_bot_cycle(api, config)
        logger.info("Completed bot cycle successfully")
    
    except Exception as e:
        logger.error(f"Fatal error: {e}")

if __name__ == "__main__":
    main()
