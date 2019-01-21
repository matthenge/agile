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

    def signup_user(self):
        """User signup"""
        newUser = {
            "username" : self.username,
            "firstname" : self.firstname,
            "password": self.password,
            "role": self.role
        }

        USER.append(newUser)

class Moderator(User):
    """docstring for Moderator."""
    pass

class Admin(Moderator):
    """docstring for Admin."""
    pass

class Comment:
    """docstring for Comment."""
    def get_comment(comment):
        comment = input("Add your comment here: ")
        commented_at = datetime.datetime.utcnow()
        new_comment = {
        "user" :
        }
    def add_comment()



if __name__ == '__main__':
    while True:
        "Welcome to The agile group challenge: "
        pass
