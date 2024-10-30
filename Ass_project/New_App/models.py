from django.db import models

    # Create your models here.
class Student(models.Model):
    #profile = models.ImageField( height_field=None, width_field=None, max_length=None)
    surname = models.CharField(max_length= 200)
    first_name = models.CharField(max_length= 150)
    status = models.CharField(max_length=225)
    rating = models.FloatField(default=0.0)
   
    def __str__(self):
        return self.surname


class Student_profile(models.Model):
    student = models.OneToOneField(Student, on_delete = models.CASCADE, related_name = "profile")
    username = models.CharField(max_length=155)
    date_of_birth = models.DateField()
    address = models.TextField()
    profile_pic = models.ImageField(upload_to="Student_profile",height_field=None, width_field=None, max_length=None )
    date_joined = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.username


class Program(models.Model):
    course = models.CharField(max_length=200)
    grade = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete= models.CASCADE)

    def __str__(self):
        return self.course

class Cohort(models.Model):
    cohort_name = models.CharField(max_length=200)
    date_join = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Student, related_name="cohort")

    def __str__(self):
        return self.cohort_name
