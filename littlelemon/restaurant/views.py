from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print("home called")
    return HttpResponse("Hello rahul. Welcome to Food Ordering API.")