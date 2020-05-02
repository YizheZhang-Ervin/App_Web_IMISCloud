from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from cloudApp.crud import retrieve_user, create_file, retrieve_userobj, \
    retrieve_file_filter_owner_filetype, retrieve_file_filter_attribute, retrieve_file_filter_filename, update_one_file, \
    update_one_file_to_bin, retrieve_recycle, recover_file, create_user, delete_file


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
                return render(request, 'index.html')
            else:
                messages.warning(request, "Wrong Account or Password")
                return render(request, 'login.html')
        except Exception:
            messages.warning(request, "Wrong Account or Password")
            return render(request, 'login.html')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        nm = request.POST.get("name")
        acc = request.POST.get("account")
        pw = request.POST.get("password")
        # try:
        if create_user(nm, acc, pw):
            request.session['account'] = acc
            request.session['password'] = pw
            request.session['rememberme'] = "true"
            messages.success(request, "Sign up Success")
            return render(request, 'login.html')
        else:
            messages.success(request, "Sign up Failed 1)Existed account name 2)other reasons")
            return render(request, 'register.html')
        # except Exception:
        #     messages.success(request, "Sign up Failed,Please try again later")
        #     return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == "GET":
        return render(request, 'upload.html')
    elif request.method == "POST":
        sf = request.FILES.get('selectfile')
        fn_origin = str(sf).split("/")[-1]
        fn = request.POST.get('filename')
        ft = request.POST.get('filetype')
        attr = request.POST.get('attribute')
        owner = retrieve_userobj(request.session['account'])
        if create_file(sf, fn, fn_origin, ft, attr, owner):
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
        owner = request.session['account']
        rst = retrieve_file_filter_filename(owner, filename)
        return render(request, "result.html", {'rst': rst})


def update(request):
    fn = request.GET.get("filename")
    ft = request.GET.get("filetype")
    fid = request.GET.get("fileid")
    if update_one_file(fn, ft, fid):
        messages.success(request, "Update Success")
    return render(request, "index.html")


def recycle(request):
    owner = request.session['account']
    rr = retrieve_recycle(owner)
    return render(request, "recycle.html", {'rst': rr})


def drop(request):
    fid = request.GET.get("fid")
    if update_one_file_to_bin(fileid=fid):
        messages.success(request, "Delete Success, also you can recover from trash bin")
    return render(request, "index.html")


def delete(request):
    fid = request.GET.get("fid")
    if delete_file(fid):
        messages.success(request, "Delete Success")
    return render(request, "index.html")


def backbin(request):
    fid = request.GET.get("fid")
    if recover_file(fileid=fid):
        messages.success(request, "Recover Success")
    return render(request, "index.html")


def clearsession(request):
    request.session.flush()
    return render(request, 'login.html')