from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    maincontent = models.TextField()
    is_private = models.BooleanField(default=True)

    def __str__(self):
        return self.title
