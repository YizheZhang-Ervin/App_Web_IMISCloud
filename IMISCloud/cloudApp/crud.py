# Database CRUD functions
from cloudApp.models import CloudStorage, CloudUser
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages


# create file
def create_file(selectfile, filename, filetype, attribute, owner):
    # create unique new file
    cs = CloudStorage.CStorage.get_or_create(owner=owner, file=selectfile, filename=filename,
                                             filetype=filetype, attribute=attribute)
    if cs:
        return True


# retrieve file
def retrieve_file_all(request):
    return CloudStorage.CStorage.all()


def retrieve_file_filter_owner_filetype(owner, filetype):
    rs = CloudStorage.CStorage.filter(owner__account=owner, filetype=filetype)
    return rs


def retrieve_file_filter_filename(filename):
    rs = CloudStorage.CStorage.filter(filename__contains=filename)
    return rs


def retrieve_file_filter_attribute(attribute):
    rs = CloudStorage.CStorage.filter(attribute=attribute)
    return rs


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


# retrieve user id
def retrieve_userobj(account):
    rs1 = CloudUser.CUser.get(account=account)
    return rs1


# create test user
def create_testuser(request):
    cs = CloudUser.CUser.get_or_create(name='001', account='001',
                                       password='001')
    messages.success(request, "Sign up Success")
    return HttpResponse("success")
