from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import Vessel, Port, Voyage, Notification
from .serializers import (
    UserRegistrationSerializer, 
    UserProfileSerializer,
    VesselSerializer,
    PortSerializer,
    VoyageSerializer,
    NotificationSerializer
)

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'message': 'User registered successfully',
            'user': UserProfileSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    API endpoint to view and update user profile
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user

# Vessel CRUD
class VesselListCreateView(generics.ListCreateAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VesselDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Port CRUD
class PortListCreateView(generics.ListCreateAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PortDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Voyage CRUD
class VoyageListCreateView(generics.ListCreateAPIView):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VoyageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]