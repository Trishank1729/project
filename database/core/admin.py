from django.contrib import admin
from .models import Port, Vessel, Voyage, Event, Notification

admin.site.register(Port)
admin.site.register(Vessel)
admin.site.register(Voyage)
admin.site.register(Event)
admin.site.register(Notification)