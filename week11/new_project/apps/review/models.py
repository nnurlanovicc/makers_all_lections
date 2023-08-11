from django.db import models
from django.contrib.auth import get_user_model
from apps.main.models import Post


User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def str(self) -> str:
        return f'{self.author.username} -> {self.body}'


