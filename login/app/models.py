from django.db import models

class loginpage(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.IntegerField(primary_key=True)
    email=models.EmailField(unique=True)
    password=models.IntegerField()


class Otp(models.Model):
    otp=models.CharField(max_length=8)


