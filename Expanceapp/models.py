from django.db import models

# Create your models here.

class Expence(models.Model):
    spend_on = models.CharField(max_length=100)
    date = models.DateTimeField()
    money = models.DecimalField(max_digits=8 , decimal_places=2)

    def __str__(self):
        return self.spend_on
