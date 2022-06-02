class Tweet:
    def __init__(self, time, message, sender):
        self.time = time
        self.message = message
        self.sender = sender

    def get_time(self):
        return self.time

    def get_message(self):
        return self.message

    def get_sender(self):
        return self.sender


class Retweet(Tweet):
    def __init__(self, referencia):
        super().__init__()
        self.referente = referencia


class DirectMessage(Tweet):
    def __init__(self, receiver):
        super().__init__()
        self.receiver = receiver



