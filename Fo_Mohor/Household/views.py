from django.shortcuts import render

# Create your views here.
def household(request):
    return render(request,'household.html')