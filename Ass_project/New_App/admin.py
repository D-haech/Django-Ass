from django.contrib import admin
from .models import Student, Student_profile, Program,Cohort

# Register your models here.
admin.site.register(Student)
admin.site.register(Program)
admin.site.register(Student_profile)
admin.site.register(Cohort)