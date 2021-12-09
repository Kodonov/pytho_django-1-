from django.db import models

# Create your models here.

class Posts(models.Model):
    tittle = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)






