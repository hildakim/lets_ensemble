from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
  title = models.CharField(max_length=200)
  sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender", default="1")
  receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver", default="1")
  upload_date = models.DateTimeField()
  body = models.TextField()

  def __str__(self):
    return self.title 