import datetime

COMMENT = []
LOGGED_IN= []
USER = []


class User(object):
    """ main user creation class """
    def __init__(self, username,password,firstname):
        super(User, self).__init__()
        self.username = username
        self.firstname = firstname
        self.password = password
        self.role = "user"

    def edit_comment(self, com_id):
        """ Edits user comment """
        for user in LOGGED_IN:
            if user['username'] == self.username: 
                for com in COMMENT:
                    if com['id'] == com_id:
                        comment = com
                    print(comment)
                if comment['user'] == self.username:
                        print("Your comment : {}".format(comment['comment']))
                        newComment = input("Edit comment: ")
                        comment['comment'] = newComment

                        comment['commented at'] = datetime.datetime.utcnow().strftime("%D %H:%M")
                        print(comment)
                        
                else:
                    print('You are not allowed to edit this comment')

            else:
                print('Please login')
