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

    def __str__(self):
        return self.name +" - "+ self.location


#employee model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    about=models.TextField(max_length=100)
    position = models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('Software Developer','sd'),
        ('Backend Developer','BD')
    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)