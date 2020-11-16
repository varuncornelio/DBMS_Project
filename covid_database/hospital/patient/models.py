from django.db import models
from django.db.models import Q

Male='Male'
Female='Female'
Other='Other'
gender_choices=[(Male,'Male'),(Female,'Female'),(Other,'Other')]

# Create your models here.
class PATIENT_DETAILS(models.Model):
    P_id=models.IntegerField(primary_key=True, unique=True)
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=6,choices=gender_choices,default='Male')
    City=models.CharField(max_length=20,default='Null')
    Street=models.CharField(max_length=20,default='Null')
    Pincode=models.IntegerField(default=0)
    Symptomatic=models.BooleanField(default=False)
    Previous_Disease=models.CharField(max_length=20,default='Null')
    Still_Exists=models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(Age__gte=1), name='Pat_Age_gte_1'),

            models.CheckConstraint(
                check=Q(Age__lte=120), name='Pat_Age_lte_120'),

            
           

        ]

class DEPENDENT(models.Model):
    Name=models.CharField(max_length=20, primary_key=True)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=6,choices=gender_choices,default='Male')

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(Age__gte=1), name='Dep_Age_gte_1'),
            
            models.CheckConstraint(
                check=Q(Age__lte=120), name='Dep_Age_lte_120'),



        ]
                 

