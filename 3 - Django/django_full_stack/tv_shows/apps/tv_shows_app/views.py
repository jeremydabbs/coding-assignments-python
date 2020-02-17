from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show

# Create your views here.
def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, "tv_shows_app/index.html", context)

def new_show(request):
    return render(request, "tv_shows_app/create.html")

def create(request): # this function is taking in the data from the Add a New Show form
    ## this is my original code before validation
    # if request.method == 'POST':
    #     Show.objects.create(
    #         title = request.POST['title'],
    #         network = request.POST['network'],
    #         release_date = request.POST['release_date'],
    #         description = request.POST['description'],
    # )
    # return redirect('/shows')
    #
    #
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        if request.method == 'POST':
            Show.objects.create(
                title = request.POST['title'],
                network = request.POST['network'],
                release_date = request.POST['release_date'],
                description = request.POST['description'],
        )
        # messages.success(request, "TV show successfully added")
        # redirect to a success route
        return redirect('/shows')

def tv_show_info(request, show_id):
    if request.method == "GET":
        context = {
            'shows': Show.objects.get(id = show_id)
        }
        return render(request, "tv_shows_app/tv_show_info.html", context)

def edit_show(request, show_id):
    if request.method == "GET":
        object = Show.objects.get(id = show_id)
        print(object.title)
        context = {
            'this_show': Show.objects.get(id = show_id)
        }

        return render(request, "tv_shows_app/edit_show.html", context)

def update(request, show_id): # this function is taking in data from the Edit Show form to update tv show data
    ## this is my original code before validation
    # if request.method == 'POST':
    # # An example is on the ORM CRUD Commands page
    #     show_to_update = Show.objects.get(id=show_id)
    #     show_to_update.title = request.POST['title']
    #     show_to_update.network = request.POST['network']
    #     show_to_update.release_date = request.POST['release_date']
    #     show_to_update.description = request.POST['description']
    #     show_to_update.save()	# needed to ensure all changes to the existing record get saved to the database
    # return redirect(f'/shows/{show_id}')
    #
    #
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{show_id}/edit')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        if request.method == 'POST':
            show_to_update = Show.objects.get(id=show_id)
            show_to_update.title = request.POST['title']
            show_to_update.network = request.POST['network']
            show_to_update.release_date = request.POST['release_date']
            show_to_update.description = request.POST['description']
            show_to_update.save()
            # messages.success(request, "Blog successfully updated")
            # redirect to a success route
            return redirect(f'/shows/{show_id}')

def destroy(request, show_id): # this function is to delete a tv show from the database
    if request.method == 'POST':
        # Show.objects.get(id=show_id).delete()
        # a two-line command below if needed
        show_to_delete = Show.objects.get(id=show_id)
        show_to_delete.delete()
    return redirect('/shows')
