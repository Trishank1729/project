from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Vessel, Port, Voyage, Notification

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'role', 'company', 'is_staff']
    list_filter = ['role', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'company', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('role', 'company', 'phone')}),
    )

@admin.register(Vessel)
class VesselAdmin(admin.ModelAdmin):
    list_display = ['name', 'imo_number', 'vessel_type', 'cargo_type', 'flag', 'operator', 'current_speed', 'last_updated']
    list_filter = ['vessel_type', 'cargo_type', 'flag']
    search_fields = ['name', 'imo_number', 'operator']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('imo_number', 'name', 'vessel_type', 'cargo_type', 'flag', 'operator')
        }),
        ('Position Data', {
            'fields': ('current_latitude', 'current_longitude', 'last_position_lat', 'last_position_lon', 'current_speed')
        }),
        ('Journey Information', {
            'fields': ('destination', 'eta')
        }),
    )
@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'country', 'latitude', 'longitude']
    list_filter = ['country']
    search_fields = ['name', 'code', 'country']

@admin.register(Voyage)
class VoyageAdmin(admin.ModelAdmin):
    list_display = ['vessel', 'origin_port', 'destination_port', 'departure_time', 'status']
    list_filter = ['status', 'departure_time']
    search_fields = ['vessel__name']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'notification_type', 'is_read', 'created_at']
    list_filter = ['notification_type', 'is_read', 'created_at']
    search_fields = ['title', 'message', 'user__username']