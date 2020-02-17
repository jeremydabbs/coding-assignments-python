from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime, timedelta
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'wall_app/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        if request.method == 'POST':
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            new_user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = pw_hash,
            )
        request.session['user_id'] = new_user.id
        request.session['first_name'] = new_user.first_name
        return redirect('/wall')

# #IN CLASS EXAMPLE:
# def register(request):
#     if request.method == 'POST':
#         errors = User.objects.basic_validator(request.POST)
#         if len(errors) > 0:
#             for key, value in errors.items():
#                 messages.error(request, value)
#             return redirect('/')
#         else:
#             pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
#             new_user = User.objects.create(
#                 first_name = request.POST['first_name'],
#                 last_name = request.POST['last_name'],
#                 email = request.POST['email'],
#                 password = pw_hash,
#             )
#             request.session['user_id'] = new_user.id
#             request.session['first_name'] = new_user.first_name
#             return redirect('/wall')
#     return redirect('/')





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
            return redirect('/wall')
        else: 
            messages.error(request, 'Email or password is incorrect.')
            return redirect('/')
    return redirect('/')

def logout(request):
    request.session.clear()
    #del request.session['user_id']  --this would be how to remove an individual session field
    return render(request, 'wall_app/index.html')




def wall(request):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in.')
        return redirect('/')
    context = {
        'messages': Message.objects.all().order_by('-created_at'),
    }
    return render(request, 'wall_app/wall.html', context)

def post_message(request):
    if request.method == "POST":
        current_user = User.objects.get(id= int(request.session['user_id']))
        Message.objects.create(
            message = request.POST['message'],
            user = current_user,
            )
    return redirect('/wall')

def delete_message(request, message_id):
    # message = Message.objects.get(id = message_id)
    # if datetime.now <= message.created_at+timedelta(minutes=30):
    if request.method == "POST":
        m = Message.objects.get(id = message_id)
        m.delete()
    return redirect('/wall')

def post_comment(request):
    if request.method == "POST":
        current_user = User.objects.get(id = int(request.session['user_id']))
        current_message_id = request.POST['message_id']
        current_message = Message.objects.get(id = current_message_id)
        Comment.objects.create(
            comment = request.POST['comment'],
            user = current_user,
            message = current_message,
        )
    return redirect('/wall')