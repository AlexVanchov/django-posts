class Comment:
    def __init__(self, id, post_id, name, email, body):
        self.id = id
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body

    def __str__(self):
        return f'Comment by {self.name}'
