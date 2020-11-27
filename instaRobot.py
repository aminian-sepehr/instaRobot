import emoji
from instapy import InstaPy
from instapy import smart_run
import os


class robot:

    def __init__(self, username, password1):
        self.user = username
        self.passwd = password1

        self.session = InstaPy(username=self.user,
                               password=self.passwd,
                               headless_browser=False)

        self.__config()

    def __config(self):
        self.session.set_relationship_bounds(enabled=False)

    def __follow_this_list(self, filepath):
        if (os.path.isfile(filepath)):  # check if exists do this and else : follow a username
            l1 = self.__readfile(filepath)
        else:
            l1 = list(filepath)
        try:
            self.session.follow_by_list(l1, 1, 600, False)
        except(Exception):
            print('failed to follow\n')

    def __unfollow_list(self, filepath):
        if (os.path.isfile(filepath)):  # check if exists do this and else : follow a username
            l1 = self.__readfile(filepath)
        else:
            l1 = list(filepath)
        try:
            self.session.unfollow_users(amount=200,
                                        custom_list_enabled=True,
                                        custom_list=l1,
                                        custom_list_param="all",
                                        style="RANDOM")
        except(Exception):
            print('failed to follow\n')

    def __get_users_info(self):
        pass

    def __like_all_photos(self, filepath):
        self.session.set_user_interact()
        self.session.like_by_feed(amount=200,
                                  randomize=True,
                                  unfollow=True,
                                  interact=True)

    def __commnet_on_post(self, comment=emoji.emojize(':red_heart: :red_heart:')):
        pass

    def run(self, flag, filepath=''):
        with smart_run(self.session):
            self.__config()

            if flag == 1:
                self.__follow_this_list(filepath)
            elif flag == 2:
                self.__unfollow_list(filepath)
            elif flag == 3:
                self.__like_all_photos(filepath)
            elif flag == 4:
                self.__commnet_on_post()
            else:
                raise 'flag error : flag number dowsnt match1 \n'

    def __readfile(self, filename):
        namelist = []
        try:
            with open(filename, 'r') as reader:
                for i in reader.readlines():
                    if (i.find('\n') != -1):
                        i = i[:i.find('\n')]
                    namelist.append(i)
            reader.close()
        except(FileNotFoundError):
            print('file not found\n')
            reader.close()
        return namelist

    def __writedata(self, datalist, filename):
        try:
            with open(filename, 'w') as writer:
                for i in datalist:
                    writer.writelines(i)
                    writer.writelines('\n')
            print("data file updated")
        except(Exception):
            print("something went wrong\n")
