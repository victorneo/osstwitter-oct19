from django.http import HttpResponse
from django.shortcuts import render
from libosstweets import get_oss_tweets

def index(request):
    return HttpResponse('Hello, World!')

# Almost equivalent to
# public HttpResponse index(HttpRequest request){
#     return new HttpResponse("Hello World"))
# }


def greet(request, name):
    return HttpResponse('Hello, %s' % name)
    # return HttpResponse('Hello, ' + name)


def get_tweets(request):
    results = get_oss_tweets()

    output = '<html><head><title>OSS Tweets</title></head><body><ul>'
    for r in results:
        output += '<li>%s</li>' % r['text']

    output +='</ul></body></html>'
    return HttpResponse(output)
