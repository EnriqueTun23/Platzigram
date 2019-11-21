"""Platzifgrma Urks modele """
from django.http import HttpResponse

#datetime
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('oh, hi! Current server time is {now}'.format(now=str(now)))


def hi(request):
    numbers = [int (i) for i in request.GET['numbers'].split(',')]
    sorted_ints =  sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')



def say_hi(request, name, age):
    if age < 12:
        message = 'Sorri {}, you are not allowed hee'.format(name)
    else:
        message = 'Hello, {}: welcome to Platzigram'.format(name)

    return HttpResponse(message)