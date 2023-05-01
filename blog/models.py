from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225, blank=False, null=False)
    content = models.TextField('Post Body', blank=False, null=False)
    author = models.CharField(max_length=225, blank=False, null=False)
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title