import json, urllib2


def get_oss_tweets():
    response = urllib2.urlopen('http://search.twitter.com/search.json?q=ntuoss')
    results = json.loads(response.readlines()[0])['results']

    return results

if __name__ == '__main__':
    results = get_oss_tweets()
    for result in results:
        print result['text']
