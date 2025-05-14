from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class WasteReport(models.Model):
    WASTE_TYPE_CHOICES=[
        ('organic','Organic'),
        ('nonorganic','Non-Organic'),
        ('ewaste','E-Easte')
    ]
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('completed','Completed'),
        ('cancelled','Cancelled')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPE_CHOICES)
    items = models.JSONField()  
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    report_time = models.DateTimeField(default=timezone.now)
    points = models.IntegerField(default=0) 
    collected_by = models.IntegerField(blank=True, default=0)  
    collected_at = models.DateTimeField(null=True, blank=True, default=None)


    def __str__(self):
        return f"{self.user.username} - {self.waste_type} ({self.status})"
    

class IllegalDumping(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    Area=models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media/')
    status = models.CharField(max_length=20, default='pending',blank=True) 
    report_time = models.DateTimeField(default=timezone.now)
    points = models.IntegerField(default=0) 

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/')

    def __str__(self):
        return self.user.username
