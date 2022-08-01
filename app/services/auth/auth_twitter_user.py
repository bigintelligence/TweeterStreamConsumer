import tweepy
from app.utils.singleton import singleton
from app.utils.constants import ConfigProps


@singleton
class AuthTwitterUserHandler:
    def __init__(self):
        self._secret_consumer_key = ConfigProps.secret_consumer_key.value
        self._secret_consumer_secret = ConfigProps.secret_consumer_secret.value
        self._oauth1_user_handler = tweepy.OAuth1UserHandler(self._secret_consumer_key,
                                                             self._secret_consumer_secret,
                                                             callback=ConfigProps.callback.value
                                                             )

    def get_authorization_url(self):
        return self._oauth1_user_handler.get_authorization_url()

    def get_access_token_secret(self, pin: str):
        access_token, access_token_secret = self._oauth1_user_handler.get_access_token(pin)
        return access_token, access_token_secret

