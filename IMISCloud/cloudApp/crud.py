# Database CRUD functions
from cloudApp.models import CloudStorage, CloudUser
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages


# create file
def create_file(request):
    # create unique new file
    cs = CloudStorage.CStorage.get_or_create(filename=request.POST.get("filename"),
                                             filetype=request.POST.get("filetype"), file=request.POST.get("file"))
    messages.success(request, "Upload Success")


# retrieve file
def retrieve_file_all(request):
    return CloudStorage.CStorage.all()


def retrieve_file_filter_filename(request):
    rs = CloudStorage.CStorage.filter(filename__contains=request.POST.get("filename"))
    return rs


def retrieve_file_filter_owner(request):
    rs = CloudStorage.CStorage.filter(owner__account=request.session['account'])
    return list(rs)


# update file
def update_file(request):
    CloudStorage.CStorage.all().update(filename=request.POST.get("filename"), filetype=request.POST.get("filetype"))
    messages.success(request, "Update Success")


# delete file
def delete_file(request):
    CloudStorage.CStorage.get(file=request.POST.get("file")).delete()
    messages.success(request, "Delete Success")


# create user
def create_user(request):
    cs = CloudUser.CUser.get_or_create(name=request.POST.get("name"), account=request.POST.get("account"),
                                       password=request.POST.get("password"))
    messages.success(request, "Sign up Success")


# retrieve user
def retrieve_user(account, password):
    rs1 = CloudUser.CUser.get(account=account, password=password)
    if rs1:
        return True


# create test user
def create_testuser(request):
    cs = CloudUser.CUser.get_or_create(name='001', account='001',
                                       password='001')
    messages.success(request, "Sign up Success")
    return HttpResponse("success")
