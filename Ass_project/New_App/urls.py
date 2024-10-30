from django.urls import path
from . import views


urlpatterns = [
    path('', views.members, name='members'),
    path("page2/", views.page2, name = "page2"),
    path("members/", views.members, name= "member" ),
    path("student/<int:id>/", views.student_detail, name="student_detail"),  
]