from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('operator', 'Operator'),
        ('analyst', 'Analyst'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operator')
    company = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    class Meta:
        db_table = 'users'

class Vessel(models.Model):
    VESSEL_TYPES = [
        ('cargo', 'Cargo'),
        ('tanker', 'Tanker'),
        ('passenger', 'Passenger'),
        ('fishing', 'Fishing'),
    ]
    
    CARGO_TYPES = [
        ('container', 'Container'),
        ('bulk', 'Bulk Cargo'),
        ('liquid', 'Liquid Cargo'),
        ('general', 'General Cargo'),
        ('none', 'None'),
    ]
    
    imo_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    vessel_type = models.CharField(max_length=50, choices=VESSEL_TYPES)
    cargo_type = models.CharField(max_length=50, choices=CARGO_TYPES, blank=True, null=True)  # NEW
    flag = models.CharField(max_length=100)
    operator = models.CharField(max_length=255, blank=True, null=True)  # NEW
    
    # Position fields (keeping both naming conventions for compatibility)
    current_latitude = models.FloatField(null=True, blank=True)
    current_longitude = models.FloatField(null=True, blank=True)
    last_position_lat = models.FloatField(null=True, blank=True)  # NEW - same as current_latitude
    last_position_lon = models.FloatField(null=True, blank=True)  # NEW - same as current_longitude
    
    current_speed = models.FloatField(null=True, blank=True)
    destination = models.CharField(max_length=255, blank=True)
    eta = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'vessels'
        
    def __str__(self):
        return f"{self.name} ({self.imo_number})"
    
    def save(self, *args, **kwargs):
        # Auto-sync position fields
        if self.current_latitude:
            self.last_position_lat = self.current_latitude
        if self.current_longitude:
            self.last_position_lon = self.current_longitude
        super().save(*args, **kwargs)

class Port(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    class Meta:
        db_table = 'ports'
        
    def __str__(self):
        return f"{self.name} ({self.code})"

class Voyage(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('delayed', 'Delayed'),
    ]
    
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE, related_name='voyages')
    origin_port = models.ForeignKey(Port, on_delete=models.SET_NULL, null=True, related_name='departures')
    destination_port = models.ForeignKey(Port, on_delete=models.SET_NULL, null=True, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='scheduled')
    
    class Meta:
        db_table = 'voyages'
        ordering = ['-departure_time']
        
    def __str__(self):
        return f"{self.vessel.name}: {self.origin_port} → {self.destination_port}"

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('alert', 'Alert'),
        ('info', 'Information'),
        ('warning', 'Warning'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES, default='info')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'notifications'
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.title} - {self.user.username}"