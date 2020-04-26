from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
from django.contrib.auth.models import User

class MainMenu(models.Model):
    created_at = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=0)
    image = models.ImageField(blank=True, upload_to='news')
    description = RichTextField()
    page_visit = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=60)
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE)
    slug = models.CharField(max_length=60, unique=True)
    status = models.BooleanField(default= 0)
    category = models.CharField(max_length=60)
    tags = models.CharField(max_length=60)
    image =models.ImageField(blank=True,upload_to="blog")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    description = RichTextField()
    def __str__(self):
        return self.title