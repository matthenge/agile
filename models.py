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
