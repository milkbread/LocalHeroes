from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    ctime = models.DateTimeField(
            default=timezone.now)
    ptime = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.ptime = timezone.now()
        self.save()

    def __str__(self):
        return self.title