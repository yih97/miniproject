from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Community(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Communities"



