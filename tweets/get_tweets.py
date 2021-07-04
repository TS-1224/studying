
import tweepy

consumer_key = "MmXYrt2SsE6gcp2AYy7F5ipKo"
consumer_secret = "3JtDs1fhEmVCbDF0HNjLfpw1i5Zzm6dm1EikMaFiCDs9YvRC3f"
access_token = "1410937196492713984-WSKfPXE56r9B6SfwcIIhcxvR2XjO7g"
access_token_secret = "8IK7D8CV8z1n57w81DtGNLZFlYGzlw2WiEWJZh8wOpnO7"

#Twitterオブジェクト作成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#ツイートの投稿
#api.update_status("test tweet")

print("-"*50)

#ツイートの取得
account = "gr_phenix"
tweets = api.user_timeline(account, count=30, page=1)
num = 1
for tweet in tweets:
    print('twid : ', tweet.id)               # tweetのID
    print('user : ', tweet.user.screen_name)  # ユーザー名
    print('date : ', tweet.created_at)      # 呟いた日時
    print(tweet.text)                  # ツイート内容
    print('favo : ', tweet.favorite_count)  # ツイートのいいね数
    print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
    print('ツイート数 : ', num) # ツイート数
    print('='*30) # =を80個表示
    num += 1 # ツイート数を計算