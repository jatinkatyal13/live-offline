from django.db import models

# Create your models here.

class Subscriber(models.Model):
    name = models.CharField(max_length = 100, blank = True, null = True)
    phone_number = models.CharField(max_length = 15)

    def __str__(self):
        return self.phone_number + " - " + self.name