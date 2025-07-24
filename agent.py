import argparse
from tools.twitter_tools import get_memecoin_tweets
from tools.nlp_tools import extract_symbol_and_type, sentiment_score
from tools.data_tools import get_token_metrics

def run_scan(max_results=50):
    tweets = get_memecoin_tweets(max_results)
    results = []
    for t in tweets:
        symbol, typ = extract_symbol_and_type(t.text)
        sent = sentiment_score(t.text)
        metrics = get_token_metrics(symbol)
        # Upside score: mix sentiment & inverse market cap
        score = sent * 0.3 + (metrics['market_cap']**-0.5 if metrics['market_cap']>0 else 0) * 0.7
        results.append({
            'tweet_id': t.id,
            'symbol': symbol,
            'type': typ,
            'sentiment': sent,
            **metrics,
            'upside_score': score
        })
    # Sort & print top 5
    top = sorted(results, key=lambda x: x['upside_score'], reverse=True)[:5]
    for r in top:
        print(r)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", action="store_true", help="Run a single memecoin scan")
    args = parser.parse_args()
    if args.scan:
        run_scan()
    else:
        print("Use --scan to run the memecoin agent.")
