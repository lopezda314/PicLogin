from django.http import HttpResponse


def home(request):
    output = 'Hello World - home'
    return HttpResponse(output)


def profile(request):
    output = 'Hello World! Configured for usernames using request context processing. My username is: ' + request.user.username
    return HttpResponse(output)