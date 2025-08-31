from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies' : [
        {'id': 1,
         'title': 'Shrek',
         'year': 2001},
        {'id': 2,
         'title': "Shrek 2",
         'year': 2004
        },
        {'id': 3,
         'title': "Shrek Forever After",
         'year': 2010}
    ]}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home page")