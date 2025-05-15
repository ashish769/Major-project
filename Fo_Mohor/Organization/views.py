from django.shortcuts import render,get_object_or_404,redirect
from common.decorators import role_required
from Household.models import WasteReport

# Create your views here.
@role_required(allowed_roles=['organization'])

@role_required(allowed_roles=['organization'])

def requests_view(request):
    user_type = request.user.organization.waste_type
    
    if user_type == 'Degradable':
        reports = WasteReport.objects.filter(status='pending', waste_type='organic')
    elif user_type == 'Non-degradable':
        reports = WasteReport.objects.filter(status='pending', waste_type='nonorganic')
    elif user_type == 'E-waste':
        reports = WasteReport.objects.filter(status='pending', waste_type='ewaste')
    else:
        reports = WasteReport.objects.none()

    # Add lat and lng fields from report.location
    for report in reports:
        try:
            lat, lng = map(str.strip, report.location.split(','))
            report.lat = lat
            report.lng = lng
        except Exception:
            report.lat = ''
            report.lng = ''

    context = {'reports': reports}
    return render(request, 'requests.html', context)

def accepted_requests(request):
    user_type = request.user.organization.waste_type
    
    if user_type == 'Degradable':
        reports = WasteReport.objects.filter(status='accepted', waste_type='organic')
    elif user_type == 'Non-degradable':
        reports = WasteReport.objects.filter(status='accepted', waste_type='nonorganic')
    elif user_type == 'E-waste':
        reports = WasteReport.objects.filter(status='accepted', waste_type='ewaste')
    else:
        reports = WasteReport.objects.none()

    # Add lat and lng fields from report.location
    for report in reports:
        try:
            lat, lng = map(str.strip, report.location.split(','))
            report.lat = lat
            report.lng = lng
        except Exception:
            report.lat = ''
            report.lng = ''

    context = {'reports': reports}
    return render(request, 'accepted_requests.html', context)


def route_view(request):
    return render(request, 'route.html')

def profile_view(request):
    return render(request, 'reciever_profile.html')


def accept_request(request, report_id):
    report = get_object_or_404(WasteReport, id=report_id)
    report.status = 'accepted'
    report.collected_by = request.user.organization.org_name
    report.save()
    
    # Redirect to the 'requests' URL
    return redirect('requests')
    