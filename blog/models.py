from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
