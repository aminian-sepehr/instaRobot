import emoji
from instapy import InstaPy
from instapy import smart_run


class robot:

    def __init__(self, username, password):
        self.user = username
        self.passwd = password

        self.session = InstaPy(username=self.user,
                               password=self.passwd,
                               headless_browser=False)

        self.config()

    def config(self):
        pass

    def follow_this_list(self):
        pass

    def unfollow_list(self):
        pass

    def get_users_info(self):
        pass

    def like_all_photos(self):
        pass

    def commnet_on_post(self, comment=emoji.emojize(':red_heart: :red_heart:')):
        pass
