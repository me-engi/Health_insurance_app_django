from django.db import models
from PIL import Image

class InsuranceHolder(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to='insurance_photos/')
    description = models.TextField()

class FamilyMember(models.Model):
    insurance_holder = models.ForeignKey(InsuranceHolder, on_delete=models.CASCADE, related_name='family_members')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    description = models.TextField()
