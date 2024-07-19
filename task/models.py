from django.db import models

from developer.models import Developer


class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    assignee = models.ForeignKey(Developer, related_name="tasks", on_delete=models.CASCADE, null=True,
                                 verbose_name="assignee")

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        db_table = 'task'
        permissions = [
            ('task_management', 'Can create, assign and delete tasks'),
        ]
