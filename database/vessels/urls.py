from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, 
    UserProfileView,
    VesselListCreateView,
    VesselDetailView,
    PortListCreateView,
    PortDetailView,
    VoyageListCreateView,
    VoyageDetailView,
)

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/profile/', UserProfileView.as_view(), name='profile'),
    
    # Vessel endpoints
    path('vessels/', VesselListCreateView.as_view(), name='vessel-list'),
    path('vessels/<int:pk>/', VesselDetailView.as_view(), name='vessel-detail'),
    
    # Port endpoints
    path('ports/', PortListCreateView.as_view(), name='port-list'),
    path('ports/<int:pk>/', PortDetailView.as_view(), name='port-detail'),
    
    # Voyage endpoints
    path('voyages/', VoyageListCreateView.as_view(), name='voyage-list'),
    path('voyages/<int:pk>/', VoyageDetailView.as_view(), name='voyage-detail'),
]