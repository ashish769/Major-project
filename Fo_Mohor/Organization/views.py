from django.shortcuts import render
from common.decorators import role_required

# Create your views here.
@role_required(allowed_roles=['organization'])
def receiver(request):
    return render(request,'receiver.html')
