from django.db import models
from django.utils import timezone
# Create your models here.
class company(models.Model):
    company_name = models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    company_type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                          ('E-Commerce','E-Commerce'),
                                                          ('BPO','BPO')))
    added_date=models.DateTimeField(default=timezone.now)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
class employee(models.Model):
    name=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=100,)
    phone_no= models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    Working = models.BooleanField(default=True)
    designation=models.CharField(max_length=100, choices=(('Intern','Intern'),
                                                   ('Jr. developer','Jr. developer'),
                                                   ('Senior developer','senior developer')))
    #added_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    actual_testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials/")
    rating=models.IntegerField(max_length=1)

    def __str__(self):
        return self.actual_testimonial