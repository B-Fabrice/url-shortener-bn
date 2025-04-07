from django.urls import path
from account.views import (
    create_account,
    Login
)

urlpatterns = [
    path('register/', create_account, name='create_account'),
    path('login/', Login.as_view(), name='sign-in'),
]