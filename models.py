import datetime

COMMENT = []
LOGGED_IN = []
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

    def login_user(self, username, password):
        """Login user"""
        users = USER
        logger = LOGGED_IN
        for user in users:
            if user["username"] == username and user["password"] == password:
                logged_in = {
                    "username": username,
                    "lastLoggedInAt": datetime.datetime.utcnow().strftime("%D %H:%M")
                }
                logger.append(logged_in)
            else:
                print("username or password are incorrect")
        return username

    def logout_user(self, username):
        """Logout user"""
        users = USER
        logger = LOGGED_IN
        for user in users:
            if user["username"] == username:
                logger.remove(user)
                print("Logged out!")

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