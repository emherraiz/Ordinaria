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

    def __str__(self):
        return f'Time: {self.time}\nMessage: {self.message}\nSender: {self.sender}'


class Retweet(Tweet):
    def __init__(self, time, message, sender, referencia):
        super().__init__(time, message, sender)
        self.referente = referencia

    def __str__(self):
        return f'Time: {self.time}\nMessage: {self.message}\nSender: {self.sender}\nReferente: {self.referente}'


class DirectMessage(Tweet):
    def __init__(self, time, message, sender, receiver):
        super().__init__(time, message, sender)
        self.receiver = receiver

    def __str__(self):
        return f'Time: {self.time}\nMessage: {self.message}\nSender: {self.sender}\nReceiver: {self.receiver}'




