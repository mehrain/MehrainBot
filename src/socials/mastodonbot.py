from mastodon import Mastodon, StreamListener
import os

class MastodonBot:
    def __init__(self):
        self.mastodon = Mastodon(
            access_token=os.getenv('MASTODON_ACCESS_TOKEN'),
            api_base_url=os.getenv('MASTODON_API_BASE_URL')
        )
        #self.start_streaming()
        
    def post_status(self, status):
        self.mastodon.status_post(status)

    def get_timeline(self):
        return self.mastodon.timeline_home()

    def get_mentions(self):
        return self.mastodon.notifications()

    def handle_mention(self, status):
        if '@your_bot_username' in status.content:
            self.mastodon.status_post('@' + status.account.username + ' Hello there, i am a bot! If you have feedback or questions, please contact my creator.')


    def start_streaming(self):
        try:
            self.mastodon.stream_user(self.handle_mention)
            print("Mastodon streaming started")
        except Exception as e:
            print(f"An error occurred while streaming: {e}")
    


