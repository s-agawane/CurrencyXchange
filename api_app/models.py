from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Extending existing user model to add wallet balance and profile picture
class extend_user(models.Model):
    # import user model inside this model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # create image field for storing profile photos
    profile_photo = models.ImageField(default='default.png', upload_to='profile_photos')
    # create field to store wallet balance
    wallet_balance = models.FloatField(default=0.0)


