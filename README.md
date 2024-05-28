# PrizePicks Automation Bot

This project is a Python script that automates placing bets on PrizePicks based on links shared by specific Twitter cappers. The script uses the Twitter API to monitor tweets and Selenium for web automation to place bets on Prizepicks from your favorite Twitter cappers.

## Features
- **Twitter Integration**: Fetches the latest tweets from specified users.
- **PrizePicks Automation**: Automates the process of placing a bet on PrizePicks.
- **Real-Time Monitoring**: Continuously checks for new PrizePicks links from specified Twitter accounts.

## Requirements
- Python 3.7+
- Tweepy
- Selenium
- ChromeDriver

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/prizepicks-automation-bot.git
```
```bash
cd prizepicks-automation-bot
```

### 2. Install Dependencies
Use pip to install the required Python packages.

```bash
pip install tweepy selenium
```
### 3. Twitter API Credentials
Create a Twitter Developer account and generate API keys. Replace the placeholder in the script with your actual credentials.

```python
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'
```

### 4. ChromeDriver
Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it matches your installed version of Chrome. Set the path to the ChromeDriver executable in the script.

```python
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
```

## Usage

### 1. Run the Script
Replace the `user_handle` in the script with the Twitter handle you want to monitor. Then, run the script.

```bash
python main.py
```

### 2. Script Explanation
- `fetch_latest_prizepicks_link(user_handle)`: Fetches the latest tweets from the specified user and looks for PrizePicks links.
- `automate_pp_bet(prizepicks_url)`: Automates the process of navigating to the PrizePicks link and placing a $5 bet (or whatever your unit size is).
- `main(user_handle)`: Integrates both functions to monitor tweets and place bets.

### Example
```python
if __name__ == "__main__":
    main('cmattdowns')
```

## Contributions
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

