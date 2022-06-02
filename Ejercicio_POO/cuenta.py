from datetime import date
from tipos_de_tweets import *
class UserAccount:
    def __init__(self, alias, email, tweets, followers, timeline):
        # string
        # porque el alias es uno solo y es una sola cadena de caracteres
        self.alias = alias
        # string
        # porque el email es uno solo y es una sola cadena de caracteres
        self.email = email
        # lista de clases
        # Como veremos en la segunda parte del ejercicio, un tweet es una estructura más compleja (necesitamos una clase)
        # Al constructor de esta clase se le asocia un time, un mensage y un sender.
        # Además esta clase tendrá más metodos
        self.tweets = tweets
        # lista de clases
        # Es una lista con todos los followers, es decir todos UserAccount que siguen a este usuario
        self.followers = followers
        # datatime
        # Es un formato de fecha que viene importado de la libreria datatime
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
