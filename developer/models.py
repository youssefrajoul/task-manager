from django.db import models
from django.contrib.auth.models import AbstractUser


class Developer(AbstractUser):
    first_name = models.CharField("first name", max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def is_free(self):
        return self.tasks.count() == 0

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    is_free.boolean = True
    is_free.short_description = 'Free'

    class Meta:
        db_table = 'developer'
