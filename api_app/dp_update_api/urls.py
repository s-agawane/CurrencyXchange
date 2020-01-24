from django.urls import path

from .views import upload_profile_photo

urlpatterns = [
    path(r'', upload_profile_photo)
    ]


