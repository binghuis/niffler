import tweepy

from niffler.config import settings

client = tweepy.Client(bearer_token=settings.x.bearer_token, wait_on_rate_limit=True)


user = client.get_user(username="elonmusk", user_fields=["public_metrics"])
print(f"粉丝数: {user.data.public_metrics['followers_count']}")
