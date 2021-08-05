from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
  title = models.CharField(max_length=200)
  upload_date = models.DateTimeField()
  author = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
  body = models.TextField()
  image = models.ImageField(upload_to='board/', null=True, blank=True)
  image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 100)])

  def __str__(self):
    return self.title 

  def summary(self):
    return self.body[:100]+'...'