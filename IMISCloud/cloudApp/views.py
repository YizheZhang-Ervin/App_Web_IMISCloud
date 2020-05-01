from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from cloudApp.crud import retrieve_user, create_file, retrieve_userobj, \
    retrieve_file_filter_owner_filetype, retrieve_file_filter_attribute, retrieve_file_filter_filename


def login(request):
    if request.method == "GET":
        try:
            if request.session['account'] and request.session['password']:
                return render(request, 'index.html')
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


def upload(request):
    if request.method == "GET":
        return render(request, 'upload.html')
    elif request.method == "POST":
        sf = request.POST.get('selectfile')
        fn = request.POST.get('filename')
        ft = request.POST.get('filetype')
        attr = request.POST.get('attribute')
        owner = retrieve_userobj(request.session['account'])
        if create_file(sf, fn, ft, attr, owner):
            messages.success(request, "Upload Success")
            return render(request, 'upload.html')
        else:
            messages.warning(request, "Upload Failed")
            return render(request, 'upload.html')


def searchresult(request):
    if request.method == "GET":
        result_type = request.GET.get('resulttype')
        rst = ''
        owner = request.session['account']
        if result_type == 'pic':
            rst = retrieve_file_filter_owner_filetype(owner, 'image')
        elif result_type == 'music':
            rst = retrieve_file_filter_owner_filetype(owner, 'music')
        elif result_type == 'video':
            rst = retrieve_file_filter_owner_filetype(owner, 'video')
        elif result_type == 'file':
            rst = retrieve_file_filter_owner_filetype(owner, 'file')
        elif result_type == 'shared':
            rst = retrieve_file_filter_attribute('shared')
        return render(request, "result.html", {"rst": rst})
    elif request.method == "POST":
        filename = request.POST.get("filename")
        rst = retrieve_file_filter_filename(filename)
        return render(request, "result.html", {'rst': rst})


def recycle(request):
    return render(request, "recycle.html")
