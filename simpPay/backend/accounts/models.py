from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=200)
    is_verfied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username