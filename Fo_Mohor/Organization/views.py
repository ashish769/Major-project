from django.shortcuts import render
from common.decorators import role_required

# Create your views here.
@role_required(allowed_roles=['organization'])

def requests_view(request):
    return render(request, 'requests.html')

def route_view(request):
    return render(request, 'route.html')

def profile_view(request):
    return render(request, 'reciever_profile.html')
