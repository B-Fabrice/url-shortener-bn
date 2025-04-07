from django.conf import settings
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed

class HasAPISecret(permissions.BasePermission):
    message = 'Invalid or missing API key.'
    def has_permission(self, request, view):
        api_key = request.headers.get('X-API-KEY')
        if api_key is None:
            raise AuthenticationFailed('API key is missing')
        if api_key != settings.API_SECRET_KEY:
            raise AuthenticationFailed('Invalid API key')
        return True
        