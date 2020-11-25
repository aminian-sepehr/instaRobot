import instaRobot

username = "sara.bot.by.maral"
passwd = "123sara456maral"
# robot = instaRobot.robot(username, passwd)
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
        pass

    elif com_splited[0] == 'unfollow':
        pass

    elif com_splited[0] == 'exit':
        working = False

    else:
        print("wrong command\n")
