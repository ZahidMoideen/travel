
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import DestinationListCreate, DestinationRetrieveUpdateDestroy, UserCreate

urlpatterns = [
    path('destinations/', DestinationListCreate.as_view(), name='destination-list-create'),
    path('destinations/<int:pk>/', DestinationRetrieveUpdateDestroy.as_view(), name='destination-detail'),
    path('api/authtoken/',obtain_auth_token, name='api_token_auth'),
    path('register/', UserCreate.as_view(), name='user-register'),

]
