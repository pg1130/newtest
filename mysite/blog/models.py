
from django.db import models
from django.urls import reverse

from .models import *

# Create your models here.

class Post(models.Model):
    title = models.CharField("TITLE",max_length=50)
    slug = models.SlugField("SLUG",unique=True, help_text="one word for title alias.")
    description = models.CharField("DESCRIPTION",max_length=100, blank=True,help_text="simple description text.")
    content = models.TextField("CONTENT")
    create_dt = models.DateField("Create Date",auto_now_add=True)
    modify_dt = models.DateField("Modify Date",auto_now = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = "my_post"
        ordering = ("-modify_dt",)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:post_detail",args=(self.slug,))
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    def get_next(self):
        return self.get_next_by_modify_dt()
    
    