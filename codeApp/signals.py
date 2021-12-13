import django.dispatch
from django.dispatch import receiver
from django.core.signals import request_finished
from django.http.response import HttpResponse
from .models import BookModel

import django.dispatch

count_visits = django.dispatch.Signal()

@receiver(request_finished)
def handler(sender, **kwargs):
    print('Request Finished!')

def signal_home(request):
    count_visits.send(sender=BookModel)
    return HttpResponse("Django signals counter")

@receiver(count_visits)
def handler2(sender, **kwargs):
    print(sender)

