from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name



class Comment(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.task

