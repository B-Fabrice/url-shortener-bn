from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def app_health_check(request):
    return Response({"message": "App is running"}, status=200)

urlpatterns = [
    path('', app_health_check, name='health_check'),
    path('auth/', include('account.urls')),
]
