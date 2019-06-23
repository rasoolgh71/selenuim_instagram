import datetime
from selenium import webdriver


class Bot(object):

    def __init__(self):
        # self.driver = webdriver.Chrome()
        self.browser = webdriver.Chrome()
        self.total = {'likes': 0,
                      'unlikes': 0,
                      'follows': 0,
                      'unfollows': 0,
                      'comments': 0,
                      'blocks': 0,
                      'unblocks': 0,
                      'messages': 0,
                      'archived': 0,
                      'unarchived': 0}

        self.start_time = datetime.datetime.now()

        # self.delays = {'like': like_delay,
        #                'unlike': unlike_delay,
        #                'follow': follow_delay,
        #                'unfollow': unfollow_delay,
        #                'comment': comment_delay,
        #                'block': block_delay,
        #                'unblock': unblock_delay,
        #                'message': message_delay}

    def open_browser(self):
        self.browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

    # def login(self, login_waite=True):
