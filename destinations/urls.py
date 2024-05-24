from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import DestinationListCreate, DestinationRetrieveUpdateDestroy, UserCreate, UserLogin

urlpatterns = [
    path('destinations/', DestinationListCreate.as_view(), name='destination-list-create'),
    path('destinations/<int:pk>/', DestinationRetrieveUpdateDestroy.as_view(), name='destination-detail'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('register/', UserCreate.as_view(), name='user-register'),
]
