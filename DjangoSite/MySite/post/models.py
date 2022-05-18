from django.db import models
from django.conf import settings


def upload_location(instance, filename):
    return f'{instance.id}, {filename}'


class Post(models.Model):
    title = models.CharField(max_length=70)

    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field')

    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    owner = models.ForeignKey(
                             settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f'/posts/detail/{self.id}'

    def __str__(self):
        return self.title
