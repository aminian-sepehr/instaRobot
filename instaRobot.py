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

    def unfollow_list(self, flist):
        self.session.follow_by_list(flist, 1, 600, False)

    def get_users_info(self):
        pass

    def like_all_photos(self):
        pass

    def commnet_on_post(self, comment=emoji.emojize(':red_heart: :red_heart:')):
        pass

    def run(self):
        with smart_run(self.session):
            self.session.set_relationship_bounds()

    def readfile(self, filename):
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

    def writedata(self, datalist, filename):
        try:
            with open(filename, 'w') as writer:
                for i in datalist:
                    writer.writelines(i)
                    writer.writelines('\n')
            print("data file updated")
        except(Exception):
            print("something went wrong\n")



