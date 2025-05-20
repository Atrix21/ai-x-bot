import openai
import os
from dotenv import load_dotenv
import logging
import random

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_tweet(topic, personality="funny, insightful, with a hint of dark humor"):
    prompt = (
        f"Write a short, engaging tweet about {topic} in a {personality} tone.\n"
        f"Requirements:\n"
        f"- Maximum 1-2 lines (around 100-120 characters)\n"
        f"- Make it punchy and memorable\n"
        f"- Include a touch of wit or humor\n"
        f"- No hashtags or mentions\n"
        f"- Be conversational and engaging\n"
        f"Tweet:"
    )
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a witty and engaging Twitter user."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=40,
            temperature=0.8,
            n=1
        )
        tweet = response.choices[0].message.content.strip()
        
        # Ensure the tweet isn't too long
        if len(tweet) > 120:
            tweet = tweet[:117] + "..."
            
        return tweet
    except Exception as e:
        logger.error(f"Error generating tweet: {e}")
        return None

def generate_reply(tweet_text, personality):
    """
    Generate a contextual reply to a tweet using OpenAI's API.
    Ensures the reply is engaging and concise.
    """
    prompt = (
        f"Write a short, engaging reply to this tweet: \"{tweet_text}\"\n"
        f"Requirements:\n"
        f"- Maximum 1-2 lines (around 100-120 characters)\n"
        f"- Make it punchy and memorable\n"
        f"- Include a touch of wit or humor\n"
        f"- No hashtags or mentions\n"
        f"- Be conversational and maintain the {personality} tone\n"
        f"Reply:"
    )
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a {personality} Twitter user."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=40,
            temperature=0.7,
            n=1
        )
        reply = response.choices[0].message.content.strip()
        
        # Ensure the reply isn't too long
        if len(reply) > 120:
            reply = reply[:117] + "..."
            
        return reply
    except Exception as e:
        logger.error(f"Error generating reply: {e}")
        return None

def get_personality_variation():
    """Returns a random personality variation for more diverse interactions"""
    personalities = [
        "witty and sarcastic",
        "thoughtful and philosophical",
        "playfully cynical",
        "intellectually curious",
        "gently mocking",
        "observant and insightful"
    ]
    return random.choice(personalities)
