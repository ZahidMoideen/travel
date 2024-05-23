# destinations/views_base.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied

class BaseAPIView(generics.GenericAPIView):
    def handle_exception(self, exc):
        if isinstance(exc, ValidationError):
            return self.exception_response('Validation Error', getattr(exc, 'detail', str(exc)), status=status.HTTP_400_BAD_REQUEST)
        elif isinstance(exc, PermissionDenied):
            return self.exception_response('Permission Denied', getattr(exc, 'detail', 'You do not have permission to perform this action.'), status=status.HTTP_403_FORBIDDEN)
        elif isinstance(exc, NotFound):
            return self.exception_response('Not Found', getattr(exc, 'detail', 'The requested resource was not found.'), status=status.HTTP_404_NOT_FOUND)
        else:
            return self.exception_response('Server Error', str(exc), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def exception_response(self, error, detail, status):
        return Response({'error': error, 'detail': detail}, status=status)
