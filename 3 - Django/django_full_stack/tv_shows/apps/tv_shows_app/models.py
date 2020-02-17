from __future__ import unicode_literals
from django.db import models


# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 1:
            errors["title"] = "Title should not be blank"
        if len(postData['network']) < 1:
            errors["network"] = "Network should not be blank"
        if len(postData['release_date']) < 1:
            errors["release_date"] = "Release date should not be blank"
        if len(postData['description']) < 1:
            errors["description"] = "Show description should not be blank"
        return errors

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=55)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()