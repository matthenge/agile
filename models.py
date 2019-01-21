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
    pass

class Admin(Moderator):
    """docstring for Admin."""
    pass

class Comment:
    """docstring for Comment."""
    def __init__(self):
        pass

    def generate_new_id(self):
        latestComment = {}
        if COMMENT:
            latestComment = COMMENT[-1]
            last_id = latestComment["id"]
        else:
            last_id = 0

        return last_id + 1

    def get_comment(self,a_comment, username):
        """ fetch comment from a user"""
        self.username = username
        self.comment = a_comment
        commentId = self.generate_new_id()
        comment = a_comment
        commentedAt = datetime.datetime.utcnow().strftime("%D %H:%M")
        newComment = {
        "id" : commentId,
        "comment": a_comment,
        "commented at" : commentedAt,
        "user": username
        }
        return newComment

    def add_comment(self):
        comment = self.get_comment(self.username, self.comment)
        COMMENT.append(comment)
        print(comment)
        print("Comment Has been added")
        print(COMMENT)




if __name__ == '__main__':
    myComment = Comment()
    myComment.get_comment("Miss me","adnnn")
    myComment.add_comment()

