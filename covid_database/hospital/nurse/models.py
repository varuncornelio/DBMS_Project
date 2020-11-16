from django.db import models

# Create your models here.
class NURSE_DETAILS(models.Model):
    Nurse_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=20)
    Super_id=models.ForeignKey(to='self',null=True,blank=True,on_delete=models.SET_NULL)