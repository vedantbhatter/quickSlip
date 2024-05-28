import tweepy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

BEARER_TOKEN = 'YOUR_BEARER_TOKEN'

client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_latest_prizepicks_link(user_handle):
    tweets = api.user_timeline(screen_name=user_handle, count=5, tweet_mode='extended')
    for tweet in tweets:
        if 'prizepicks.onelink.me' in tweet.full_text:
            for word in tweet.full_text.split():
                if 'prizepicks.onelink.me' in word:
                    return word
    return None

def automate_pp_bet(prizepicks_url):
    PATH = 'YOUR_CHROMEDRIVER_PATH'
    driver = webdriver.Chrome(PATH)
    driver.get(prizepicks_url)

    time.sleep(5)

    bet_amt = driver.find_element(By.XPATH, '//*[@id="entry-input"]')
    bet_amt.clear()
    bet_amt.send_keys('5')

    place_bet = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/main/div/div/div[2]/div[2]/div[3]/div/form/div[2]/button').click()

    time.sleep(5)
    driver.quit()


def main(user_handle):
    link = fetch_latest_prizepicks_link(user_handle)
    if link:
        automate_pp_bet(link)
    else:
        print('No prizepicks link found')


if __name__ == '__main__':
    main('cmattdowns')





