from django.shortcuts import render

# Create your views here.
def waste_status(request):
    return render(request,'waste_status.html')

def vehicle_details(request):
    return render(request,'vehicles_details.html')

def waste_graph(request):
    return render(request,'waste_graphs.html')

def user_recyclers(request):
    return render(request,'user_recyclers.html')

def schedule(request):
    return render(request,'schedule.html')

def illegal_dumping(request):
    return render(request,'illegal_dumping.html')

def cost_estimation(request):
    return render(request,'cost_estimation.html')

def Profile(request):
    return render(request,'profile.html')


