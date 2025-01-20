from django.db import models

# Create your models here.
class UserData(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.email
    
class Chart(models.Model):
    title = models.CharField(max_length=100)
    timeframe = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Course(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Concept(models.Model):
    concept = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.concept
