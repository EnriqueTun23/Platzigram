

# Create your views here.
from django.shortcuts import render

from datetime import datetime

posts = [
    {
        'name': 'Mont blac',
        'user': {
            'name': 'yesica cortes',
            'picture' : 'https://picsum.photos/100/100/',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs '),
        'photo' : 'https://picsum.photos/800/600/',
    },
    {
        'name': 'Via lactea',
        'user': {
            'name': 'Pepito cortes',
            'picture' : 'https://picsum.photos/100/100/',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs '),
        'photo' : 'https://picsum.photos/800/800/',
    },
    {
        'name': 'Nuevo auditorio',
        'user': {
            'name': 'Enrique cortes',
            'picture' : 'https://picsum.photos/100/100/',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs '),
        'photo' : 'https://picsum.photos/500/700/',
    },
]


def list_posts(request):
    return render(request, 'posts/feel.html', {'posts': posts})