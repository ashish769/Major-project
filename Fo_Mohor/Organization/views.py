from django.shortcuts import render

# Create your views here.
def receiver(request):
    return render(request,'receiver.html')
