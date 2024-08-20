from django.db import models

# Create your models here.
class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligiblity = models.CharField(max_length=30)
    address = models.TextField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class BngJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligiblity = models.CharField(max_length=30)
    address = models.TextField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligiblity = models.CharField(max_length=30)
    address = models.TextField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()