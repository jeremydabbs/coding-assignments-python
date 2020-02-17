from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# def index(request):
# 	return render(request, 'generator/index.html')

def generate(request):
	if not 'counter' in request.session:
		request.session['counter']=1
	else:
		request.session['counter']+=1
	context = {
		"word": get_random_string(length=14),
    }
	return render(request,'generator/index.html', context)

def reset(request):
	request.session['counter']=0
	return redirect ('/generate')
