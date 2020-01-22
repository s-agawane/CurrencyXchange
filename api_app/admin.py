from django.contrib import admin

# Register your models here.
from .models import extend_user

admin.site.register(extend_user)