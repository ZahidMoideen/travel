import logging
from rest_framework import generics, permissions, exceptions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Destination
from .serializers import DestinationSerializer, UserSerializer
from .views_base import BaseAPIView


logger = logging.getLogger(__name__)

class DestinationListCreate(BaseAPIView, generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error in DestinationListCreate create: {e}")
            return self.handle_exception(e)

class DestinationRetrieveUpdateDestroy(BaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        try:
            obj = super().get_object()
            return obj
        except exceptions.NotFound:
            raise exceptions.NotFound("Data not found.")

    def handle_exception(self, exc):
        logger.error(f"Exception occurred: {exc}")
        if isinstance(exc, exceptions.ValidationError):
            return Response({'detail': str(exc)}, status=exc.status_code)
        if isinstance(exc, exceptions.NotFound):
            return Response({'detail': 'Not found.'}, status=404)
        return Response({'detail': 'No data found.'}, status=204)

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception as e:
            return self.handle_exception(e)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return self.handle_exception(e)

    def destroy(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            self.perform_destroy(obj)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except exceptions.NotFound as e:
            logger.error(f"Not found error in destroy: {e}")
            return Response({'detail': 'Data not found.'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error in destroy: {e}")
            return self.handle_exception(e)

class UserCreate(BaseAPIView, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error in UserCreate create: {e}")
            return self.handle_exception(e)

class UserLogin(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            raise AuthenticationFailed('Invalid username or password')

class UserLogout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'detail': 'User is already logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error in UserLogout post: {e}")
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
