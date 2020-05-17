
class ExtendedPost(BasePost):
    pass

    def __init__(self, createdAt):
        dict.__init__(self, createdAt=createdAt)
        self.createdAt = createdAt