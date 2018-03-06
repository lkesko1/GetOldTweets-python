from urllib.parse import urlparse

class Tweet:

    def __init__(self):
        pass

    def __str__(self):
        tweet_args = []

        url_comp = urlparse(self.permalink)
        self.username = url_comp.path.split('/')[1]

        username = ':'.join(('"username"',
                         ''.join(('"',
                                  str(self.username),
                                  '"'))))
        tweet_args.append(username)

        for key in ['id', 'permalink','text', 'retweets', 'favorites', 'mentions', 'hashtags', 'geo']:
            tweet_args.append(':'.join(('"' + key + '"',
                                        ''.join(('"',
                                                 str(self.__dict__[key]),
                                                 '"')))))

        date = ':'.join(('"date"',
                         ''.join(('"',
                                  self.date.strftime('%d/%m/%Y %H:%M:%S'),
                                  '"'))))
        tweet_args.append(date)

        str_tweet = ','.join(tweet_args)

        return str_tweet


    def __repr__(self):
        return ''.join(('{', self.__str__(), '}'))