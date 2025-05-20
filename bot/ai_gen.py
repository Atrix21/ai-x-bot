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

def clean_tweet_text(text):
    """Clean and format tweet text to ensure proper formatting"""
    # Remove quotes if present
    text = text.strip('"\'')
    
    # Remove any partial hashtags at the end
    if text.endswith('...'):
        text = text[:-3]
    if '#' in text:
        # Find the last complete word
        last_space = text.rfind(' ')
        if last_space > 0:
            text = text[:last_space]
    return text.strip()

def generate_tweet(topic, personality="funny, insightful, with a hint of dark humor"):
    prompt = (
        f"Write a complete, engaging tweet about {topic} in a {personality} tone.\n"
        f"Requirements:\n"
        f"- Write 1-2 complete sentences\n"
        f"- Make it punchy and memorable\n"
        f"- Include a touch of wit or humor\n"
        f"- No hashtags or mentions\n"
        f"- Be conversational and engaging\n"
        f"- Ensure each sentence is complete and makes sense\n"
        f"- Do not use quotes\n"
        f"Tweet:"
    )
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a witty and engaging Twitter user. Always write complete thoughts and statements. Never use quotes."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,  # Increased to allow for complete thoughts
            temperature=0.8,
            n=1
        )
        tweet = response.choices[0].message.content.strip()
        
        # Clean and format the tweet
        tweet = clean_tweet_text(tweet)
        
        # Ensure we have complete sentences
        sentences = tweet.split('.')
        if len(sentences) > 2:  # If more than 2 sentences
            tweet = '.'.join(sentences[:2]) + '.'  # Keep only first two sentences
            
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
        f"Write a complete, engaging reply to this tweet: \"{tweet_text}\"\n"
        f"Requirements:\n"
        f"- Write 1-2 complete sentences\n"
        f"- Make it punchy and memorable\n"
        f"- Include a touch of wit or humor\n"
        f"- No hashtags or mentions\n"
        f"- Be conversational and maintain the {personality} tone\n"
        f"- Ensure each sentence is complete and makes sense\n"
        f"- Do not use quotes\n"
        f"Reply:"
    )
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a {personality} Twitter user. Always write complete thoughts and statements. Never use quotes."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,  # Increased to allow for complete thoughts
            temperature=0.7,
            n=1
        )
        reply = response.choices[0].message.content.strip()
        
        # Clean and format the reply
        reply = clean_tweet_text(reply)
        
        # Ensure we have complete sentences
        sentences = reply.split('.')
        if len(sentences) > 2:  # If more than 2 sentences
            reply = '.'.join(sentences[:2]) + '.'  # Keep only first two sentences
            
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
