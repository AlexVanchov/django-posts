class Post:
    def __init__(self, id, user_id, title, body, comments=None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.body = body
        self.snippet = self.get_snippet()
        self.comments = comments if comments else []

    def __str__(self):
        return self.title

    def get_snippet(self, length=100):
        return self.body[:length] + ('...' if len(self.body) > length else '')

    def add_comment(self, comment):
        self.comments.append(comment)
