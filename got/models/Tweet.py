class Tweet:

    def __init__(self):
        pass

    def __str__(self):
        id = ':'.join(('id', self.id))
        permalink = ':'.join(('pemalink', self.permalink))
        username = ':'.join(('username', self.username))
        text = ':'.join(('text', self.text))
        date = ':'.join(('date', self.date.strftime('%m/%d/%Y')))
        retweets = ':'.join(('retweets', str(self.retweets)))
        favorites = ':'.join(('favorites', str(self.favorites)))
        mentions = ':'.join(('mentions', str(self.mentions)))
        hasthags = ':'.join(('hasthags', self.hashtags))
        geo = ':'.join(('geo', self.geo))

        tweet_args = (id,
                      permalink,
                      username,
                      text,
                      date,
                      retweets,
                      favorites,
                      mentions,
                      hasthags,
                      geo)
        str_tweet = ','.join(tweet_args)
        return str_tweet

    def __repr__(self):
        return ''.join(('{', self.__str__(), '}'))