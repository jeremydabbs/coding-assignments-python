from __future__ import unicode_literals
from django.db import models

import re
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name is too short"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name is too short"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['invalid_email'] = "Invalid email address!"
        
        # Check if email address is unique
        if len(User.objects.filter(email = postData['email'])) != 0:
            errors['not_unique_email'] = "Email is already in use"

        if len(postData['password']) < 8:
            errors["password_length"] = "Password needs to be at least 8 characters long"
        if postData['confirm_pw'] != postData['password']:
            errors["password_match"] = "Passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
