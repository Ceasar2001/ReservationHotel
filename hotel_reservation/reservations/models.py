from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return self.name