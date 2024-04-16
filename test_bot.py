from mastodon import Mastodon, StreamListener
import time

class MyStreamListener(StreamListener):
    def __init__(self, mastodon):
        self.mastodon = mastodon

    def on_update(self, status):
        if '@MehrainBot' in status.content:
            self.mastodon.status_post('@' + status.account.username + ' Hello there!')

# Create an instance of the Mastodon class
mastodon = Mastodon(
    access_token='RDsjIxrdcGP7qgTBcL2REZzW79xFOjFsIs14hoJWwuI',
    api_base_url='https://mastodon.social'
)

listener = MyStreamListener(mastodon)

# Start streaming for mentions
try:
    mastodon.stream_user(listener)
    print("Mastodon streaming started")
except ConnectionResetError:
    print("Connection reset by peer. Retrying in 5 seconds...")
    time.sleep(5)
except Exception as e:
    print(f"An error occurred while streaming: {e}")
    