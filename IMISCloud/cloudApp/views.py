from django.http import Http404
from django.shortcuts import render, redirect


# Create your views here.
def verify(request):
    if request.method == "GET":
        if request.session['account'] and request.session['password']:
            return render(request, 'index.html', {'account': request.session['account'], 'password': request.session['password']})
        else:
            return render(request, 'verify.html')
    elif request.method == "POST":
        account = request.POST.get('account')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        if account and password:
            request.session['account'] = account
            request.session['password'] = password
            request.session['rememberme'] = remember
            return render(request, 'index.html', {'account': request.session['account'], 'password': request.session['password']})
        else:
            raise Http404("Something Wrong with your account,please contact Manager")


def index(request):
    return render(request, 'index.html')