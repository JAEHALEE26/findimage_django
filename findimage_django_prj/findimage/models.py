from django.db import models
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, \
    GoogleDrivePermissionRole, GoogleDriveFilePermission

# Create your models here.

permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.USER,
   "findimage123@gmail.com"
)

gd_storage = GoogleDriveStorage(permissions=(permission, ))

class Gallery(models.Model):
    gallery_id = models.AutoField( primary_key=True)
    gallery_name = models.CharField(max_length=200)
    gallery_img = models.ImageField(upload_to='gallery/', storage=gd_storage)


