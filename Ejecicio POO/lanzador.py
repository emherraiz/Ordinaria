class UserAccount:
    def __init__(self, alias, email, tweets, followers, timeline):
        # string
        self.alias = alias
        # string
        self.email = email
        # lista de clases
        self.tweets = tweets
        # list
        self.followers = followers
        # datatime
        self.timeline = timeline

    def follow(self, user_2):
        self.followers.append(user_2)

    def tweet(self, tweet1):
        self.tweets.append(tweet1)

    def __str__(self):
        print(f'Alias:{self.alias}\nEmail:{self.email}\n')

        print('\nTweets:\n')
        for i in range(len(self.tweets)):
            print(f'{i + 1} - {self.tweets[i]}')

        print('\nFollowers:\n')
        for i in range(len(self.followers)):
            print(f'{i + 1} - {self.followers[i]}')


