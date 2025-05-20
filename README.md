# AI Twitter Bot 🤖

An intelligent Twitter bot that generates and posts content using OpenAI's GPT model, with natural interaction patterns and personality variations. The bot runs automatically through GitHub Actions, posting at random intervals throughout the day.

## 🌟 Features

- **AI-Powered Content Generation**: Uses OpenAI's GPT model to generate engaging tweets
- **Smart Posting Schedule**: Posts at random intervals throughout the day (approximately 5 posts per day)
- **Dynamic Personality**: Varies personality traits for more natural and engaging content
- **Topic-Based Content**: Focuses on specific topics while maintaining variety
- **Interactive Behavior**: Engages with other tweets and users
- **Peak Hour Optimization**: Adjusts activity levels based on peak social media hours
- **Automated Deployment**: Runs automatically through GitHub Actions

## 📋 Prerequisites

- Python 3.9 or higher
- Twitter Developer Account with API access
- OpenAI API key
- GitHub account (for automated deployment)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-x-bot.git
cd ai-x-bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following variables:
```env
OPENAI_API_KEY=your_openai_api_key
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
BOT_TOPICS=your,comma,separated,topics
BOT_PERSONALITY=your_base_personality
TWEETS_PER_TOPIC=2
```

## 📁 Project Structure

```
ai-x-bot/
├── .github/
│   └── workflows/
│       └── bot.yml          # GitHub Actions workflow configuration
├── bot/
│   ├── __init__.py
│   ├── ai_gen.py           # AI content generation logic
│   ├── auth.py             # Twitter API authentication
│   ├── interactions.py     # Tweet interaction logic
│   └── poster.py           # Tweet posting functionality
├── .env                    # Environment variables (not tracked in git)
├── .gitignore
├── main.py                 # Main bot logic and orchestration
├── README.md
└── requirements.txt        # Python dependencies
```

## 🚀 Usage

### Local Development

To run the bot locally:
```bash
python main.py
```

### Automated Deployment

The bot is configured to run automatically through GitHub Actions. The workflow:
- Runs every 5 hours
- Adds a random delay of 0-4 hours before posting
- Posts approximately 5 times per day at random intervals

To set up automated deployment:
1. Fork this repository
2. Add your secrets to GitHub repository settings:
   - `OPENAI_API_KEY`
   - `TWITTER_API_KEY`
   - `TWITTER_API_SECRET`
   - `TWITTER_ACCESS_TOKEN`
   - `TWITTER_ACCESS_TOKEN_SECRET`
   - `BOT_TOPICS`
   - `BOT_PERSONALITY`
   - `TWEETS_PER_TOPIC`

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `TWITTER_API_KEY`: Twitter API key
- `TWITTER_API_SECRET`: Twitter API secret
- `TWITTER_ACCESS_TOKEN`: Twitter access token
- `TWITTER_ACCESS_TOKEN_SECRET`: Twitter access token secret
- `BOT_TOPICS`: Comma-separated list of topics to tweet about
- `BOT_PERSONALITY`: Base personality for the bot
- `TWEETS_PER_TOPIC`: Number of tweets to generate per topic

### Customization

You can customize the bot's behavior by:
1. Modifying the topics in the environment variables
2. Adjusting the personality traits
3. Changing the posting frequency in the GitHub Actions workflow
4. Modifying the interaction patterns in `interactions.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This bot is for educational purposes only. Please ensure you comply with Twitter's terms of service and API usage guidelines when using this bot.
