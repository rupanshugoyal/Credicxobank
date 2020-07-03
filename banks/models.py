from django.db import models

# Create your models here.
class banks(models.Model):
    name = models.CharField(max_length=11)
    id = models.IntegerField(blank=False, primary_key=True)

class bank_branches(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank_id = models.IntegerField(blank=False)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195) 
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)
    
    def __str__(self):
        return str(list([self.ifsc, self.bank_name,  self.branch, self.address, self.city, self.district, self.state]))