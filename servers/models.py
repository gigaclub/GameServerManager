from django.db import models

# Create your models here.

class Server(models.Model):
    name = models.CharField(max_length=100)
    slots = models.IntegerField(default=20)
    port = models.IntegerField(default=0)

    def __str__(self):
        return self.name