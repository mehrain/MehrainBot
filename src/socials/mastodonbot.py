from mastodon import Mastodon, StreamListener
import os
import threading

class MyStreamListener(StreamListener):
    def __init__(self, mastodon):
        self.mastodon = mastodon

    def on_notification(self, notification):
        if notification.type == 'mention':
            status = notification.status
            self.mastodon.handle_mention(status)
        elif notification.type == 'follow':
            self.mastodon.handle_follow(notification)

class MastodonBot:
    def __init__(self):
        self.mastodon = Mastodon(
            access_token=os.getenv('MASTODON_ACCESS_TOKEN'),
            api_base_url=os.getenv('MASTODON_API_BASE_URL')
        )
        self.listener = MyStreamListener(self)
        self.start_streaming()

    def handle_mention(self, status):
        if '@MehrainBot' in status.content:
            self.post_mention(status)

    def post_mention(self, status):
        reply = '@' + status.account.acct + ' Hello there, i am a bot! If you have feedback or questions, please contact my creator.'
        self.mastodon.status_post(reply, in_reply_to_id=status.id)
        username = status.account.acct
        print(f"Replied to {username}")

    def handle_follow(self, notification):
        follower_id = notification.account.id
        self.mastodon.account_follow(follower_id)
        #self.post_status(notification.account.acct, 'Thanks for following my bot!')
        print(f"Followed {follower_id}")

    def post_status(self, status):
        self.mastodon.status_post(status)

    def get_timeline(self):
        return self.mastodon.timeline_home()

    def start_streaming(self):
        try:
            thread = threading.Thread(target=self.mastodon.stream_user, args=(self.listener,))
            thread.start()
            print("Mastodon streaming started")
        except Exception as e:
            print(f"An error occurred while streaming: {e}")