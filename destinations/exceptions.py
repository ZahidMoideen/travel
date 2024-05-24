from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError):
        detail = exc.detail
    else:
        detail = {'error': 'Internal Server Error'}

    if response is not None:
        response.data = {
            'errors': detail
        }
    return response
