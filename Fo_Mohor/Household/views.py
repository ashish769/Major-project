from django.shortcuts import render
from common.decorators import role_required

# Create your views here.
@role_required(allowed_roles=['household'])
def waste_report(request):
    return render(request,'report.html')

@role_required(allowed_roles=['household'])
def illegal_dumping(request):
    return render(request,'illegal.html')

@role_required(allowed_roles=['household'])
def household_profile(request):
    return render(request,'household_profile.html')

@role_required(allowed_roles=['household'])
def household_notification(request):
    return render(request,'household_notification.html')

@role_required(allowed_roles=['household'])
def map_view(request):
    return render(request,'map.html')