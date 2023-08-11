from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class TestModel(models.Model):
    slug = models.SlugField(max_length=10, primary_key=True, unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updeted_at = models.DateTimeField(auto_now=True)
    integer = models.IntegerField()
    ii_stock = models.BooleanField(verbose_name='I LOVE YOU')
    email = models.EmailField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.slug



class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


