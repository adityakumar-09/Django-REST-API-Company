from django.db import models

# Create your models here.
#creating company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True) #autho incrementing primary key
    name = models.CharField(max_length=100) #company name
    location = models.CharField(max_length=100) #comapny locaiton
    about = models.TextField() #about company
    type = models.CharField(max_length=100,choices=(('IT','IT'),
                                                    ('Non IT','Non IT'),
                                                    ('Finance','Finance'),
                                                    ('Healthcare','Healthcare')),default='IT') #company type with choices
    added_date = models.DateTimeField(auto_now=True) #date when company added
    active = models.BooleanField(default=True) #active status of company