from django.db import models
from datetime import datetime

class Community(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title