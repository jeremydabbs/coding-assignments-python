from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not 'gold' in request.session:
        request.session['gold']=0
    if not 'message' in request.session:
        request.session['message']=""
    return render(request, 'get_gold/index.html')

def process_money(request):
    add_gold = 0
    import random
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            add_gold = random.randint(10, 20)
            request.session['gold'] += add_gold
            request.session['message'] += f"<li class='win'>Earned {add_gold} from the farm!</li>"
            return redirect('/')
        if request.POST['building'] == 'cave':
            add_gold = random.randint(5, 10)
            request.session['gold'] += add_gold
            request.session['message'] += f"<li class='win'>Earned {add_gold} from the cave!</li>"
            return redirect("/")
        if request.POST['building'] == 'house':
            add_gold = random.randint(2, 5)
            request.session['gold'] += add_gold
            request.session['message'] += f"<li class='win'>Earned {add_gold} from the house!</li>"
            return redirect("/")
        if request.POST['building'] == 'casino':
            add_gold = random.randint(-50, 50)
            request.session['gold'] += add_gold
            if add_gold > 0:
                request.session['message'] += f"<li class='win'>Won {add_gold} from the casino! Lady Luck is on your side!</li>"
            else:
                request.session['message'] += f"<li class='loss'>Entered a casino and lost {add_gold}. Ouch.</li>"
            return redirect("/")

def reset(request):
    request.session['gold']=0
    request.session['message']=""
    return redirect("/")