from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=256, blank=False )
    description = models.TextField(max_length=400, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['complete']

    def __str__(self):
        return self.title



