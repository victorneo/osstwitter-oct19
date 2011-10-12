from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, OSS Members!')

def greet(request, name):
    return HttpResponse('Hello, %s' % name)
    # return HttpResponse('Hello, ' + name)

# Almost equivalent to
# public HttpResponse index(HttpRequest request){
#     return new HttpResponse("Hello World"))
# }
