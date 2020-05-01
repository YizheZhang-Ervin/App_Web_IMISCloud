from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from cloudApp.crud import retrieve_user, retrieve_file_filter_owner


def login(request):
    if request.method == "GET":
        try:
            if request.session['account'] and request.session['password']:
                return render(request, 'index.html',
                              {'files': retrieve_file_filter_owner(request)})
        except Exception:
            return render(request, 'login.html')
    elif request.method == "POST":
        try:
            account = request.POST.get('account')
            password = request.POST.get('password')
            remember = request.POST.get('remember')
            if retrieve_user(account, password):
                request.session['account'] = account
                request.session['password'] = password
                request.session['rememberme'] = remember
                messages.success(request, "Login success")
                return render(request, 'index.html',
                              {'account': request.session['account'], 'password': request.session['password']})
            else:
                messages.warning(request, "Wrong Account or Password")
                return render(request, 'login.html')
        except Exception:
            messages.warning(request, "Wrong Account or Password")
            return render(request, 'login.html')


def register(request):
    pass


def index(request):
    return render(request, 'index.html')
