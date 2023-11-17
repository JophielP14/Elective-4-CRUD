from django.db import models

# Create your models here.
class Member(models.Model):
    
    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
    )
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date = models.DateField()
    contract_duration = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)

    def __str__(self):
        return self.lastname