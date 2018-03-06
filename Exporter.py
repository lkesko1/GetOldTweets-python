import sys, getopt, datetime, codecs
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got


def main(argv):
    if len(argv) == 0:
        print('You must pass some parameters. Use \"-h\" to help.')
        return

    if len(argv) == 1 and argv[0] == '-h':
        f = open('exporter_help_text.txt', 'r')
        print(f.read())
        f.close()

        return

    try:
        opts, args = getopt.getopt(argv, "", (
        "username=", "near=", "within=", "since=", "until=", "querysearch=", "toptweets=", "maxtweets=", "output="))

        tweetCriteria = got.manager.TweetCriteria()

        for opt, arg in opts:
            if opt == '--username' and arg != '':
                tweetCriteria.username = arg

            elif opt == '--since' and arg != '':
                tweetCriteria.since = arg

            elif opt == '--until' and arg != '':
                tweetCriteria.until = arg

            elif opt == '--querysearch' and arg != '':
                tweetCriteria.querySearch = arg

            elif opt == '--toptweets':
                tweetCriteria.topTweets = arg

            elif opt == '--maxtweets' and arg != '':
                tweetCriteria.maxTweets = int(arg)

            elif opt == '--near' and arg != '':
                tweetCriteria.near = '"' + arg + '"'

            elif opt == '--within' and arg != '':
                tweetCriteria.within = '"' + arg + '"'

        tweets = got.manager.TweetManager.getTweets(tweetCriteria)

        print(tweets)
        sys.stdout.flush()

    except argv:
        print('Arguments parser error, try -h' + argv)
    finally:
        pass

if __name__ == '__main__':
    main(sys.argv[1:])
