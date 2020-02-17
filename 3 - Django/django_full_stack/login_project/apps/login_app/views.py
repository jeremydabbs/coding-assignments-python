from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            new_user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = pw_hash,
            )
            request.session['user_id'] = new_user.id
            request.session['first_name'] = new_user.first_name
            return redirect('/success')
    return redirect('/')




def success(request):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in.')
        return redirect('/')
    return render(request, 'login_app/success.html')

def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email = request.POST['email'])
        except: 
            messages.error(request, 'Email or password is incorrect.')
            return redirect('/')
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            return redirect('/success')
        else: 
            messages.error(request, 'Email or password is incorrect.')
            return redirect('/')
    return redirect('/')

def logout(request):
    request.session.clear()
    #del request.session['user_id']  --this would be how to remove an individual session field
    return render(request, 'login_app/index.html')