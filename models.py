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
    pass
