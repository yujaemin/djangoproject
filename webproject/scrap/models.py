from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    uid = models.CharField(max_length=20, primary_key=True)
    site = models.CharField(max_length=20)
    title = models.TextField()
    content = models.TextField()
    view_count = models.IntegerField()
    comment_count = models.IntegerField()
    crwal_time = models.DateTimeField()
    article_time = models.DateTimeField()

    def publish(self):
        self.save()
