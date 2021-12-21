import datetime

class Tweet():
    text = ""
    created_at = None
    id = None

    def __init__(self, text):
        self.text = text
        self.created_at = datetime.datetime.now()