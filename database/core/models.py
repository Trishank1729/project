from django.db import models
from django.contrib.auth.models import User

# 1. Port Table (Locations)
class Port(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # E.g., "Singapore"
    code = models.CharField(max_length=10, unique=True)  # E.g., "SGSIN"

    def __str__(self):
        return f"{self.name} ({self.code})"

# 2. Vessel Table (The Ships)
class Vessel(models.Model):
    name = models.CharField(max_length=100)
    imo_number = models.CharField(max_length=20, unique=True)  # Unique Ship ID
    flag = models.CharField(max_length=50)  # Country flag

    def __str__(self):
        return f"{self.name} ({self.imo_number})"

# 3. Voyage Table (The Journey)
class Voyage(models.Model):
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE, related_name='voyages')
    origin = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='arrivals')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Scheduled')  # Scheduled, Active, Completed

    def __str__(self):
        return f"{self.vessel.name}: {self.origin.code} -> {self.destination.code}"

# 4. Event Table (Tracking updates during a voyage)
class Event(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='events')
    description = models.TextField()  # E.g., "Arrived at checkpoint"
    timestamp = models.DateTimeField(auto_now_add=True)
    location_lat = models.FloatField(null=True, blank=True)
    location_long = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Event for {self.voyage} at {self.timestamp}"

# 5. Notification Table (Alerts for users)
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"