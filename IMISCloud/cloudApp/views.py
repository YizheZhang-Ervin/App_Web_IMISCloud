from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from cloudApp.crud import retrieve_user


def verify(request):
    if request.method == "GET":
        try:
            if request.session['account'] and request.session['password']:
                return render(request, 'index.html',
                              {'account': request.session['account'], 'password': request.session['password']})
        except Exception:
            return render(request, 'verify.html')
    elif request.method == "POST":
        try:
            account = request.POST.get('account')
            password = request.POST.get('password')
            remember = request.POST.get('remember')
            if retrieve_user(account, password):
                request.session['account'] = account
                request.session['password'] = password
                request.session['rememberme'] = remember
                return render(request, 'index.html',
                              {'account': request.session['account'], 'password': request.session['password']})
            else:
                messages.warning(request, "Wrong Account or Password")
                return render(request, 'verify.html')
        except Exception:
            messages.warning(request, "Wrong Account or Password")
            return render(request, 'verify.html')

def index(request):
    return render(request, 'index.html')
