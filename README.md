# Meme Coin AI Agent

This agent scans Twitter for meme‑coin and airdrop mentions, evaluates upside potential, and outputs a ranked list.

## Setup
1. Clone this repo.
2. Copy `.env.example` to `.env` and fill in your keys.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running locally

```bash
python agent.py --scan
```

## Deployment

- Use the included `Dockerfile` or deploy on Railway/Heroku.
- Set environment variables in your host or CI.
- (Optional) Configure a cron job or Railway Cron for scheduled scans.
