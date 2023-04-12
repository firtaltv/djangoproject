from django.db import models
from users.models import User
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=250)
    text = models.TextField(max_length=50)
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(null=True, blank=True)
    like = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
