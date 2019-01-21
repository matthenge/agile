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

class Moderator(User):
    """docstring for Moderator."""
    def delete_comment(self, com_id):
        """ delete user comment """
        for user in LOGGED_IN:
            if user['username'] == self.username: 
                for com in COMMENT:
                    if com['id'] == com_id: 
                        COMMENT.remove(com)
                        print('COMMENT DELETED')


class Admin(Moderator):
    """docstring for Admin."""
    pass
