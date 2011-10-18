from django.http import HttpResponse
from django.shortcuts import render
from libosstweets import get_oss_tweets

def index(request):
    return HttpResponse('Hello, OSS Members!')

def greet(request, name):
    return HttpResponse('Hello, %s' % name)
    # return HttpResponse('Hello, ' + name)

def get_tweets(request):
    results = get_oss_tweets()
    return render(request, 'tweets.html', {'results': results})


# Almost equivalent to
# public HttpResponse index(HttpRequest request){
#     return new HttpResponse("Hello World"))
# }
