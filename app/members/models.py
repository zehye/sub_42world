from django.db import models


class User(models.Model):
    CHOICE_GENDER = (
        ('m','남성'),
        ('f','여성'),
        ('x','선택안함'),
    )
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=CHOICE_GENDER)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
