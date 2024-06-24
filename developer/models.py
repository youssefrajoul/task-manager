from django.db import models


class Developer(models.Model):
    first_name = models.CharField("first name", max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'developer'


class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    assignee = models.ForeignKey(Developer, related_name="tasks", on_delete=models.CASCADE, null=True,
                                 verbose_name="assignee")

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        db_table = 'task'
