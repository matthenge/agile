import datetime

class User(object):
    """ main user creation class """
    def __init__(self, username,password,firstname):
        super(User, self).__init__()
        self.username = username
        self.firstname = firstname
        self.password = password
        self.role = "user"

    def add_default_role(self)

class Moderator(User):
    """docstring for Moderator."""
    pass

class Admin(Moderator):
    """docstring for Admin."""
    pass

class Comment:
    """docstring for Comment."""
    comments = []
    def add_comment(comment):
        comment = input("Add your comment here: ")
        commented_at = datetime.datetime.utcnow()


if __name__ == '__main__':
    while True:
        "Welcome to The agile group challenge: "
        pass
