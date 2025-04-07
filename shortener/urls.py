from django.urls import path
from shortener.views import (
    shorten,
    urls,
)

urlpatterns = [
    path('', shorten, name='shorten'),
    path('urls/', urls, name='urls'),
]