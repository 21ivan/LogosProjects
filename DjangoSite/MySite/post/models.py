from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
