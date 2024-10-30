from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import  Student
# Create your views here.


def members(request):
  #template = loader.get_template('index.html')
  students = Student.objects.all()
  context = { "students": students }
  return render(request,"index.html", context)

def page2(request):
  #temp = loader.get_template("page2.html")
  students = Student.objects.all()
  context = { "students": students, }
  return render(request,"page2.html", context )

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "index.html", {"student": student})




