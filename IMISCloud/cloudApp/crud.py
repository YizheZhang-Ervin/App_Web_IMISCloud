# Database CRUD functions
from cloudApp.models import CloudStorage, CloudUser
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages


# create file
def create_file(selectfile, filename, fn_origin, filetype, attribute, owner):
    # create unique new file
    cs = CloudStorage.CStorage.get_or_create(owner=owner, file=selectfile, filename=filename, filename_origin=fn_origin,
                                             filetype=filetype, attribute=attribute)
    if cs:
        return True


# retrieve file
def retrieve_file_all(request):
    return CloudStorage.CStorage.all()


def retrieve_file_filter_owner_filetype(owner, filetype):
    # user self file + given filetype + saved file
    rs = CloudStorage.CStorage.filter(owner__account=owner, filetype=filetype, status="saved")
    return rs


def retrieve_recycle(owner):
    # user self file + deleted file
    rs = CloudStorage.CStorage.filter(owner__account=owner, status="deleted")
    return rs


def retrieve_file_filter_filename(owner, filename):
    # user self file + given filename + saved file
    rs = CloudStorage.CStorage.filter(owner__account=owner, filename__contains=filename, status="saved")
    return rs


def retrieve_file_filter_attribute(attribute):
    # shared or private file + saved file
    rs = CloudStorage.CStorage.filter(attribute=attribute, status="saved")
    return rs


# update all file
def update_all_file(filename, filetype):
    ud = CloudStorage.CStorage.all().update(filename=filename, filetype=filetype)
    if ud:
        return True


# update one file
def update_one_file(filename, filetype, fileid):
    ud = CloudStorage.CStorage.filter(id=fileid).update(filename=filename, filetype=filetype)
    if ud:
        return True


# drop file to bin
def update_one_file_to_bin(fileid):
    ud = CloudStorage.CStorage.filter(id=fileid).update(status="deleted")
    if ud:
        return True


# drop file to bin
def recover_file(fileid):
    ud = CloudStorage.CStorage.filter(id=fileid).update(status="saved")
    if ud:
        return True


# delete file
def delete_file(fileid):
    cs = CloudStorage.CStorage.get(id=fileid).delete()
    if cs:
        return True


# create user
def create_user(name, account, password):
    cs = CloudUser.CUser.get_or_create(name=name, account=account, password=password)
    if cs:
        return True


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
