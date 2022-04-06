from django.http import JsonResponse, HttpResponseNotAllowed
from django.utils import timezone

from .models import Tweet

def index(request):
    if (request.method != 'GET'):
        raise HttpResponseNotAllowed('Method not allowed')    
    
    return JsonResponse({
        'latest_tweets': list(Tweet.objects.values('username', 'message', 'pub_date'))
    })

def store(request):
    if (request.method != 'POST'):
        raise HttpResponseNotAllowed('Method not allowed')    

    username = request.POST['username']
    message = request.POST['message']
    pub_date = timezone.now()

    tweet = Tweet(username=username, message=message, pub_date=pub_date)

    tweet.save()

    return JsonResponse({
        'new_tweet': {
            'username': username,
            'message': message,
            'pub_date': pub_date
        }
    }, status=201)