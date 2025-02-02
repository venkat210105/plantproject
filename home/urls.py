from django.contrib import admin
from django.urls import path, include
from home import views
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Plant Detection App!")

urlpatterns = [
    path("",views.index, name='home'),
    path("about/",views.about, name='about'),
    path("contact/",views.contact, name='contact'),
    path('upload/', views.upload_image, name='upload_image'),
]