from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)

def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books_authors_app/authors.html', context)

def add_book(request): # this function is taking in the data from the Add a Book form
    if request.method == 'POST':
        Book.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
        )
    return redirect('/')

def add_author(request): # this function is taking in the data from the Add an Author form
    if request.method == 'POST':
        Author.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            notes = request.POST['notes'],
        )
    return redirect('/authors')

def show_books(request, book_id):
    context = {
        'books': Book.objects.get(id = book_id),
        'authors': Author.objects.exclude(books = book_id)
    }
    return render(request, 'books_authors_app/show_books.html', context)

def show_authors(request, author_id):
    context = {
        'authors': Author.objects.get(id = author_id),
        'books': Book.objects.exclude(authors = author_id)
    }
    return render(request, 'books_authors_app/show_authors.html', context)

def delete_book(request, book_id):
    Book.objects.get(id = book_id).delete()
    return redirect('/')

def delete_author(request, author_id):
    Author.objects.get(id = author_id).delete()
    return redirect('/authors')

def update_author(request, book_id):
    selected_author = Author.objects.get(id= int(request.POST["author"]))
    current_book = Book.objects.get(id =book_id)
    selected_author.books.add(current_book)
    return redirect(f'/books/{book_id}')

def update_book(request, author_id):
    selected_book = Book.objects.get(id= int(request.POST["book"]))
    current_author = Author.objects.get(id =author_id)
    selected_book.authors.add(current_author)
    return redirect(f'/authors/{author_id}')






# # Example from "Putting Everything Together"
# # other imports
# # from .models import Movie
# # # show all of the data from a table
# # def index(request):
# #     context = {
# #     	"all_the_movies": Movie.objects.all()
# #     }
# #     return render(request, "my_app/index.html", context)

# from .models import Book
# def index(request):
#     context = {
#         "all_the_books": Book.objects.all()
#     }
#     return render(request, "books_authors_app/index.html", context)



# # Example from class
# from .models import User  #you can use * instead of each model name if you have many models

# def index(request):
#     context = {
#         'users': User.objects.all()
#     }
#     return render(request, 'users_app/index.html', context)

# def create_user(request): # this function is taking in the data from the form
#     if request.method == 'POST':
#         User.objects.create(
#             first_name = request.POST['first_name'],
#         )
#     return redirect('/')

# def delete_user(request, user_id):
#     user = User.objects.get(id = user_id)
#     user.delete()
#     #in one line: User.objects.get(id = user_id).delete()
#     #do not call user.save() after deleting a user because it will add user back
#     return redirect('/')