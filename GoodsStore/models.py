from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    price = models.CharField(max_length=20, null=True, blank=True)
    upload_img = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title
