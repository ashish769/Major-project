from django.shortcuts import render
from common.decorators import role_required

# Create your views here.
@role_required(allowed_roles=['metro'])
def waste_status(request):
    return render(request,'waste_status.html')
@role_required(allowed_roles=['metro'])
def vehicle_details(request):
    return render(request,'vehicles_details.html')
@role_required(allowed_roles=['metro'])
def waste_graph(request):
    return render(request,'waste_graphs.html')
@role_required(allowed_roles=['metro'])
def user_recyclers(request):
    return render(request,'user_recyclers.html')
@role_required(allowed_roles=['metro'])
def schedule(request):
    return render(request,'schedule.html')
@role_required(allowed_roles=['metro'])
def illegal_dumping(request):
    return render(request,'illegal_dumping.html')
@role_required(allowed_roles=['metro'])
def cost_estimation(request):
    return render(request,'cost_estimation.html')
@role_required(allowed_roles=['metro'])
def Profile(request):
    return render(request,'profile.html')


