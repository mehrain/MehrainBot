from mastodon import Mastodon
import os

class MastodonBot:
    def __init__(self):
        self.mastodon = Mastodon(
            access_token=os.getenv('MASTODON_ACCESS_TOKEN'),
            api_base_url=os.getenv('MASTODON_API_BASE_URL')
        )

    def post_status(self, status):
        self.mastodon.status_post(status)

    def get_timeline(self):
        return self.mastodon.timeline_home()

    def get_mentions(self):
        return self.mastodon.notifications()
    


