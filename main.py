import instaRobot

username = ''
passwd = ''
robot = instaRobot.robot(username, passwd)
working = True
print("Welcome to insta robot what do you want to do?\n"
      " 1-follow\n"
      " 2-unfollow\n"
      " 3-get user info\n"
      " 4-like all posts of someone\n"
      " 5-comment on last post\n"
      " 6-exit\n")

while (working):
    command = input()
    com_splited = command.split()
    if com_splited[0] == 'follow':
        # robot1.follow_this_list(com_splited[1])
        try:
            robot.run(1,com_splited[1])
        except(IndexError):
            print('follow command must at least have an additional argument\n')

    elif com_splited[0] == 'unfollow':
        try:
            robot.run(2, com_splited[1])
        except(IndexError):
            print(' Unfollow command must at least have an additional argument\n')

    elif com_splited[0] == 'exit':
        working = False

    else:
        print("wrong command\n")
from instapy import InstaPy
from instapy import smart_run

# login credentials
# insta_username = "sara.bot.by.maral"
# insta_password = "123sara456maral"
# # insta_username = ''
# # insta_password = ''
#
# # get an InstaPy session!
# # set headless_browser=True to run InstaPy in the background
# session = InstaPy(username=insta_username,
#                   password=insta_password,
#                   headless_browser=False)
#
# # with smart_run(session):
# #     """ Activity flow """
# #     # general settings
# #     session.set_relationship_bounds(enabled=True,
# #                                     delimit_by_numbers=True,
# #                                     max_followers=4590,
# #                                     min_followers=45,
# #                                     min_following=77)
# #
# #     session.set_dont_include(["friend1", "friend2", "friend3"])
# #     session.set_dont_like(["pizza", "#store"])
# #
# #     # activities
# #
# #     """ Massive Follow of users followers (I suggest to follow not less than
# #     3500/4000 users for better results)...
# #     """
# #     session.follow_user_followers(['user1', 'user2', 'user3'], amount=800,
# #                                   randomize=False, interact=False)