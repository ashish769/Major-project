import math

def haversine_distance_time(lat1, lon1, lat2, lon2, avg_speed_kmph=20):
    """
    Calculate the great-circle distance between two points 
    on the Earth (specified in decimal degrees) using the Haversine formula,
    and estimate the driving time.
    
    Parameters:
    lat1, lon1: Latitude and Longitude of Point A
    lat2, lon2: Latitude and Longitude of Point B
    avg_speed_kmph: Average driving speed in kilometers per hour
    
    Returns:
    distance_km: Distance in kilometers
    time_minutes: Estimated driving time in minutes
    """
    
    R = 6371  # Radius of Earth in km

    # Convert degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Haversine formula
    a = math.sin(delta_phi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_km = R * c

    # Estimated time (in minutes)
    time_hours = distance_km / avg_speed_kmph
    time_minutes = time_hours * 60

    return round(distance_km, 2), round(time_minutes, 2)
