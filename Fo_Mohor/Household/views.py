from django.shortcuts import render
from common.decorators import role_required

# Create your views here.
@role_required(allowed_roles=['household'])
def household(request):
    return render(request,'household.html')