from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied


class BaseAPIView(APIView):
    def handle_exception(self, exc):

        if isinstance(exc, ValidationError):
            return Response({'error': exc.detail}, status=status.HTTP_400_BAD_REQUEST)

        elif isinstance(exc, PermissionDenied):
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

        elif isinstance(exc, AuthenticationFailed):
            return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
