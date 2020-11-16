from django.db import models

# Create your models here.
class DOCTOR_DETAILS(models.Model):
    Dr_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=20)
    Designation=models.CharField(max_length=20)
    Super_id=models.ForeignKey(to='self',null=True,blank=True,on_delete=models.SET_NULL)
