# from django.shortcuts import render

# Create your views here.

# Sample from first exercise
# from django.shortcuts import render, HttpResponse
# def index(request):
# 	return HttpResponse("this is the equivalent of @app.route('/')!")

from django.shortcuts import render
from time import localtime, gmtime, strftime
    
def index(request):
    context = {
        "date": strftime("%A, %B %d, %Y", localtime()),
        "time": strftime("%I:%M %p", localtime())
    }
    return render(request,'show_time/index.html', context)
