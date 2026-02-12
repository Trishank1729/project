from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Vessel, Port, Voyage, Notification

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'role', 'company', 'phone']
    
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'company', 'phone', 'date_joined', 'last_login']
        read_only_fields = ['id', 'date_joined', 'last_login']

class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = [
            'id', 
            'imo_number', 
            'name', 
            'vessel_type', 
            'cargo_type',  # NEW
            'flag', 
            'operator',  # NEW
            'current_latitude', 
            'current_longitude',
            'last_position_lat',  # NEW
            'last_position_lon',  # NEW
            'current_speed', 
            'destination', 
            'eta', 
            'last_updated'
        ]
        read_only_fields = ['last_updated', 'last_position_lat', 'last_position_lon']

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = '__all__'

class VoyageSerializer(serializers.ModelSerializer):
    vessel_name = serializers.CharField(source='vessel.name', read_only=True)
    origin_port_name = serializers.CharField(source='origin_port.name', read_only=True)
    destination_port_name = serializers.CharField(source='destination_port.name', read_only=True)
    
    class Meta:
        model = Voyage
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['created_at']