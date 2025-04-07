from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
from shortener.models import Link

@api_view(['GET'])
def app_health_check(request):
    return Response({"message": "App is running"}, status=200)

def redirect_to_original(request, key):
    try:
        link = Link.objects.get(key=key)
        return redirect(link.original_url)
    except Link.DoesNotExist:
        return Response({"error": "Link not found"}, status=404)

path('<str:key>/', redirect_to_original, name='redirect'),

urlpatterns = [
    path('', app_health_check, name='health_check'),
    path('auth/', include('account.urls')),
    path('shorten/', include('shortener.urls')),
    path('<str:key>/', redirect_to_original, name='redirect')
]
