from django.contrib import admin

# Register your models here.
from .models import PATIENT_DETAILS
admin.site.register(PATIENT_DETAILS)

from patient.models import DEPENDENT
admin.site.register(DEPENDENT)