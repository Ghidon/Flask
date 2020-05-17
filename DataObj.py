

class DataObj(dict):
    def __init__(self, userId, id, title, body):
        dict.__init__(self, userId=userId, id=id, title=title, body=body)
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body