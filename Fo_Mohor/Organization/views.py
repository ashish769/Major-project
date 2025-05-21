from django.shortcuts import render,get_object_or_404,redirect
from common.decorators import role_required
from common.functions import haversine_distance_time
from Household.models import WasteReport
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
@role_required(allowed_roles=['organization'])

@role_required(allowed_roles=['organization'])

def get_location(request):
    if request.method == "POST":
        data = json.loads(request.body)
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        # ✅ Save to session
        request.session['receiver_lat'] = latitude
        request.session['receiver_lon'] = longitude

        print(f"✅ Saved in session → Lat: {latitude}, Lon: {longitude}")
        return JsonResponse({"status": "success", "lat": latitude, "lon": longitude})

    return JsonResponse({"status": "error"}, status=400)

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

    # ✅ Get receiver location from session
    lat2 = request.session.get('receiver_lat')
    lon2 = request.session.get('receiver_lon')

    for report in reports:
        try:
            lat1, lon1 = map(str.strip, report.location.split(','))
            report.lat = lat1
            report.lng = lon1

            if lat1 and lon1 and lat2 and lon2:
                distance, time = haversine_distance_time(
                    float(lat1), float(lon1),
                    float(lat2), float(lon2)
                )
                report.distance = distance
                report.eta_minutes = time
            else:
                report.distance = None
                report.eta_minutes = None
        except Exception:
            report.lat = ''
            report.lng = ''
            report.distance = None
            report.eta_minutes = None

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
    
