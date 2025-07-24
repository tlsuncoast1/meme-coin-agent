import os
from dotenv import load_dotenv
import tweepy

# Load environment vars
load_dotenv()
API_KEY      = os.getenv("TWITTER_API_KEY")
API_SECRET   = os.getenv("TWITTER_API_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Initialize Tweepy client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    wait_on_rate_limit=True
)

def fetch_recent_tweets(query: str, max_results: int = 50):
    """Return up to `max_results` recent tweets matching `query`."""
    resp = client.search_recent_tweets(
        query=query,
        max_results=max_results,
        tweet_fields=["id","text","created_at","public_metrics"]
    )
    return resp.data or []

# Quick test
if __name__ == "__main__":
    tweets = fetch_recent_tweets("#memecoin -is:retweet", max_results=10)
    for t in tweets:
        print(f"{t.id} • {t.created_at:%Y-%m-%d %H:%M} • {t.text}\n")
