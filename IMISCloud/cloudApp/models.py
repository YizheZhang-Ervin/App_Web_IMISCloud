from django.db import models

# Create your models here.
from IMISCloud.settings import MEDIA_ROOT


class CloudUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='Anonymous user')
    account = models.TextField()
    password = models.TextField()
    usertype = models.CharField(max_length=20, default='common')

    def __str__(self):
        return "CloudUser: %s" % self.name

    class Meta:
        db_table = 'CloudUser'

    CUser = models.Manager()


def upload_place(instance, filename):
    return '/'.join([MEDIA_ROOT, instance.user_name, filename])


class CloudStorage(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(CloudUser, on_delete=models.CASCADE)
    filename = models.TextField()
    filetype = models.TextField()
    file = models.FileField(upload_to=upload_place)

    def __str__(self):
        return "File: %s" % self.filename

    class Meta:
        db_table = 'CloudStorage'

    CStorage = models.Manager()