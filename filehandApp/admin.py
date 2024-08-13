from django.contrib import admin
from .models import CustomUser
from .models import UploadedFile

admin.site.register(UploadedFile)
